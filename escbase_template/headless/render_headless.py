#!/usr/bin/env python3
"""Render headless TẤT ĐỊNH cho deck escbase (nhánh thợ 2).

Trị dứt giật 2-3s đầu của dây chuyền quay real-time: mở deck trong Chromium
headless, lái thời gian ẢO bằng window.renderAt(t), chụp CDP JPEG từng khung,
pipe thẳng vào ffmpeg, rồi trộn audio OFFLINE. Xem headless/KE_HOACH.md.

    render_headless.py <deck_dir> [--fps 30] [--dsf 2.769230769230769]
                       [--size 390x693] [--doan GIÂY] [--bgm-vol 0.12]

--doan N: chỉ render N giây đầu (để thử nhanh, KHÔNG render cả bài trong phiên phụ).

LUẬT: chỉ ĐỌC dây chuyền cũ. Import auto_render cho timeline/CSS/subtitle để
khớp tuyệt đối pipeline đã duyệt. Mọi thứ ghi ra nằm trong <deck_dir>/output_headless/.
"""

import argparse
import asyncio
import base64
import json
import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ESC_ROOT = HERE.parent  # escbase_template/
sys.path.insert(0, str(ESC_ROOT))

import auto_render as ar  # noqa: E402  (chỉ đọc/gọi, không sửa)

FPS_DEFAULT = 30
DSF_DEFAULT = 2.769230769230769  # 390*dsf ≈ 1080, 693*dsf ≈ 1919 (pad -> 1920)
FINAL_W, FINAL_H = 1080, 1920
TARGET_MEAN_DB = -17.0  # mức tiếng của bộ BOSS đã duyệt (03→10)
REVEAL_DUR = 0.72
SLIDE_DUR = 0.50
FIRST_REVEAL_OFFSET = 0.42  # goToSlide auto-reveal elem0 sau 420ms (khớp bản gốc)


# ─────────────────────────── đo & timeline ───────────────────────────

