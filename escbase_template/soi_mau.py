#!/usr/bin/env python3
"""Dò MÀU LẠC trong ảnh chụp slide — thứ mà validate_slide.py không bao giờ bắt được.

Bẫy đã trả giá 24/07: deck bài 05 (rose+gold) còn sót `#a5a0ff` làm icon hiện ra TÍM
và `#cdeffd` làm chữ hiện ra XANH. `validate_slide.py` PASS hoàn toàn; chỉ mở ảnh nhìn
mới thấy. File này tự động hoá đúng khâu đó: gom các điểm ảnh có màu ĐẬM rồi báo màu
nào lệch khỏi bảng màu của bài.

Cách dùng:
    .venv/bin/python soi_mau.py /tmp/escbase-qa/<slug> 07

KHÔNG thay được việc soi mắt: nó chỉ bắt MÀU, không bắt chữ tràn, chữ cắt, gạch hụt,
hay bố cục thưa. Vẫn phải Read từng ảnh.
"""
import colorsys
import sys
from pathlib import Path

from PIL import Image

# Sắc độ (hue, 0-360) hợp lệ của từng bài. Lấy từ DICH trong remap_palette.py.
SAC_DO = {
    "05": [347, 43, 160],        # rose, gold, emerald
    "06": [199, 79, 142],        # sky, lime, green
    "07": [173, 27, 142],        # teal, cam, green
    "08": [258, 142],            # tím, lục
    "09": [25, 199, 142],        # cam, sky, green
    "10": [160, 48, 142],        # emerald, vàng, green
}
# Ngưỡng 45°: đủ rộng để BỎ QUA màu pha trong gradient (hiệu chỉnh trên bài 05 đã soi
# mắt là sạch: gradient rose 347° + gold 43° đẻ ra sắc ~20°, ngưỡng 22° báo nhầm).
# Vẫn thừa sức bắt màu lạc THẬT của 24/07: tím #a5a0ff lệch 89°, xanh #cdeffd lệch 147°.
NGUONG_LECH = 45

# Sắc CHO PHÉP Ở MỌI BÀI: đỏ "sai / nguy hiểm" (#ff8a95, #ff4757, #ff5252) là màu
# ngữ nghĩa CỐ ĐỊNH xuyên cả bộ, không nằm trong bảng 8 màu vai trò nên remap không
# đụng tới. Không whitelist thì thước báo nhầm ở gần như mọi deck (đã đo 24/07).
SAC_CHUNG = [350]
MIN_TY_LE = 0.0006  # bỏ qua đốm quá nhỏ (nhiễu hạt nền)


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[2] not in SAC_DO:
        print(__doc__)
        print("Bài hợp lệ:", ", ".join(sorted(SAC_DO)))
        return 2

    thu_muc = Path(sys.argv[1])
    hop_le = SAC_DO[sys.argv[2]] + SAC_CHUNG
    anh = sorted(thu_muc.glob("slide*.png"),
                 key=lambda p: int("".join(c for c in p.stem if c.isdigit())))
    if not anh:
        print(f"❌ Không thấy ảnh slide*.png trong {thu_muc}")
        return 1

    print(f"Bảng sắc hợp lệ: {hop_le} (lệch > {NGUONG_LECH}° là nghi)\n")
    tong_nghi = 0
    for f in anh:
        im = Image.open(f).convert("RGB")
        im.thumbnail((300, 540))          # co nhỏ cho nhanh, đủ để bắt mảng màu
        thung = {}
        n = 0
        for r, g, b in im.getdata():
            h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
            if s < 0.45 or l < 0.18 or l > 0.92:   # bỏ nền tối, chữ trắng, xám
                continue
            thung[int(h * 360) // 10 * 10] = thung.get(int(h * 360) // 10 * 10, 0) + 1
            n += 1
        tong_px = im.size[0] * im.size[1]
        nghi = []
        for sac, dem in sorted(thung.items(), key=lambda x: -x[1]):
            if dem / tong_px < MIN_TY_LE:
                continue
            lech = min(min(abs(sac - h), 360 - abs(sac - h)) for h in hop_le)
            if lech > NGUONG_LECH:
                nghi.append((sac, dem, lech))
        if nghi:
            tong_nghi += len(nghi)
            print(f"  ⚠️ {f.name}: sắc lạ ->", ", ".join(
                f"{s}° ({d} px, lệch {l}°)" for s, d, l in nghi))
        else:
            print(f"  ✅ {f.name}: màu sạch")

    print()
    if tong_nghi:
        print(f"❌ {tong_nghi} chỗ nghi màu lạc. MỞ ĐÚNG ẢNH ĐÓ RA NHÌN rồi grep mã màu"
              f" trong style.css để sửa.")
    else:
        print("✅ Không thấy màu lạc. (Vẫn phải Read từng ảnh: thước này KHÔNG bắt"
              " chữ tràn / gạch hụt / bố cục.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
