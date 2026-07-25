#!/usr/bin/env python3
"""Dựng 5 preset nhạc nền synth của template thành file WAV dùng được cho render.

VÌ SAO CẦN: template có sẵn 5 preset nhạc (ambient · cinematic · lofi · piano ·
dark) trong `bgmPresets` (app.js:2545) nhưng CHƯA BAO GIỜ dùng được khi render —
nhạc synth do WebAudio chơi THỜI GIAN THỰC, còn nhánh headless trộn tiếng OFFLINE
bằng ffmpeg. Script này chạy đúng đồ thị âm thanh của template trong
OfflineAudioContext rồi ghi ra WAV, sau đó dùng như một file nhạc bình thường.

KHÔNG sửa app.js của deck: bảng hợp âm được ĐỌC từ trang đang mở, phần lập lịch
bơm từ ngoài vào. Deck mới không phải vá lại gì.

Khác bản chạy live (cố ý, có lý do):
  · `startBackgroundMusic` lái bằng setInterval 8s/2s — trong OfflineAudioContext
    không có đồng hồ tường, nên lập lịch tường minh: hợp âm tại t=i*8, arp tại t=j*2.
  · Độ dài = ĐÚNG MỘT VÒNG hợp âm (4 × 8s = 32s) để `-stream_loop -1` nối vòng
    không cấn: hợp âm cuối tắt dần về 0.001 đúng lúc t=32.
  · Arp chỉ đặt khi còn đủ 2,5s đuôi, tránh cắt ngang tiếng ở mối nối.

Chạy:
    .venv/bin/python dung_nhac_synth.py                 # dựng cả 5 preset
    .venv/bin/python dung_nhac_synth.py --preset lofi   # dựng 1 preset
Ra: nhac/synth_<preset>.wav  (48kHz mono) — render_headless.py tự tìm khi
preview-settings.json đặt bgm.mode="preset".
"""
from __future__ import annotations

import argparse
import asyncio
import base64

import re
import sys
import wave
from pathlib import Path

HERE = Path(__file__).resolve().parent
NHAC = HERE / "nhac"
SR = 48000
VONG = 32.0            # 4 hợp âm × 8 giây = đúng một vòng
MUC_DICH_DB = -24.1    # RMS thô — chỉ dùng cho lượt dựng đầu, KHÔNG phải thước chốt
MUC_DICH_LUFS = -22.7  # ⭐ THƯỚC THẬT: độ to cảm nhận của meta.mp3 (đo 25/07)
DINH_TRAN_DBTP = -1.0  # trần đỉnh thật sau khi nâng

