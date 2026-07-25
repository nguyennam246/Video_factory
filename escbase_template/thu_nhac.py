#!/usr/bin/env python3
"""Dựng BÀI THỬ NHẠC NỀN: cùng một đoạn video, đổi nhạc, để BOSS nghe rồi chốt.

VÌ SAO: AI KHÔNG NGHE ĐƯỢC (luật số 1 của dự án). Máy chỉ chứng minh được mức
tiếng đúng chuẩn; hay hay dở phải BOSS nghe. Nên cách làm đúng là dựng nhiều
phương án cho BOSS chọn — y như khuôn thử giọng `kichban/00*_thu_giong.md`.

RẺ: không render lại khung hình nào. Dùng lại nguyên liệu deck đã render:
  output_headless/silent.mp4   (video câm, đã có sẵn)
  output/voiceover_concat.mp3  (giọng)
  output_headless/sfx_bed.wav  (tiếng chuyển slide + reveal)
rồi chỉ trộn lại phần tiếng với từng bản nhạc. Mỗi phương án ~5 giây xử lý.

Mỗi bản đều đi qua ĐÚNG hàm mix_audio của render_headless (amix normalize=0 +
alimiter 0.95 + tự nâng để chạm mean -17 dB) ⇒ so sánh công bằng: chỉ khác NHẠC,
không khác cách trộn, không khác độ to tổng.

Chạy:
    .venv/bin/python thu_nhac.py                     # tất cả nhạc trong nhac/ + meta.mp3
    .venv/bin/python thu_nhac.py --giay 30           # đổi độ dài đoạn thử
    .venv/bin/python thu_nhac.py --deck headless/deck_msr01
Ra: results/video/thunhac_NN_<ten>.mp4
"""
from __future__ import annotations

import argparse
import asyncio
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE_DIR = HERE.parent.parent          # .../Cloud
RA = BASE_DIR / "results" / "video"
GIAY_MAC_DINH = 25.0

spec = importlib.util.spec_from_file_location("rh", HERE / "headless" / "render_headless.py")
rh = importlib.util.module_from_spec(spec)
sys.modules["rh"] = rh
spec.loader.exec_module(rh)


def gom_nhac(deck: Path) -> list[tuple[str, Path]]:
    """Danh sách phương án: nhạc đang dùng của deck + mọi file trong nhac/."""
    ds: list[tuple[str, Path]] = []
    hien = deck / "preview-assets" / "bgm" / "meta.mp3"
    if hien.exists():
        ds.append(("dangdung_meta", hien))
    kho = HERE / "nhac"
    if kho.exists():
        for f in sorted(kho.iterdir()):
            if f.suffix.lower() in (".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac"):
                ds.append((f.stem, f))
    return ds


async def mot_bai(deck: Path, ten: str, nhac: Path, stt: int, T: float,
                  bgm_vol: float, tam: Path) -> dict:
    voice = deck / "output" / "voiceover_concat.mp3"
    sfx = deck / "output_headless" / "sfx_bed.wav"
    silent = deck / "output_headless" / "silent.mp4"
    mixed = tam / f"mix_{stt:02d}.wav"
    ra = RA / f"thunhac_{stt:02d}_{ten}.mp4"

    # Hai lượt y như render_headless: trộn gốc → đo → nâng đúng hệ số về -17 dB.
    await rh.mix_audio(voice, nhac, mixed, T, bgm_vol, sfx=sfx if sfx.exists() else None)
    mean0, _ = await rh.measure_levels(mixed)
    gain = rh.TARGET_MEAN_DB - mean0
    await rh.mix_audio(voice, nhac, mixed, T, bgm_vol, gain_db=gain,
                       sfx=sfx if sfx.exists() else None)
    mean1, max1 = await rh.measure_levels(mixed)
    await rh.mux(silent, mixed, ra, T)
    mixed.unlink(missing_ok=True)
    return {"file": ra, "mean": mean1, "max": max1, "gain": gain,
            "mb": ra.stat().st_size / 1e6}


async def amain() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--deck", default="headless/deck_sp01")
    ap.add_argument("--giay", type=float, default=GIAY_MAC_DINH)
    ap.add_argument("--bgm-vol", type=float, default=None,
                    help="Bỏ trống = lấy bgm.volume của deck (mặc định 0.3)")
    args = ap.parse_args()

    deck = Path(args.deck)
    if not deck.is_absolute():
        deck = (HERE / deck).resolve()
    thieu = [p for p in ("output/voiceover_concat.mp3", "output_headless/silent.mp4")
             if not (deck / p).exists()]
    if thieu:
        sys.exit(f"Deck chưa render xong, thiếu: {thieu}\n"
                 f"Chạy headless/render_headless.py {deck} trước.")

    import json
    ps = deck / "preview-settings.json"
    bgm_vol = args.bgm_vol
    if bgm_vol is None:
        cfg = json.loads(ps.read_text("utf-8")) if ps.exists() else {}
        bgm_vol = float((cfg.get("bgm") or {}).get("volume", 0.30))

    ds = gom_nhac(deck)
    if not ds:
        sys.exit("Không có bản nhạc nào. Bỏ file vào nhac/ hoặc chạy dung_nhac_synth.py")

    RA.mkdir(parents=True, exist_ok=True)
    tam = deck / "output_headless"
    print(f"Deck: {deck.name} · đoạn {args.giay:g}s · bgm_vol={bgm_vol} · "
          f"{len(ds)} phương án\n")
    kq = []
    for i, (ten, nhac) in enumerate(ds, 1):
        r = await mot_bai(deck, ten, nhac, i, args.giay, bgm_vol, tam)
        kq.append((ten, r))
        print(f"  {i:02d}. {ten:22s} → {r['file'].name}  "
              f"mean {r['mean']:.1f} dB · max {r['max']:.1f} dB · {r['mb']:.1f} MB")

    print("\n=== BẢNG CHO BOSS NGHE ===")
    print(f"{'#':>2}  {'Phương án':22s}  File")
    for i, (ten, r) in enumerate(kq, 1):
        print(f"{i:2d}  {ten:22s}  results/video/{r['file'].name}")
    print("\n⚠️  Mọi bản đều đã chuẩn về mean ~-17 dB — khác nhau CHỈ ở bản nhạc.")
    print("    AI không nghe được: hay/dở do BOSS phán.")


if __name__ == "__main__":
    asyncio.run(amain())
