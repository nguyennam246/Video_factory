#!/usr/bin/env python3
"""LÀM VIDEO HƯỚNG DẪN từ file kịch bản — 0 đồng, không đăng ký tool nào.

Dây chuyền:  kịch bản .md  →  slide PNG (Pillow)  +  giọng đọc (Gemini TTS free)
             →  ghép từng cảnh (ffmpeg)  →  1 file .mp4 dọc 9:16.

Vì sao KHÔNG dùng tool sinh video trả tiền: nội dung là chữ kỹ thuật (tên lệnh,
tên file). Tool sinh video ghép cảnh stock + không kiểm soát được chữ trên màn
hình. Ở đây MỌI chữ là do kịch bản quy định, sai một ký tự cũng thấy được.

Chạy:
    .venv/bin/python scripts/lam_video.py tailieu/kichban_video/01_hooks.md
    .venv/bin/python scripts/lam_video.py <kịch bản> --canh 1-3   # render thử

Định dạng kịch bản: xem tailieu/kichban_video/README.md
"""
import argparse
import base64
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
import wave
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
KHO_TTS = BASE_DIR / "state" / "video_tts"
RA = BASE_DIR / "results" / "video"

# ---- khung hình dọc 9:16 cho điện thoại ----
W, H = 1080, 1920
LE = 80                      # lề trái/phải
VUNG_SLIDE = (280, 1440)     # y bắt đầu / kết thúc vùng chữ chính
NEN = (15, 20, 25)
MAU = {
    "thuong": (230, 237, 243),
    "nhan": (126, 231, 135),   # xanh — dòng nhấn
    "ma": (255, 166, 87),      # cam — lệnh / tên file
}
CO_CHU = {"thuong": 64, "nhan": 92, "ma": 50}
MAU_PHU = (139, 148, 158)

FONT_SANS = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
FONT_MONO = "/System/Library/Fonts/Menlo.ttc"

TTS_MODEL = "gemini-2.5-flash-preview-tts"   # đo 23/07: 5,8s/cảnh (3.1 mất 17,4s)
NHIP_LAY = 24000                             # Gemini trả PCM 16-bit mono 24kHz
IM_CUOI = 0.45                               # giây lặng thêm cuối mỗi cảnh


# ─────────────────────────── đọc kịch bản ───────────────────────────
def doc_kich_ban(duong: Path) -> tuple:
    tieu_de, giong, canh_list = duong.stem, "Kore", []
    nghi = IM_CUOI
    hien_tai = None
    for dong in duong.read_text(encoding="utf-8").splitlines():
        d = dong.rstrip()
        if d.startswith("TIÊU ĐỀ:"):
            tieu_de = d.split(":", 1)[1].strip()
        elif d.startswith("GIỌNG:") and hien_tai is None:
            giong = d.split(":", 1)[1].strip()          # giọng chung cả bài
        elif d.startswith("NGHỈ:") and hien_tai is None:
            # Giây lặng thêm sau mỗi cảnh. Bài DẠY cần nghỉ dài hơn truyện: giọng đọc
            # nhanh nhưng mắt vẫn phải kịp đọc tên lệnh trên màn hình.
            nghi = float(d.split(":", 1)[1].strip())
        elif d.strip() == "---":
            hien_tai = {"loi": "", "dong": [], "giong": None, "kieu": "", "tieng": ""}
            canh_list.append(hien_tai)
        elif hien_tai is None:
            continue
        elif d.startswith("GIỌNG:"):        # đổi giọng RIÊNG cảnh này (bài thử giọng)
            hien_tai["giong"] = d.split(":", 1)[1].strip()
        elif d.startswith("KIỂU:"):         # chỉ dẫn lối đọc, KHÔNG đọc ra, KHÔNG hiện
            hien_tai["kieu"] = d.split(":", 1)[1].strip()
        elif d.startswith("TIẾNG:"):        # file tiếng CÓ SẴN → bỏ qua mọi engine TTS
            hien_tai["tieng"] = d.split(":", 1)[1].strip()
        elif d.startswith("LỜI:"):
            hien_tai["loi"] = d.split(":", 1)[1].strip()
        elif d.startswith("CHỮ*:"):
            hien_tai["dong"].append(("nhan", d.split(":", 1)[1].strip()))
        elif d.startswith("CHỮ:"):
            hien_tai["dong"].append(("thuong", d.split(":", 1)[1].strip()))
        elif d.startswith("MÃ:"):
            hien_tai["dong"].append(("ma", d.split(":", 1)[1].strip()))
        elif d.strip() and hien_tai["loi"]:
            hien_tai["loi"] += " " + d.strip()   # dòng nối tiếp LỜI
    canh_list = [c for c in canh_list if c["loi"]]
    if not canh_list:
        sys.exit(f"❌ {duong} không có cảnh nào (thiếu `---` hoặc `LỜI:`)")
    return tieu_de, giong, canh_list, nghi