# Lập lịch chạy trong trang: dùng lại nguyên đồ thị osc→filter→gain của
# playChord (app.js:2091) và playArpNote (app.js:2114).
JS_DUNG_NHAC = r"""
async ([preset, dur, SR, MUC_DICH_DB]) => {
  if (typeof bgmPresets === 'undefined') return { loi: 'trang không có bgmPresets' };
  const p = bgmPresets[preset];
  if (!p) return { loi: 'không có preset ' + preset };

  const off = new OfflineAudioContext(1, Math.ceil(SR * dur), SR);
  const master = off.createGain();
  master.gain.value = 1.0;          // âm lượng thật do ffmpeg đặt lúc trộn
  master.connect(off.destination);

  // ── hợp âm: y hệt playChord, chỉ thay audioCtx.currentTime bằng t0 tường minh
  const datHopAm = (chord, t) => {
    chord.forEach((freq, i) => {
      const osc1 = off.createOscillator();
      const osc2 = off.createOscillator();
      const gain = off.createGain();
      const filter = off.createBiquadFilter();
      osc1.type = 'sine'; osc1.frequency.value = freq;
      osc2.type = 'triangle'; osc2.frequency.value = freq * 1.003;
      filter.type = 'lowpass'; filter.frequency.value = 350 + i * 50; filter.Q.value = 0.5;
      gain.gain.setValueAtTime(0, t);
      gain.gain.linearRampToValueAtTime(0.18, t + 2);
      gain.gain.setValueAtTime(0.18, t + 5);
      gain.gain.linearRampToValueAtTime(0.001, t + 8);
      osc1.connect(gain); osc2.connect(gain); gain.connect(filter); filter.connect(master);
      osc1.start(t + i * 0.15); osc2.start(t + i * 0.15);
      osc1.stop(t + 8.5); osc2.stop(t + 8.5);
    });
  };

  // ── arp: y hệt playArpNote (có cả nhánh delay 0.375s / 0.25)
  const datArp = (note, t) => {
    const osc = off.createOscillator();
    const gain = off.createGain();
    const filter = off.createBiquadFilter();
    const delay = off.createDelay(1.0);
    const delayGain = off.createGain();
    osc.type = 'sine'; osc.frequency.value = note;
    filter.type = 'lowpass'; filter.frequency.value = 2000; filter.Q.value = 0.3;
    gain.gain.setValueAtTime(0, t);
    gain.gain.linearRampToValueAtTime(0.12, t + 0.05);
    gain.gain.exponentialRampToValueAtTime(0.03, t + 0.8);
    gain.gain.linearRampToValueAtTime(0.001, t + 2.5);
    delay.delayTime.value = 0.375; delayGain.gain.value = 0.25;
    osc.connect(filter); filter.connect(gain); gain.connect(master);
    gain.connect(delay); delay.connect(delayGain); delayGain.connect(master);
    osc.start(t); osc.stop(t + 3);
  };

  let soHopAm = 0, soArp = 0;
  for (let i = 0; i * 8 < dur; i++) {
    datHopAm(p.chords[i % p.chords.length], i * 8);
    soHopAm++;
  }
  let arpIdx = 0;
  for (let t = 0; t + 2.5 <= dur; t += 2) {
    const bang = p.arps[Math.floor(t / 8) % p.arps.length];
    datArp(bang[arpIdx % bang.length], t);
    arpIdx++; soArp++;
  }

  const buf = await off.startRendering();
  const ch = buf.getChannelData(0);
  let dinh = 0, tong = 0;
  for (let i = 0; i < ch.length; i++) {
    const a = Math.abs(ch[i]); if (a > dinh) dinh = a;
    tong += ch[i] * ch[i];
  }
  const rms = Math.sqrt(tong / ch.length);
  // Chuẩn hoá khi CÒN LÀ SỐ THỰC (bốn giọng hợp âm cộng lại đo được đỉnh ~1,2-1,3
  // ⇒ đổi thẳng sang int16 là cắt ngọn, méo nướng vĩnh viễn vào file).
  // Đích là MỨC TRUNG BÌNH của meta.mp3 (-24,1 dB đo 25/07), KHÔNG phải đỉnh:
  // bgm.volume = 0.3 và tương quan nhạc/giọng là thứ BOSS đã duyệt, đổi bản nhạc
  // mà đổi luôn độ to là đổi cả bản phối. Nhạc synth thô ra -14,5 dB, to hơn
  // meta.mp3 gần 10 dB — thả nguyên vào là nhạc át giọng.
  const rmsDich = Math.pow(10, MUC_DICH_DB / 20);
  let heSo = rms > 0 ? rmsDich / rms : 1;
  if (dinh * heSo > 0.95) heSo = 0.95 / dinh;   // chặn trần, không bao giờ cắt ngọn
  const pcm = new Int16Array(ch.length);
  for (let i = 0; i < ch.length; i++) {
    const v = Math.max(-1, Math.min(1, ch[i] * heSo));
    pcm[i] = v < 0 ? v * 0x8000 : v * 0x7FFF;
  }
  const bytes = new Uint8Array(pcm.buffer);
  let bin = ''; const CH = 0x8000;
  for (let i = 0; i < bytes.length; i += CH) bin += String.fromCharCode.apply(null, bytes.subarray(i, i + CH));
  return { b64: btoa(bin), soHopAm, soArp, dinh, rms, heSo, mau: ch.length };
}
"""