async def decoded_voice_duration(mp3: Path) -> float:
    """Đo thời lượng THẬT của voiceover bằng số sample giải mã (KE_HOACH §5:
    header MP3 có encoder delay, đừng tin — đếm sample mới chuẩn)."""
    proc = await asyncio.create_subprocess_exec(
        "ffmpeg", "-v", "error", "-i", str(mp3),
        "-f", "s16le", "-ac", "1", "-ar", "48000", "-",
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
    )
    out, err = await proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg decode voiceover fail: {err.decode('utf-8','ignore')[-500:]}")
    return (len(out) // 2) / 48000.0


def quantize(t: float, fps: int) -> float:
    """Lượng tử mốc sự kiện về biên khung: eventFrame = ceil(t*fps) (Codex §2)."""
    return math.ceil(round(t * fps, 6)) / fps


def clicks_to_events(clicks: list[dict], fps: int,
                     base_units: list[int] | None = None,
                     modes: list[str] | None = None) -> list[dict]:
    """Chuyển click-timeline (dây chuyền cũ) -> sự kiện ngữ nghĩa cho renderAt.

    reveal: {t, kind:'reveal', slide, elem}   slide: {t, kind:'slide', slide}
    elem0 của slide>=1 do 'slide' tự lộ sau FIRST_REVEAL_OFFSET; elem0 slide0 do 'start'.

    base_units/modes: slide `data-mode="highlight"`/`traffic-light` có thêm nhịp
    TÔ SÁNG `.highlightable` / BẬT ĐÈN `.lightable` SAU khi hết `.slide-element`
    (đường cũ: app.js:2226-2246). Chỉ số reveal vượt quá số `.slide-element` ⇒
    đổi thành sự kiện 'highlight'/'light'. Thiếu bước này thì vừa mất nhịp vừa
    LỆCH CẢ TIMELINE của slide đó (vì num_actions vào build_click_timeline sai).
    """
    events: list[dict] = []
    active = 0
    for c in clicks:
        desc = c.get("desc", "")
        t = float(c["time"])
        if desc == "Start presentation":
            active = 0
            events.append({"t": quantize(0.0, fps), "kind": "reveal", "slide": 0, "elem": 0})
        elif "transition" in desc:
            m = re.search(r"→\s*(\d+)", desc)
            active = (int(m.group(1)) - 1) if m else active + 1
            events.append({"t": quantize(t, fps), "kind": "slide", "slide": active})
            events.append({"t": quantize(t + FIRST_REVEAL_OFFSET, fps),
                           "kind": "reveal", "slide": active, "elem": 0})
        elif "reveal" in desc:
            ms = re.search(r"Slide\s*(\d+):\s*reveal\s*(\d+)/", desc)
            if ms:
                slide = int(ms.group(1)) - 1
                elem = int(ms.group(2)) - 1
                nbase = base_units[slide] if base_units and slide < len(base_units) else None
                mode = modes[slide] if modes and slide < len(modes) else ""
                if nbase is not None and elem >= nbase:
                    kind = "highlight" if mode == "highlight" else "light"
                    events.append({"t": quantize(t, fps), "kind": kind,
                                   "slide": slide, "idx": elem - nbase})
                else:
                    events.append({"t": quantize(t, fps), "kind": "reveal", "slide": slide, "elem": elem})
    events.sort(key=lambda e: (e["t"], 0 if e["kind"] == "slide" else 1))
    return events


# ─────────────────────────── recording HTML ───────────────────────────

def build_recording_html(deck: Path, out_dir: Path, render_size: tuple[int, int],
                         preview_settings: dict, subtitle_captions: list) -> Path:
    """Dựng bản _recording_headless.html RIÊNG (tham khảo prepare_recording_html
    của auto_render nhưng thêm cờ __HEADLESS_RENDER__ + hook phụ đề seek được).

    render_size = khổ NATIVE (vd 1080x1919). build_recording_css dùng
    RENDER_ZOOM = render_w/390 để zoom khối 390px lên khổ native (dsf=1) —
    NHANH GẤP ~6 LẦN chụp dsf+clip mà độ nét y hệt (đo 24/07)."""
    w, h = render_size
    ar.configure_render_geometry(w, h)  # -> RENDER_ZOOM = w/390 (=2.769) cho build_recording_css
    html = (deck / "index.html").read_text(encoding="utf-8")
    base_tag = f'<base href="{deck.as_uri()}/" />'
    settings_payload = json.dumps(preview_settings or {}, ensure_ascii=False).replace("</", "<\\/")

    head_inject = (
        f"{base_tag}\n"
        "<script>window.__RENDER_MODE__ = true; window.__HEADLESS_RENDER__ = true;"
        f" window.__PREVIEW_SETTINGS__ = {settings_payload}; window.__VT_MS__ = 0;</script>\n"
        f"<style>{ar.build_recording_css()}</style>\n"
        f"<style>{ar.SUBTITLE_CSS}</style>\n"
    )
    # biến CSS phụ đề theo preview-settings (fontSize/bottom/màu...)
    sub_css = ar.subtitle_css_from_settings(preview_settings or {})
    if sub_css:
        head_inject += f"<style>{sub_css}</style>\n"
    html = html.replace("<head>", "<head>\n" + head_inject, 1)

    # Phụ đề: dùng captions dựng sẵn, PHƠI render(time) ra global để renderAt lái.
    if subtitle_captions:
        sub_data = {"captions": subtitle_captions}
        payload = json.dumps(sub_data, ensure_ascii=False).replace("</", "<\\/")
        sub_script = ar.SUBTITLE_SCRIPT.replace(
            "window.__startScriptSubtitles = () => {",
            "window.__renderSubtitleAt = render;\n  window.__startScriptSubtitles = () => {",
            1,
        )
        html = html.replace(
            "</body>",
            f"<script>window.__SCRIPT_SUBTITLE_DATA__ = {payload};</script>\n"
            f"<script>{sub_script}</script>\n</body>",
            1,
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    rec = out_dir / "_recording_headless.html"
    rec.write_text(html, encoding="utf-8")
    return rec


# ─────────────────────────── ffmpeg helpers ───────────────────────────

def silent_encode_cmd(fps: int, out: Path) -> list[str]:
    # setparams cuối chuỗi: ffmpeg 8.1.2 BỎ QUA -color_primaries/-color_trc ở dòng
    # lệnh khi filter đã gán thuộc tính khung ⇒ video ra color_transfer=unknown
    # (bản cũ có bt709 đủ bộ). Đo lại bằng ffprobe -show_entries stream=color_transfer.
    vf = (
        f"pad={FINAL_W}:{FINAL_H}:(ow-iw)/2:(oh-ih)/2:black,"
        "scale=in_range=full:out_range=tv,setsar=1,format=yuv420p,"
        "setparams=range=tv:color_primaries=bt709:color_trc=bt709:colorspace=bt709"
    )
    return [
        "ffmpeg", "-y",
        "-f", "image2pipe", "-framerate", str(fps), "-vcodec", "mjpeg", "-i", "pipe:0",
        "-vf", vf,
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-profile:v", "high", "-level", "4.1",
        "-pix_fmt", "yuv420p",
        "-color_range", "tv", "-colorspace", "bt709",
        "-color_primaries", "bt709", "-color_trc", "bt709",
        "-r", str(fps), "-g", str(fps * 2), "-keyint_min", str(fps),
        "-movflags", "+faststart",
        str(out),
    ]


async def build_sfx_bed(page, events: list[dict], T: float, out: Path) -> int:
    """Dựng 1 file WAV chứa TOÀN BỘ tiếng chuyển slide + tiếng reveal, đặt đúng
    mốc timeline. Tiếng do chính template tổng hợp (transitionLib/revealLib chạy
    trong OfflineAudioContext — xem window.__renderSfxOffline trong app.js), nên
    KHÔNG chép tay, deck đổi lựa chọn tiếng trong preview-settings là tự theo.

    Trả về số tiếng đã đặt. Không có tiếng nào -> ghi file im lặng.
    """
    import numpy as np
    import wave

    SR = 48000
    keys = await page.evaluate(
        "() => ({tr: (typeof slideTransitions !== 'undefined' ? slideTransitions : []),"
        "        rv: (typeof slideReveals !== 'undefined' ? slideReveals : [])})"
    )
    tr_keys, rv_keys = keys.get("tr") or [], keys.get("rv") or []

    def key_for(ev: dict) -> tuple[str, str] | None:
        s = ev["slide"]
        if ev["kind"] == "slide":
            return ("slide", tr_keys[s]) if s < len(tr_keys) else None
        return ("reveal", rv_keys[s]) if s < len(rv_keys) else None

    # Lúc BẮT ĐẦU bài, bản gốc phát CẢ tiếng chuyển slide 0 lẫn tiếng reveal
    # (app.js:2209 playSlideSound(0) + 2215 playRevealSound).
    placements: list[tuple[float, tuple[str, str]]] = []
    if tr_keys:
        placements.append((0.0, ("slide", tr_keys[0])))
    for ev in events:
        k = key_for(ev)
        if k:
            placements.append((float(ev["t"]), k))

    clips: dict[tuple[str, str], "np.ndarray"] = {}
    for k in {p[1] for p in placements}:
        b64 = await page.evaluate(
            "([kind, name]) => window.__renderSfxOffline(kind, name)", [k[0], k[1]]
        )
        if not b64:
            continue
        pcm = np.frombuffer(base64.b64decode(b64), dtype="<i2").astype(np.float32) / 32768.0
        nz = np.nonzero(np.abs(pcm) > 1e-5)[0]
        clips[k] = pcm[: int(nz[-1]) + 1] if len(nz) else pcm[:1]

    bed = np.zeros(int(math.ceil((T + 3.0) * SR)), dtype=np.float32)
    placed = 0
    for t0, k in placements:
        clip = clips.get(k)
        if clip is None:
            continue
        off = int(round(t0 * SR))
        end = min(len(bed), off + len(clip))
        if end > off:
            bed[off:end] += clip[: end - off]
            placed += 1

    np.clip(bed, -1.0, 1.0, out=bed)
    with wave.open(str(out), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((bed * 32767.0).astype("<i2").tobytes())
    return placed


async def measure_levels(path: Path) -> tuple[float, float]:
    """Đọc mean/max dB bằng volumedetect (0 API). Trả (mean_db, max_db)."""
    proc = await asyncio.create_subprocess_exec(
        "ffmpeg", "-i", str(path), "-af", "volumedetect", "-f", "null", "-",
        stdout=asyncio.subprocess.DEVNULL, stderr=asyncio.subprocess.PIPE,
    )
    _, err = await proc.communicate()
    txt = err.decode("utf-8", "ignore")
    mean = float(re.search(r"mean_volume:\s*(-?[\d.]+) dB", txt).group(1))
    mx = float(re.search(r"max_volume:\s*(-?[\d.]+) dB", txt).group(1))
    return mean, mx


async def mix_audio(voice: Path, bgm: Path | None, out: Path, T: float, bgm_vol: float,
                    gain_db: float = 0.0, sfx: Path | None = None) -> None:
    """gain_db: nâng ĐỀU cả bản trộn (giữ nguyên tỉ lệ giọng/nhạc) trước limiter.
    Bơm sau khi đo lượt 1 để chạm đích TARGET_MEAN_DB — xem render().
    sfx: bed tiếng chuyển slide + reveal do build_sfx_bed dựng (có thể None).
    bgm: None = bài không có nhạc nền (preview-settings bgm.mode = "none").

    Nhạc nền lên dần trong 4 GIÂY đúng như bản gốc (app.js:2057
    linearRampToValueAtTime(bgm.volume, currentTime + 4)), không phải 0,4s."""
    fade_out_st = max(0.0, T - 0.8)
    fade_in_d = min(4.0, max(0.5, T / 4))
    fc = (
        f"[0:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
        f"asetpts=PTS-STARTPTS,apad,atrim=0:{T:.6f},volume=1.0[voice];"
    )
    inputs = ["-i", str(voice)]
    mix_labels = "[voice]"
    n_mix = 1
    if bgm is not None:
        inputs += ["-stream_loop", "-1", "-i", str(bgm)]
        fc += (
            f"[{n_mix}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
            f"asetpts=PTS-STARTPTS,atrim=0:{T:.6f},"
            f"afade=t=in:st=0:d={fade_in_d:.3f},afade=t=out:st={fade_out_st:.6f}:d=0.8,"
            f"volume={bgm_vol:.4f}[bg];"
        )
        mix_labels += "[bg]"
        n_mix += 1
    if sfx is not None:
        inputs += ["-i", str(sfx)]
        fc += (
            f"[{n_mix}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,"
            f"asetpts=PTS-STARTPTS,apad,atrim=0:{T:.6f},volume=1.0[sfx];"
        )
        mix_labels += "[sfx]"
        n_mix += 1
    fc += (
        f"{mix_labels}amix=inputs={n_mix}:duration=longest:dropout_transition=0:normalize=0,"
        f"volume={gain_db:.3f}dB,"
        f"alimiter=limit=0.95,apad,atrim=0:{T:.6f},asetpts=PTS-STARTPTS[aout]"
    )
    cmd = [
        "ffmpeg", "-y", *inputs,
        "-filter_complex", fc,
        "-map", "[aout]", "-c:a", "pcm_s16le", str(out),
    ]
    proc = await asyncio.create_subprocess_exec(
        *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    _, err = await proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError(f"mix_audio fail: {err.decode('utf-8','ignore')[-800:]}")


async def mux(silent: Path, audio: Path, out: Path, T: float) -> None:
    cmd = [
        "ffmpeg", "-y",
        "-i", str(silent), "-i", str(audio),
        "-map", "0:v:0", "-map", "1:a:0",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-ar", "48000",
        "-t", f"{T:.6f}", "-movflags", "+faststart", str(out),
    ]
    proc = await asyncio.create_subprocess_exec(
        *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    _, err = await proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError(f"mux fail: {err.decode('utf-8','ignore')[-800:]}")


# ─────────────────────────── render loop ───────────────────────────

def resolve_bgm(deck: Path, preview_settings: dict) -> tuple[Path | None, str]:
    """Chọn file nhạc nền theo preview-settings.json thay vì ghi cứng meta.mp3.

    Trước 25/07 hàm này không tồn tại: nhánh headless ghi cứng
    `preview-assets/bgm/meta.mp3` ⇒ CẢ DỰ ÁN dùng chung đúng 1 bản nhạc 60 giây
    dù template có sẵn cơ chế chọn nhạc. Đọc đúng 3 chế độ của template:
      custom → bgm.custom.path (tương đối so với deck)
      preset → nhac/synth_<preset>.wav dựng sẵn bằng dung_nhac_synth.py
      none   → không nhạc
    Thiếu/sai đường dẫn thì QUAY VỀ meta.mp3 + in cảnh báo, để mọi deck cũ
    render lại vẫn ra y hệt bản BOSS đã duyệt.
    """
    fallback = deck / "preview-assets" / "bgm" / "meta.mp3"
    bgm_cfg = preview_settings.get("bgm") or {}
    mode = bgm_cfg.get("mode", "custom")

    if mode == "none":
        return None, "nhạc nền: TẮT (bgm.mode=none)"

    if mode == "preset":
        preset = bgm_cfg.get("preset", "ambient")
        cand = ESC_ROOT / "nhac" / f"synth_{preset}.wav"
        if cand.exists():
            return cand, f"nhạc nền: preset synth '{preset}' ({cand.name})"
        print(f"[cảnh báo] thiếu {cand} — chạy dung_nhac_synth.py để dựng. Quay về meta.mp3")
        return (fallback if fallback.exists() else None), "nhạc nền: meta.mp3 (dự phòng)"

    rel = (bgm_cfg.get("custom") or {}).get("path") or (bgm_cfg.get("custom") or {}).get("url")
    if rel:
        cand = (deck / rel).resolve()
        if cand.exists():
            return cand, f"nhạc nền: {cand.name}"
        print(f"[cảnh báo] preview-settings trỏ '{rel}' nhưng không có file. Quay về meta.mp3")
    if not fallback.exists():
        print("[cảnh báo] deck không có nhạc nền nào — render KHÔNG nhạc")
        return None, "nhạc nền: KHÔNG CÓ"
    return fallback, "nhạc nền: meta.mp3"


async def render(deck: Path, fps: int, dsf: float, size: tuple[int, int],
                 doan: float | None, bgm_vol: float, use_gpu: bool = True) -> dict:
    from playwright.async_api import async_playwright

    out_dir = deck / "output_headless"
    out_dir.mkdir(parents=True, exist_ok=True)
    timing_data = json.loads((deck / "output" / "timing.json").read_text("utf-8"))
    voice = deck / "output" / "voiceover_concat.mp3"
    preview_settings = {}
    ps = deck / "preview-settings.json"
    if ps.exists():
        preview_settings = json.loads(ps.read_text("utf-8"))
    bgm, bgm_note = resolve_bgm(deck, preview_settings)
    print(bgm_note)
    # PHỤ ĐỀ: phải TỰ DỰNG như dây chuyền cũ (auto_render.py:1394-1401), không
    # được chỉ đọc cache. Deck đã render bằng nhánh cũ thì sẵn cache nên lỗi này
    # ẩn; deck MỚI toanh sẽ ra video KHÔNG CÓ PHỤ ĐỀ mà mọi phép đo khác vẫn PASS
    # (đã dính đúng bẫy này với deck superpowers 01 ngày 24/07).
    subtitle_captions = []
    subs_cfg = preview_settings.get("subtitles") or {}
    if subs_cfg.get("enabled", True) is not False:
        max_lines = int(subs_cfg.get("maxLines", 2) or 2)
        try:
            subtitle_data = ar.build_karaoke_subtitle_timing(
                deck / "output", timing_data, max_lines=max_lines)
            print("phụ đề: karaoke theo từng chữ")
        except Exception as exc:
            subtitle_data = ar.build_script_subtitle_timing(timing_data, max_lines=max_lines)
            print(f"phụ đề: karaoke hỏng ({exc.__class__.__name__}), quay về caption tĩnh")
        subtitle_captions = (subtitle_data or {}).get("captions", [])

    # Tỉ lệ nhạc nền: NGUỒN CHÂN LÝ là preview-settings (bản gốc đặt gain đúng
    # số này trong WebAudio — app.js:2057). Đặt tay khác đi là đổi tương quan
    # nhạc/giọng so với bộ BOSS đã duyệt.
    if bgm_vol is None:
        bgm_vol = float((preview_settings.get("bgm") or {}).get("volume", 0.30))

    D = await decoded_voice_duration(voice)
    N_full = math.ceil(D * fps)
    N = N_full if doan is None else min(N_full, math.ceil(doan * fps))
    T = N / fps

    # Khổ NATIVE = size × dsf (390*2.769≈1080, 693*2.769≈1919), render bằng CSS
    # zoom ở dsf=1 (nhanh) rồi pad -> 1080x1920 ở bước encode.
    render_w = int(round(size[0] * dsf))
    render_h = int(round(size[1] * dsf))
    rec = build_recording_html(deck, out_dir, (render_w, render_h), preview_settings, subtitle_captions)

    async with async_playwright() as pw:
        # --use-angle=default: bật ANGLE GPU trong headless → chụp NHANH GẤP ~6 LẦN
        # trên máy này (50ms vs 313ms/khung raster phần mềm). Đo 24/07.
        # Đánh đổi: chữ đang FADE (reveal) có vi sai khử răng cưa ±1 giữa 2 lần render
        # ~1.5s đầu (dưới ngưỡng mắt thấy, hội tụ khi chữ đứng yên). Cần khung TRÙNG
        # bit tuyệt đối thì --no-gpu (raster phần mềm, chậm hơn ~2.5x).
        gpu_args = (["--enable-gpu", "--ignore-gpu-blocklist", "--use-angle=default"]
                    if use_gpu else ["--disable-gpu"])
        browser = await ar.launch_chromium(
            pw, ["--allow-file-access-from-files"] + gpu_args, headless=True,
        )
        page = await browser.new_page(
            viewport={"width": render_w, "height": render_h},
            device_scale_factor=1,
        )
        try:
            await page.emulate_media(reduced_motion="no-preference")
        except Exception:
            pass
        await page.goto(rec.as_uri(), wait_until="load")

        # Đếm reveal_units GIỐNG HỆT dây chuyền cũ (auto_render.py:936-943):
        # .slide-element + .highlightable (mode highlight) + .lightable (traffic-light).
        counted = await page.evaluate(
            """() => Array.from(document.querySelectorAll('.slide')).map(s => {
                 const base = s.querySelectorAll('.slide-element').length;
                 const mode = s.dataset.mode || '';
                 let extra = 0;
                 if (mode === 'highlight') extra = s.querySelectorAll('.highlightable').length;
                 if (mode === 'traffic-light') extra = s.querySelectorAll('.lightable').length;
                 return {base, extra, mode};
               })"""
        )
        base_units = [int(c["base"]) for c in counted]
        modes = [c["mode"] for c in counted]
        reveal_units = [int(c["base"]) + int(c["extra"]) for c in counted]
        clicks = ar.build_click_timeline(timing_data, reveal_units)
        events = clicks_to_events(clicks, fps, base_units, modes)

        await page.evaluate("(ev) => { window.__RENDER_TIMELINE__ = ev; }", events)
        await page.evaluate("() => document.fonts.ready.then(() => true)")
        await page.evaluate("() => { if (window.__headlessBuild) window.__headlessBuild(); }")
        await page.wait_for_timeout(150)  # layout/canvas settle

        # SFX dựng TRƯỚC vòng chụp (dùng OfflineAudioContext của chính trang).
        sfx_path = out_dir / "sfx_bed.wav"
        try:
            n_sfx = await build_sfx_bed(page, events, T, sfx_path)
        except Exception as e:                      # thiếu SFX vẫn render được
            print(f"[cảnh báo] không dựng được SFX: {e}")
            n_sfx, sfx_path = 0, None
        if n_sfx == 0:
            sfx_path = None

        cdp = await page.context.new_cdp_session(page)
        # Viewport đã = khổ native (zoom, dsf=1) nên chụp thẳng, KHÔNG clip.scale
        # (clip.scale ép raster 2 lần, chậm gấp ~6). Ra đúng render_w×render_h.

        silent = out_dir / "silent.mp4"
        proc = await asyncio.create_subprocess_exec(
            *silent_encode_cmd(fps, silent),
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.PIPE,
        )
        err_tail: list[bytes] = []

        async def drain_err():
            # ĐỌC THEO KHỐI, KHÔNG readline(). ffmpeg in tiến độ bằng '\r' chứ
            # không '\n' ⇒ cả lượt encode dồn thành MỘT "dòng"; StreamReader có
            # trần 64 KiB/dòng nên readline() ném LimitOverrunError và giết cả
            # lượt render NGAY SAU KHI đã chụp đủ khung (silent.mp4 nhìn đầy đủ,
            # nhưng chưa kịp trộn tiếng ⇒ không có video cuối). Đã dính 25/07.
            while True:
                khoi = await proc.stderr.read(65536)
                if not khoi:
                    break
                err_tail.append(khoi)
                if len(err_tail) > 8:
                    err_tail.pop(0)
        err_task = asyncio.create_task(drain_err())

        step_ms = 1000.0 / fps
        written = 0
        cap_w = cap_h = 0
        for i in range(N):
            t_ms = i * step_ms
            # renderAt + chờ 1 rAF (chống chụp surface cũ) trong 1 round-trip
            await page.evaluate(
                "(t) => { window.renderAt(t); return new Promise(r => requestAnimationFrame(r)); }",
                t_ms,
            )
            res = await cdp.send("Page.captureScreenshot", {
                "format": "jpeg", "quality": 95,
                "optimizeForSpeed": True, "fromSurface": True,
                "captureBeyondViewport": False,
            })
            data = base64.b64decode(res["data"])
            if i == 0:
                try:
                    import io as _io
                    from PIL import Image as _Img
                    cap_w, cap_h = _Img.open(_io.BytesIO(data)).size
                except Exception:
                    cap_w, cap_h = 0, 0
            proc.stdin.write(data)
            await proc.stdin.drain()  # tôn trọng backpressure (tránh EPIPE ~frame 2500)
            written += 1

        proc.stdin.close()
        await proc.wait()
        await err_task
        if proc.returncode != 0:
            raise RuntimeError("silent encode fail:\n" + b"".join(err_tail).decode("utf-8", "ignore"))
        await browser.close()

    # audio offline + mux
    mixed = out_dir / "mixed.wav"
    suffix = "" if doan is None else f"_doan{int(round(doan))}s"
    final = out_dir / f"final_headless{suffix}.mp4"

    # Lượt 1 trộn ở mức gốc rồi ĐO, lượt 2 nâng đúng hệ số để chạm mean đích
    # (bộ BOSS đã duyệt ~-17 dB; bản trộn gốc của nhánh này ra -22,8 dB).
    await mix_audio(voice, bgm, mixed, T, bgm_vol, sfx=sfx_path)
    mean0, max0 = await measure_levels(mixed)
    gain = TARGET_MEAN_DB - mean0
    await mix_audio(voice, bgm, mixed, T, bgm_vol, gain_db=gain, sfx=sfx_path)
    mean1, max1 = await measure_levels(mixed)
    await mux(silent, mixed, final, T)

    return {
        "final": final, "silent": silent, "D": D, "N": N, "T": T,
        "written": written, "reveal_units": reveal_units,
        "events": len(events), "cap": (cap_w, cap_h),
        "audio": (mean0, max0, gain, mean1, max1),
        "sfx": n_sfx, "bgm_vol": bgm_vol, "bgm": bgm_note,
        "kinds": {k: sum(1 for e in events if e["kind"] == k)
                  for k in ("slide", "reveal", "highlight", "light")},
    }


async def amain() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("deck_dir")
    p.add_argument("--fps", type=int, default=FPS_DEFAULT)
    p.add_argument("--dsf", type=float, default=DSF_DEFAULT)
    p.add_argument("--size", default="390x693")
    p.add_argument("--doan", type=float, default=None, help="Chỉ render N giây đầu (thử nhanh)")
    p.add_argument("--bgm-vol", type=float, default=None,
                   help="Âm lượng nhạc nền; bỏ trống = lấy bgm.volume trong preview-settings.json")
    p.add_argument("--no-gpu", action="store_true",
                   help="Raster phần mềm: khung TRÙNG bit tuyệt đối nhưng chậm hơn ~2.5x")
    args = p.parse_args()

    deck = Path(args.deck_dir).resolve()
    if not (deck / "index.html").exists():
        sys.exit(f"Không thấy index.html trong {deck}")
    m = re.fullmatch(r"(\d+)x(\d+)", args.size)
    if not m:
        sys.exit("--size phải dạng WIDTHxHEIGHT, vd 390x693")
    size = (int(m.group(1)), int(m.group(2)))

    import time
    t0 = time.time()
    info = await render(deck, args.fps, args.dsf, size, args.doan, args.bgm_vol,
                        use_gpu=not args.no_gpu)
    dt = time.time() - t0

    print("=== render_headless XONG ===")
    print(f"voiceover D (sample-accurate): {info['D']:.4f}s")
    print(f"frames N={info['N']}  video T={info['T']:.4f}s  fps={args.fps}")
    print(f"reveal_units/slide: {info['reveal_units']}  (events={info['events']}: {info['kinds']})")
    print(f"SFX đặt: {info['sfx']} tiếng  ·  {info['bgm']}  ·  vol={info['bgm_vol']}")
    print(f"capture CSS size: {info['cap']}  (dsf={args.dsf} -> raster ~{int(size[0]*args.dsf)}x{int(size[1]*args.dsf)})")
    print(f"frames written: {info['written']}")
    m0, x0, g, m1, x1 = info["audio"]
    print(f"tiếng: trộn gốc mean {m0:.1f} dB / max {x0:.1f} dB  -> nâng {g:+.1f} dB "
          f"-> mean {m1:.1f} dB / max {x1:.1f} dB (đích {TARGET_MEAN_DB} dB)")
    print(f"thời gian render tường: {dt:.1f}s  ({dt/max(1,info['N'])*1000:.1f} ms/frame)")
    print(f"OUT: {info['final']}")



# ── KHOÁ RENDER (BOSS lệnh 25/07/2026) ──────────────────────────────────────
# Chỉ MỘT tiến trình quay/render một lúc. Đặt ở ĐÂY chứ không ở lam_bai.py, vì
# script này còn bị gọi TAY từ phiên khác. Lý do kỹ thuật + cách dùng: video/khoa_render.py
def _nap_khoa():
    import sys as _s
    from pathlib import Path as _P
    _d = _P(__file__).resolve()
    for _t in _d.parents:
        if (_t / "khoa_render.py").is_file():
            _s.path.insert(0, str(_t))
            from khoa_render import bao_roi_thoat
            return bao_roi_thoat
    return None


if __name__ == "__main__":
    _khoa = _nap_khoa()
    _cm = _khoa(f"render {' '.join(sys.argv[1:])[:60]}") if _khoa else None
    try:
        asyncio.run(amain())
    finally:
        if _cm:
            _cm.__exit__(None, None, None)
