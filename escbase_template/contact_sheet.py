#!/usr/bin/env python3
"""CONTACT SHEET — ghép các slide PNG thành 1 tấm để SOI BẰNG 1 LƯỢT ĐỌC ẢNH.

    .venv/bin/python contact_sheet.py deck_pnj02            # tên deck (tìm trong /tmp/escbase-qa)
    .venv/bin/python contact_sheet.py /tmp/escbase-qa/deck_pnj02   # hoặc đường dẫn thẳng
    .venv/bin/python contact_sheet.py deck_pnj02 --cot 5 --rong 460

Vì sao có file này (25/07/2026, BOSS hỏi "sao làm video tốn thời gian thế?"):
bước SOI ẢNH của dây chuyền bảo `Read` từng file slide1..slide10.png. Mỗi vòng vá lỗi
là 10 lượt đọc ảnh, mà một bài thường 2-3 vòng ⇒ 20-30 lượt. Ảnh là thứ đắt token nhất
trong cả dây chuyền, trong khi phần lớn lỗi (chữ tràn, hộp lệch, màu mâu thuẫn với
nghĩa, khoảng trống chết) NHÌN LƯỚT CẢ LOẠT là thấy — thấy rồi mới cần mở đúng slide
nghi ngờ ở cỡ thật.

Vòng soi mới: **LƯỚT 1 tấm → ZOOM slide đáng ngờ**. Đo thật bài PNJ 02: 2 lượt đọc ảnh
thay vì 20-30, vẫn bắt được lỗi nghĩa (`hk-lockup-a` đỏ bọc câu dạy nghề đứng vững).

KHÔNG thay thế bước soi ảnh — chỉ đổi THỨ TỰ. Bỏ soi là mất khâu bắt lỗi nghĩa duy nhất.
"""
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw

QA = Path("/tmp/escbase-qa")


def tim_thu_muc(dau_vao: str) -> Path:
    p = Path(dau_vao)
    if p.is_dir():
        return p
    p2 = QA / dau_vao
    if p2.is_dir():
        return p2
    sys.exit(f"❌ không thấy thư mục ảnh: {dau_vao} (cũng thử {p2})")


def ghep(dau_vao: str, cot: int = 5, rong: int = 460) -> Path:
    thu_muc = tim_thu_muc(dau_vao)
    # tự đếm số slide, đừng hardcode 10 — deck kỹ năng / deck thử có thể khác
    anh = sorted((p for p in thu_muc.glob("slide*.png")),
                 key=lambda p: int(re.search(r"(\d+)", p.stem).group(1)))
    if not anh:
        sys.exit(f"❌ không có slide*.png trong {thu_muc} — chạy capture_slides.py trước")

    mo = [Image.open(p).convert("RGB") for p in anh]
    w0, h0 = mo[0].size
    cao = round(rong * h0 / w0)
    cot = min(cot, len(mo))
    hang = -(-len(mo) // cot)
    le, nhan = 10, 26

    tam = Image.new("RGB", (cot * rong + (cot + 1) * le,
                            hang * (cao + nhan + le) + le), (12, 14, 18))
    ve = ImageDraw.Draw(tam)
    for i, im in enumerate(mo):
        r, c = divmod(i, cot)
        x = le + c * (rong + le)
        y = le + r * (cao + nhan + le)
        ve.text((x + 4, y + 5), anh[i].stem, fill=(255, 176, 32))
        tam.paste(im.resize((rong, cao), Image.LANCZOS), (x, y + nhan))

    ra = thu_muc / "_contact_sheet.png"
    tam.save(ra, optimize=True)
    print(f"✅ {ra}  ({tam.size[0]}x{tam.size[1]}, {ra.stat().st_size // 1024} KB, "
          f"{len(mo)} slide)")
    return ra


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(2)
    kw = {}
    for co, ten in (("--cot", "cot"), ("--rong", "rong")):
        if co in a:
            i = a.index(co)
            kw[ten] = int(a[i + 1])
            del a[i:i + 2]
    ghep(a[0], **kw)