def ghi_wav(duong: Path, mau_i16: bytes, sr: int = SR) -> None:
    with wave.open(str(duong), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(mau_i16)


async def do_lufs(duong: Path) -> tuple[float, float]:
    """Trả (LUFS tích hợp, đỉnh thật dBTP) bằng ebur128 của ffmpeg."""
    proc = await asyncio.create_subprocess_exec(
        "ffmpeg", "-i", str(duong), "-af", "ebur128=peak=true", "-f", "null", "-",
        stdout=asyncio.subprocess.DEVNULL, stderr=asyncio.subprocess.PIPE)
    _, err = await proc.communicate()
    txt = err.decode("utf-8", "ignore")
    duoi = txt[txt.rfind("Integrated loudness"):]
    m_i = re.search(r"I:\s*(-?[\d.]+)\s*LUFS", duoi)
    m_p = re.search(r"Peak:\s*(-?[\d.]+)\s*dBFS", txt[txt.rfind("True peak"):])
    return (float(m_i.group(1)) if m_i else 0.0,
            float(m_p.group(1)) if m_p else 0.0)


async def nang_ve_lufs(duong: Path) -> dict:
    """Đo LUFS rồi nâng đúng hệ số để chạm MUC_DICH_LUFS — cùng lối 'đo rồi tính'
    mà dây chuyền đã dùng cho mức tiếng tổng (đừng chép số dB tay).

    VÌ SAO KHÔNG DÙNG RMS: chuẩn theo RMS thô cho cả 5 preset ra ĐÚNG -24,1 dB
    y như meta.mp3, NHƯNG BOSS nghe vẫn thấy meta TO HƠN — và tai BOSS đúng:
    đo LUFS (có trọng số tần số như tai người) ra meta -22,7 còn synth -24,5…-25,8.
    Nhạc synth toàn sine tầm thấp, RMS bằng nhau mà nghe nhỏ hơn ~2 dB.
    """
    lufs0, tp0 = await do_lufs(duong)
    nang = MUC_DICH_LUFS - lufs0
    tam = duong.with_suffix(".tmp.wav")
    proc = await asyncio.create_subprocess_exec(
        "ffmpeg", "-y", "-i", str(duong), "-af", f"volume={nang:.3f}dB",
        "-c:a", "pcm_s16le", str(tam),
        stdout=asyncio.subprocess.DEVNULL, stderr=asyncio.subprocess.DEVNULL)
    await proc.communicate()
    tam.replace(duong)
    lufs1, tp1 = await do_lufs(duong)
    return {"lufs0": lufs0, "nang": nang, "lufs": lufs1, "dinh_that": tp1}


async def dung_mot(page, preset: str) -> dict:
    kq = await page.evaluate(JS_DUNG_NHAC, [preset, VONG, SR, MUC_DICH_DB])
    if kq.get("loi"):
        raise RuntimeError(kq["loi"])
    raw = base64.b64decode(kq["b64"])
    NHAC.mkdir(parents=True, exist_ok=True)
    ra = NHAC / f"synth_{preset}.wav"
    ghi_wav(ra, raw)
    do = await nang_ve_lufs(ra)
    if do["dinh_that"] > DINH_TRAN_DBTP:
        print(f"  ⚠️ {preset}: đỉnh thật {do['dinh_that']:.1f} dBTP vượt trần "
              f"{DINH_TRAN_DBTP} — có thể méo trên loa điện thoại")
    return {"file": ra, "hop_am": kq["soHopAm"], "arp": kq["soArp"],
            "dinh_goc": kq["dinh"], "rms": kq["rms"], "he_so": kq["heSo"],
            "giay": kq["mau"] / SR, "kb": ra.stat().st_size // 1024, **do}


async def amain() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--preset", default=None,
                    help="Chỉ dựng 1 preset (ambient/cinematic/lofi/piano/dark)")
    ap.add_argument("--deck", default="headless/deck_sp01",
                    help="Deck để mượn bảng hợp âm (chỉ ĐỌC, không sửa gì)")
    args = ap.parse_args()

    deck = (HERE / args.deck).resolve() if not Path(args.deck).is_absolute() else Path(args.deck)
    trang = deck / "index.html"
    if not trang.exists():
        sys.exit(f"Không thấy {trang}")

    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(trang.as_uri())
        await page.wait_for_timeout(400)

        ten = await page.evaluate(
            "() => (typeof bgmPresets === 'undefined') ? [] : Object.keys(bgmPresets)")
        if not ten:
            await browser.close()
            sys.exit("Trang không đọc được bgmPresets — sai deck?")
        chon = [args.preset] if args.preset else ten
        thieu = [p for p in chon if p not in ten]
        if thieu:
            await browser.close()
            sys.exit(f"Không có preset: {thieu}. Có: {ten}")

        print(f"bgmPresets đọc từ {deck.name}: {ten}")
        for p in chon:
            r = await dung_mot(page, p)
            print(f"  {p:10s} → {r['file'].name}  {r['giay']:.1f}s · {r['kb']} KB · "
                  f"{r['hop_am']} hợp âm + {r['arp']} arp · thô: đỉnh {r['dinh_goc']:.3f} "
                  f"LUFS {r['lufs0']:.1f} → nâng {r['nang']:+.1f} dB → {r['lufs']:.1f} LUFS · đỉnh thật {r['dinh_that']:.1f} dBTP")
        await browser.close()
    print(f"\nXong. File nằm ở {NHAC}")
    print('Dùng: đặt "bgm": {"mode": "preset", "preset": "<tên>"} trong preview-settings.json')


if __name__ == "__main__":
    asyncio.run(amain())