# ─────────────────────────── vẽ slide ───────────────────────────
def _font(kieu: str, co: int):
    from PIL import ImageFont

    if kieu == "ma":
        return ImageFont.truetype(FONT_MONO, co)
    return ImageFont.truetype(FONT_SANS, co)


def _rong(draw, text, font) -> int:
    return draw.textbbox((0, 0), text, font=font)[2]


def _ngat_dong(draw, text, font, rong_toi_da) -> list:
    tu, dong_ra, cur = text.split(), [], ""
    for t in tu:
        thu = f"{cur} {t}".strip()
        if _rong(draw, thu, font) <= rong_toi_da or not cur:
            cur = thu
        else:
            dong_ra.append(cur)
            cur = t
    if cur:
        dong_ra.append(cur)
    return dong_ra


def ve_slide(canh: dict, chi_so: int, tong: int, tieu_de: str, ra: Path) -> None:
    from PIL import Image, ImageDraw

    anh = Image.new("RGB", (W, H), NEN)
    d = ImageDraw.Draw(anh)
    rong_toi_da = W - 2 * LE

    # thanh tiến độ trên cùng — người xem biết còn bao nhiêu
    d.rectangle([0, 0, W, 8], fill=(35, 42, 51))
    d.rectangle([0, 0, int(W * chi_so / tong), 8], fill=MAU["nhan"])

    f_td = _font("thuong", 34)
    d.text((LE, 90), tieu_de.upper(), font=f_td, fill=MAU_PHU)
    f_st = _font("ma", 30)
    stt = f"{chi_so}/{tong}"
    d.text((W - LE - _rong(d, stt, f_st), 92), stt, font=f_st, fill=MAU_PHU)

    # ---- vùng chữ chính: thu nhỏ dần tới khi vừa cả bề ngang lẫn bề dọc ----
    cao_toi_da = VUNG_SLIDE[1] - VUNG_SLIDE[0]
    ty_le = 1.0
    while ty_le > 0.35:
        khoi = []
        for kieu, text in canh["dong"]:
            co = max(18, int(CO_CHU[kieu] * ty_le))
            if kieu == "ma":
                # Dòng lệnh KHÔNG được ngắt giữa chừng (`PreToolUse — TRƯỚC khi
                # dùng / tool` đọc thành 2 ý khác nhau) → tự thu cho vừa 1 dòng
                while co > 18 and _rong(d, text, _font(kieu, co)) > rong_toi_da:
                    co -= 2
                khoi.append((kieu, text, _font(kieu, co)))
                continue
            f = _font(kieu, co)
            for dl in _ngat_dong(d, text, f, rong_toi_da):
                khoi.append((kieu, dl, f))
        tong_cao = sum(int(f.size * 1.55) for _, _, f in khoi)
        if tong_cao <= cao_toi_da:
            break
        ty_le -= 0.05

    y = VUNG_SLIDE[0] + (cao_toi_da - sum(int(f.size * 1.55) for _, _, f in khoi)) // 2
    for kieu, text, f in khoi:
        d.text(((W - _rong(d, text, f)) // 2, y), text, font=f, fill=MAU[kieu])
        y += int(f.size * 1.55)

    # ---- phụ đề = chính lời đọc → tắt tiếng vẫn hiểu ----
    f_pd = _font("thuong", 38)
    dong_pd = _ngat_dong(d, canh["loi"], f_pd, rong_toi_da)[:5]
    y = H - 150 - len(dong_pd) * 54
    d.line([(LE, y - 46), (W - LE, y - 46)], fill=(35, 42, 51), width=3)
    for dl in dong_pd:
        d.text(((W - _rong(d, dl, f_pd)) // 2, y), dl, font=f_pd, fill=MAU_PHU)
        y += 54

    anh.save(ra)


# ─────────────────────────── giọng đọc ───────────────────────────
def _cac_key() -> list:
    keys = []
    for dong in (BASE_DIR / ".env").read_text().splitlines():
        d = dong.strip()
        if d.startswith("gemini_api_key") and "=" in d:
            keys.append(d.split("=", 1)[1].strip().strip('"').strip("'"))
    if not keys:
        sys.exit("❌ .env không có gemini_api_key")
    return keys


def _tts_edge(loi: str, giong: str) -> bytes:
    """Edge TTS (Microsoft) — giọng tiếng Việt BẢN ĐỊA, free, không cần key, không hạn mức.
    Khai giọng: `edge:vi-VN-NamMinhNeural` hoặc kèm tốc độ `edge:vi-VN-NamMinhNeural:-10%`.
    ⚠️ Đây là đường KHÔNG CHÍNH THỨC (dùng dịch vụ đọc-to của trình duyệt Edge) — chạy tốt
    nhiều năm nay nhưng Microsoft có thể đổi bất cứ lúc nào. Gemini TTS là đường dự phòng.
    """
    import asyncio

    import edge_tts

    phan = giong.split(":")
    ten = phan[1]
    toc_do = phan[2] if len(phan) > 2 else "+0%"
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        mp3 = f.name
    # Endpoint Edge CHẬP CHỜN: đo 23/07 — cùng một câu, lượt này `NoAudioReceived`,
    # lượt sau chạy ngon. Không phải sai tham số ⇒ cứ thử lại, đừng đi sửa tham số.
    for lan in range(4):
        try:
            asyncio.run(edge_tts.Communicate(loi, ten, rate=toc_do).save(mp3))
            if Path(mp3).stat().st_size > 0:
                break
        except Exception as e:  # noqa: BLE001
            if lan == 3:
                sys.exit(f"❌ Edge TTS trượt 4 lần: {type(e).__name__} — mạng hoặc "
                         f"Microsoft đổi endpoint. Đổi sang giọng Gemini để chạy tiếp.")
            print(f"      Edge TTS chập chờn (lần {lan + 1}/4) → thử lại")
            time.sleep(3 * (lan + 1))
    p = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", mp3, "-ar", str(NHIP_LAY), "-ac", "1",
         "-f", "s16le", "-"],
        capture_output=True,
    )
    Path(mp3).unlink(missing_ok=True)
    if p.returncode or not p.stdout:
        sys.exit(f"❌ đổi mp3→pcm hỏng: {p.stderr.decode()[:300]}")
    return p.stdout


def tieng_co_san(duong: str, ra: Path, nghi: float) -> float:
    """Dùng file tiếng BOSS tự làm (CapCut · ElevenLabs · Vbee · tự đọc bằng micro).
    Nhận mọi định dạng ffmpeg đọc được (.mp3 .m4a .wav .aac…), tự đổi về khuôn chung.
    Nhờ đường này mà dây chuyền KHÔNG phụ thuộc một nhà TTS nào.
    """
    f = Path(duong)
    if not f.is_absolute():
        f = BASE_DIR / duong
    if not f.exists():
        sys.exit(f"❌ không thấy file tiếng: {f}")
    p = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(f), "-ar", str(NHIP_LAY), "-ac", "1",
         "-f", "s16le", "-"], capture_output=True)
    if p.returncode or not p.stdout:
        sys.exit(f"❌ đọc file tiếng hỏng: {p.stderr.decode()[:300]}")
    raw = p.stdout + b"\x00\x00" * int(NHIP_LAY * nghi)
    with wave.open(str(ra), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(NHIP_LAY)
        w.writeframes(raw)
    return len(raw) / (NHIP_LAY * 2)


def tach_tieng(nguon: str, so_canh: int, thu_muc: Path) -> None:
    """Cắt MỘT file tiếng dài thành đúng `so_canh` mẩu, cắt tại các khoảng LẶNG dài nhất.

    Vì sao có hàm này: CapCut/ElevenLabs không có API. Xuất tay từng cảnh thì 13 lần bấm.
    Cách này chỉ cần **dán cả bài một lần, xuất một file**, rồi máy tự cắt ra từng cảnh.
    Điều kiện: khi dán vào CapCut phải để **mỗi cảnh một đoạn riêng** (xuống dòng trống)
    để nó nghỉ hơi giữa các cảnh — chỗ nghỉ đó chính là chỗ máy cắt.
    """
    p = subprocess.run(
        ["ffmpeg", "-v", "info", "-i", nguon, "-af",
         "silencedetect=noise=-35dB:d=0.30", "-f", "null", "-"],
        capture_output=True, text=True)
    lang = []
    dau_lang = None
    for d in p.stderr.splitlines():
        if "silence_start:" in d:
            dau_lang = float(d.split("silence_start:")[1].strip())
        elif "silence_end:" in d and dau_lang is not None:
            ket = float(d.split("silence_end:")[1].split("|")[0].strip())
            lang.append((ket - dau_lang, dau_lang, ket))
            dau_lang = None
    if len(lang) < so_canh - 1:
        sys.exit(f"❌ chỉ thấy {len(lang)} chỗ nghỉ, cần {so_canh - 1}. "
                 "Dán lại vào CapCut với MỖI CẢNH MỘT ĐOẠN (có dòng trống ngăn cách).")

    # lấy N-1 chỗ nghỉ DÀI NHẤT rồi xếp lại theo thời gian → ranh giới giữa các cảnh
    chon = sorted(sorted(lang, reverse=True)[: so_canh - 1], key=lambda x: x[1])
    moc = [0.0] + [(a + b) / 2 for _, a, b in chon]

    tong = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", nguon], capture_output=True, text=True).stdout.strip())
    moc.append(tong)

    thu_muc.mkdir(parents=True, exist_ok=True)
    for i in range(so_canh):
        ra = thu_muc / f"{i + 1:02d}.wav"
        ffmpeg(["-i", nguon, "-ss", f"{moc[i]:.3f}", "-to", f"{moc[i + 1]:.3f}",
                "-ar", str(NHIP_LAY), "-ac", "1", str(ra)])
        print(f"   ✓ cảnh {i + 1:2d}  {moc[i + 1] - moc[i]:5.1f}s  → {ra.name}")
    print(f"\n✅ cắt xong {so_canh} mẩu vào {thu_muc}\n"
          f"   Render: thêm  --tieng-thu-muc {thu_muc}")


def doc_tieng(loi: str, giong: str, keys: list, ra: Path, nghi: float) -> float:
    """Đọc lời → .wav. CACHE theo hash (lời + giọng) nên render lại không gọi API."""
    ma = hashlib.sha1(f"{giong}|{TTS_MODEL}|{nghi}|{loi}".encode()).hexdigest()[:16]
    cache = KHO_TTS / f"{ma}.wav"
    if not cache.exists() and giong.startswith("edge:"):
        raw = _tts_edge(loi, giong)
        raw += b"\x00\x00" * int(NHIP_LAY * nghi)
        with wave.open(str(cache), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(NHIP_LAY)
            w.writeframes(raw)
    if not cache.exists():
        body = json.dumps({
            "contents": [{"parts": [{"text": loi}]}],
            "generationConfig": {
                "responseModalities": ["AUDIO"],
                "speechConfig": {
                    "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": giong}}
                },
            },
        }).encode()
        raw = None
        for i, key in enumerate(keys):
            req = urllib.request.Request(
                f"https://generativelanguage.googleapis.com/v1beta/models/{TTS_MODEL}:generateContent",
                data=body,
                headers={"Content-Type": "application/json", "x-goog-api-key": key},
            )
            try:
                with urllib.request.urlopen(req, timeout=180) as r:
                    o = json.loads(r.read())
                raw = base64.b64decode(
                    o["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
                )
                break
            except Exception as e:
                ma_loi = getattr(e, "code", "")
                print(f"      key #{i + 1} lỗi {ma_loi or type(e).__name__} → đổi key")
                time.sleep(2)
        if raw is None:
            sys.exit("❌ cả 5 key đều trượt TTS — dừng, đừng ghi file hỏng")
        raw += b"\x00\x00" * int(NHIP_LAY * nghi)      # đệm lặng cuối cảnh
        with wave.open(str(cache), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(NHIP_LAY)
            w.writeframes(raw)
    shutil.copy(cache, ra)
    with wave.open(str(ra)) as w:
        return w.getnframes() / w.getframerate()


# ─────────────────────────── ghép ───────────────────────────
def ffmpeg(args: list) -> None:
    p = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args],
                       capture_output=True, text=True)
    if p.returncode:
        sys.exit(f"❌ ffmpeg: {p.stderr[:600]}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("kich_ban")
    ap.add_argument("--canh", help="render thử một khoảng, vd 1-3")
    ap.add_argument("--loi", action="store_true",
                    help="chỉ IN lời đọc từng cảnh để dán sang CapCut/Vbee, không render")
    ap.add_argument("--tach-tieng", metavar="FILE",
                    help="cắt 1 file tiếng dài (xuất từ CapCut) thành từng cảnh, không render")
    ap.add_argument("--tieng-thu-muc", metavar="DIR",
                    help="lấy tiếng từng cảnh ở thư mục này (01.wav, 02.wav…) thay cho TTS")
    args = ap.parse_args()

    duong = Path(args.kich_ban)
    if not duong.is_absolute():
        duong = BASE_DIR / duong
    tieu_de, giong, canh_list, nghi = doc_kich_ban(duong)

    if args.tach_tieng:
        print(f"✂️  cắt {args.tach_tieng} thành {len(canh_list)} cảnh…")
        tach_tieng(args.tach_tieng, len(canh_list),
                   BASE_DIR / "state" / "tieng_tach" / duong.stem)
        return

    if args.loi:
        # Cho BOSS dán sang tool GUI (CapCut/ElevenLabs) rồi xuất từng file tiếng,
        # đặt tên đúng số cảnh, khai lại bằng dòng `TIẾNG:` trong kịch bản.
        print(f"# {tieu_de} — {len(canh_list)} cảnh\n")
        for i, c in enumerate(canh_list, 1):
            print(f"[cảnh {i:02d}]  {c['loi']}\n")
        return

    dau, cuoi = 1, len(canh_list)
    if args.canh:
        m = re.match(r"(\d+)(?:-(\d+))?$", args.canh)
        dau = int(m.group(1))
        cuoi = int(m.group(2) or m.group(1))

    KHO_TTS.mkdir(parents=True, exist_ok=True)
    RA.mkdir(parents=True, exist_ok=True)
    tam = RA / f"_tam_{duong.stem}"
    shutil.rmtree(tam, ignore_errors=True)
    tam.mkdir()

    print(f"🎬 {tieu_de}  ·  giọng {giong}  ·  cảnh {dau}-{cuoi}/{len(canh_list)}")
    keys = _cac_key()
    tong_giay, doan = 0.0, []
    for i in range(dau, cuoi + 1):
        canh = canh_list[i - 1]
        png, wav, mp4 = tam / f"{i:02d}.png", tam / f"{i:02d}.wav", tam / f"{i:02d}.mp4"
        ve_slide(canh, i, len(canh_list), tieu_de, png)
        tu_ngoai = canh["tieng"]
        if args.tieng_thu_muc and not tu_ngoai:
            san = Path(args.tieng_thu_muc) / f"{i:02d}.wav"
            if not san.is_absolute():
                san = BASE_DIR / args.tieng_thu_muc / f"{i:02d}.wav"
            if san.exists():
                tu_ngoai = str(san)
        if tu_ngoai:
            giay = tieng_co_san(tu_ngoai, wav, nghi)
        else:
            # KIỂU đi vào lời nhờ TTS đọc theo lối đó — nó KHÔNG bị đọc thành tiếng
            loi_doc = f"{canh['kieu']}: {canh['loi']}" if canh["kieu"] else canh["loi"]
            giay = doc_tieng(loi_doc, canh["giong"] or giong, keys, wav, nghi)
        ffmpeg(["-loop", "1", "-i", str(png), "-i", str(wav),
                "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage",
                "-r", "30", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
                "-shortest", str(mp4)])
        doan.append(mp4)
        tong_giay += giay
        print(f"   ✓ cảnh {i:2d}  {giay:5.1f}s  {canh['loi'][:52]}…")

    ds = tam / "danh_sach.txt"
    ds.write_text("".join(f"file '{p.name}'\n" for p in doan), encoding="utf-8")
    ra_mp4 = RA / f"{duong.stem}.mp4"
    ffmpeg(["-f", "concat", "-safe", "0", "-i", str(ds), "-c", "copy", str(ra_mp4)])

    mb = ra_mp4.stat().st_size / 1e6
    print(f"\n✅ {ra_mp4.relative_to(BASE_DIR)}  ·  {tong_giay:.0f} giây  ·  {mb:.1f} MB  ·  {W}×{H}")


if __name__ == "__main__":
    main()
