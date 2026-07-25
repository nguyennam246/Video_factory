#!/usr/bin/env python3
"""BÀI THỬ PHÁT ÂM — sinh mp3 nhiều phương án đọc cho BOSS nghe rồi chọn.

    .venv/bin/python thu_phat_am.py <file_loi.txt> <ra.mp3>

Vì sao có file này (25/07/2026): BOSS nghe video PNJ rồi phán *"AI đọc chữ tiếng Anh
hay bị lỗi, như superpower, hoặc mã cổ phiếu PNJ đọc lỗi"* và **"làm file âm thanh cho
tôi duyệt trước rồi mới làm video"**.

🔴 LUẬT SỐNG CÒN: **AI KHÔNG NGHE ĐƯỢC.** Script này CHỈ sinh file. Nó không biết, và
không được phép đoán, phương án nào nghe hay. Mọi phán xét là của BOSS. Cấm viết
"phương án B nghe tự nhiên hơn" — đó là bịa.

Giọng khoá cứng theo chuẩn đã chốt (BOSS duyệt 2 vòng 20 giọng, và bác ElevenLabs
24/07): edge `vi-VN-NamMinhNeural` `+14%`. Đổi giọng ở đây là làm hỏng phép so —
bài thử phải nghe ĐÚNG giọng sẽ dùng thật.

Định dạng file lời: mỗi dòng 1 câu đọc, dòng trống bị bỏ qua, dòng bắt đầu bằng `#`
là ghi chú cho người đọc (không đọc lên).
"""
import asyncio
import subprocess
import sys
import tempfile
from pathlib import Path

import edge_tts

GIONG = "vi-VN-NamMinhNeural"
TOC_DO = "+14%"
NGHI = 0.55          # giây im lặng chèn giữa các câu, để BOSS tách được từng phương án


async def doc_mot_cau(text: str, ra: Path):
    await edge_tts.Communicate(text, GIONG, rate=TOC_DO).save(str(ra))


async def lam(file_loi: Path, ra: Path):
    dong = [d.strip() for d in file_loi.read_text(encoding="utf-8").splitlines()]
    cau = [d for d in dong if d and not d.startswith("#")]
    if not cau:
        sys.exit(f"❌ {file_loi} không có câu nào để đọc")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        # một file im lặng dùng lại cho mọi chỗ nghỉ
        im = tmp / "im.mp3"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "lavfi", "-i",
                        "anullsrc=r=24000:cl=mono", "-t", str(NGHI), "-q:a", "9", str(im)],
                       check=True)
        manh = []
        for i, c in enumerate(cau):
            f = tmp / f"c{i:02d}.mp3"
            await doc_mot_cau(c, f)
            print(f"  {i + 1:2d}/{len(cau)}  {c[:72]}")
            manh += [f, im]

        ds = tmp / "ds.txt"
        ds.write_text("".join(f"file '{p}'\n" for p in manh), encoding="utf-8")
        ra.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat",
                        "-safe", "0", "-i", str(ds), "-c", "copy", str(ra)], check=True)

    giay = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                           "-of", "csv=p=0", str(ra)], capture_output=True, text=True).stdout.strip()
    print(f"\n✅ {ra}  ({len(cau)} câu · {float(giay):.1f}s · {ra.stat().st_size // 1024} KB)")
    print("🟡 BOSS nghe rồi chọn — máy không nghe được, không tự phán phương án nào.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    asyncio.run(lam(Path(sys.argv[1]), Path(sys.argv[2])))
