#!/usr/bin/env python3
"""Đổi palette cho deck escbase mới chép từ deck bài 05 (rose+gold).

Vì sao có file này (bẫy đã trả giá 24/07):
  1. Sửa mỗi `:root` trong style.css là KHÔNG ĐỦ. Màu lúc chạy lấy từ
     `defaultPreviewSettings` trong app.js. Phải đổi cả style.css + app.js +
     preview-settings.json.
  2. Còn hàng trăm mã màu HARDCODE rải rác (kể cả dạng rgba). Phải remap cả
     `#hex` lẫn `rgba(r,g,b` / `rgb(r,g,b)`.
  3. Thay thế TUẦN TỰ có thể map chồng 2 lần (A->B rồi B->C thành A->C). File này
     thay thế MỘT LƯỢT ĐỒNG THỜI nên an toàn kể cả khi màu đích trùng màu nguồn.

Cách dùng:
    .venv/bin/python remap_palette.py slide/<deck> 06          # khoá đã phân sẵn
    .venv/bin/python remap_palette.py slide/<deck> --mau "#38bdf8,#fbbf24"
    .venv/bin/python remap_palette.py slide/<deck> --liet-ke   # xem các khoá có sẵn

Bảng màu tự chọn (`--mau`): đưa 2 màu (primary + accent) là đủ — 6 vai còn lại
suy ra tự động (sáng/tối hơn theo đúng tỉ lệ của các bảng đã chốt). Muốn kiểm
soát hết thì đưa đủ 8 màu theo thứ tự VAI_TRO.

Xong thì BẮT BUỘC capture + soi mắt: có những màu lạc chỉ lộ ra khi nhìn ảnh
(24/07 sót `#a5a0ff` làm icon tím và `#cdeffd` làm chữ xanh, validate vẫn PASS).
"""
import colorsys
import re
import sys
from pathlib import Path

# Màu ĐANG CÓ trong deck bài 05 (nguồn để chép). Thứ tự = vai trò bên dưới.
VAI_TRO = ["primary", "primary-light", "primary-dark", "accent",
           "accent-light", "success", "info", "chu-hk-note"]
NGUON = ["#f43f5e", "#ffa2b3", "#8f1533", "#fbbf24",
         "#fde68a", "#34d399", "#fb7185", "#ffe1e6"]

# Palette đã phân sẵn cho từng bài. ĐỪNG tự chọn màu khác: phân trung tâm để
# 10 bài không đụng màu nhau (01 xanh lá · 02 indigo · 03 amber · 04 cyan · 05 rose).
DICH = {
    "06": ["#38bdf8", "#9ad9fb", "#0c5a7a", "#a3e635",   # sky + lime (điện, ổ cắm)
           "#d4f58a", "#22c55e", "#7dd3fc", "#e0f2fe"],
    "07": ["#14b8a6", "#7fe6da", "#0a5c53", "#fb923c",   # teal + cam (bàn trước, cầm búa sau)
           "#fdc99a", "#22c55e", "#5eead4", "#ccfbf1"],
    "08": ["#8b5cf6", "#c4b0fd", "#4c2a9e", "#22c55e",   # tím + lục (quay ngược thời gian)
           "#86efac", "#4ade80", "#a78bfa", "#ede9fe"],
    "09": ["#f97316", "#fdba8c", "#8a3d06", "#38bdf8",   # cam + sky (đắt lên, cảnh báo)
           "#9ad9fb", "#22c55e", "#fb923c", "#ffedd5"],
    "10": ["#10b981", "#7fe0c0", "#075f46", "#facc15",   # lục + vàng (khép bộ, gọi lại bài 01)
           "#fef08a", "#22c55e", "#6ee7b7", "#d1fae5"],
    # SERIES SUPERPOWERS (8 bài) — DÙNG CHUNG một bảng màu cho cả series, cố ý
    # khác luật "mỗi bài 1 màu" của bộ dạy Claude Code: xem 8 bài phải nhận ra
    # cùng một bộ (giống series rủi ro). Xanh bản vẽ + hổ phách công trường.
    "sp": ["#38bdf8", "#bae6fd", "#075985", "#fbbf24",
           "#fde68a", "#34d399", "#7dd3fc", "#e0f2fe"],
    # SERIES PHÂN TÍCH TÀI CHÍNH (ruiro_01-03 + msr_01…) — DÙNG CHUNG một bảng cho
    # cả series, giống series sp. Vàng đèn pin + đỏ cảnh báo, chốt 24/07 ở bài
    # ruiro_01_TCL (khi đó remap tay); nay đóng thành khoá để bài sau khỏi chép tay.
    # `success` giữ XANH LỤC cố ý: slide 7 MẶT KIA cần một màu "cái tốt" tách khỏi
    # tông cảnh báo, nếu không cả bài chỉ một tông thì squint-test là lỗi.
    "tc": ["#ffb020", "#ffd28a", "#7a4d00", "#ef4444",
           "#fca5a5", "#34d399", "#ffcf8a", "#fff2dd"],
}

FILES = ("style.css", "app.js", "preview-settings.json")


def rgb(h: str):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _hex(r: float, g: float, b: float) -> str:
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(v * 255))) for v in (r, g, b))


def _doi_do_sang(mau: str, do_sang: float) -> str:
    """Giữ nguyên tông (hue) và độ bão hoà, chỉ kéo độ sáng.

    Hệ số ĐO NGƯỢC từ 7 bảng màu đã chốt, không phải đoán. Ví dụ khoá `sp`
    (#38bdf8 L=0,596): light #bae6fd L=0,86 → ×1,44 · dark #075985 L=0,275 →
    ×0,46 · info #7dd3fc → ×1,24 · chu #e0f2fe → ×1,57. Khoá `tc` cho ×1,37 /
    ×0,42 / ×1,37 / ×1,66. Lấy khoảng giữa.
    Chặn trần L ở 0,93: nhân thẳng là bão hoà thành TRẮNG BỆCH, mất sạch tông màu."""
    r, g, b = (v / 255 for v in rgb(mau))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return _hex(*colorsys.hls_to_rgb(h, max(0.04, min(0.93, l * do_sang)), s))


def suy_bang_mau(primary: str, accent: str) -> list[str]:
    """8 vai từ 2 màu. success giữ XANH LỤC cố định — mọi bảng đã chốt đều thế,
    vì cần một màu "cái tốt" tách khỏi tông chính, nếu không cả bài một tông
    là hỏng phép squint-test."""
    return [
        primary,
        _doi_do_sang(primary, 1.42),   # primary-light
        _doi_do_sang(primary, 0.44),   # primary-dark
        accent,
        _doi_do_sang(accent, 1.36),    # accent-light
        "#34d399",                     # success — cố định
        _doi_do_sang(primary, 1.28),   # info
        _doi_do_sang(primary, 1.60),   # chu-hk-note
    ]


def doc_tham_so(argv: list[str]) -> tuple[Path, list[str], str] | None:
    """Trả (deck, 8 màu đích, nhãn) hoặc None nếu tham số sai."""
    if len(argv) < 3:
        return None
    deck = Path(argv[1])
    if argv[2] == "--mau":
        if len(argv) < 4:
            return None
        ds = [c.strip() for c in argv[3].replace(" ", ",").split(",") if c.strip()]
        for c in ds:
            if not re.fullmatch(r"#[0-9a-fA-F]{6}", c):
                print(f"❌ Màu không hợp lệ: {c} (phải dạng #rrggbb)")
                return None
        if len(ds) == 2:
            return deck, suy_bang_mau(*ds), f"tự chọn {ds[0]} + {ds[1]}"
        if len(ds) == len(VAI_TRO):
            return deck, ds, "tự chọn (đủ 8 vai)"
        print(f"❌ --mau cần 2 màu (primary,accent) hoặc đủ {len(VAI_TRO)} màu; "
              f"đang có {len(ds)}")
        return None
    if argv[2] in DICH:
        return deck, DICH[argv[2]], f"khoá '{argv[2]}'"
    return None


def main() -> int:
    if len(sys.argv) >= 3 and sys.argv[2] == "--liet-ke":
        print("Khoá có sẵn:")
        for k, v in sorted(DICH.items()):
            print(f"  {k:<4} primary {v[0]}  accent {v[3]}")
        return 0

    ts = doc_tham_so(sys.argv)
    if ts is None:
        print(__doc__)
        print("Khoá hợp lệ:", ", ".join(sorted(DICH)))
        return 2
    deck, dich, nhan = ts
    if not deck.is_dir():
        print(f"❌ Không thấy deck: {deck}")
        return 1

    print(f"Đổi palette deck {deck.name} sang bảng màu {nhan}:")
    for v, a, b in zip(VAI_TRO, NGUON, dich):
        print(f"  {v:<14} {a} -> {b}")
    print()

    # Bảng tra một lượt: khoá là chuỗi thường hoá, giá trị là màu mới.
    hex_map = {a.lower(): b for a, b in zip(NGUON, dich)}
    rgb_map = {rgb(a): rgb(b) for a, b in zip(NGUON, dich)}

    hex_re = re.compile("|".join(re.escape(a) for a in NGUON), re.I)
    rgb_re = re.compile(
        r"rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*(,|\))"
    )

    def sua_rgb(m):
        key = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
        if key not in rgb_map:
            return m.group(0)
        r, g, b = rgb_map[key]
        dau = "rgba(" if m.group(0).startswith("rgba") else "rgb("
        return f"{dau}{r}, {g}, {b}{m.group(4)}"

    tong = 0
    for name in FILES:
        f = deck / name
        if not f.exists():
            continue
        s = f.read_text(encoding="utf-8")
        s2, n1 = hex_re.subn(lambda m: hex_map[m.group(0).lower()], s)
        s2, n2 = rgb_re.subn(sua_rgb, s2)
        f.write_text(s2, encoding="utf-8")
        print(f"  {name:<24} {n1:>4} mã hex + {n2:>4} rgba = {n1 + n2}")
        tong += n1 + n2

    # soát màu cũ còn sót
    sot = 0
    for name in FILES:
        f = deck / name
        if not f.exists():
            continue
        s = f.read_text(encoding="utf-8")
        for a in NGUON:
            r, g, b = rgb(a)
            k = len(hex_re.findall(s)) if False else len(re.findall(re.escape(a), s, re.I))
            k += len(re.findall(rf"rgba?\(\s*{r}\s*,\s*{g}\s*,\s*{b}\s*[,)]", s))
            if k:
                print(f"  ⚠️ {name}: còn {k} chỗ màu cũ {a}")
                sot += k

    print(f"\nTổng đã đổi: {tong}")
    print("✅ SẠCH — không còn màu cũ." if sot == 0 else f"❌ CÒN SÓT {sot} chỗ.")
    print("\n⚠️ CHƯA XONG: phải capture + ĐỌC TỪNG ẢNH. Màu hardcode lạc palette")
    print("   (kiểu #a5a0ff, #cdeffd) chỉ lộ ra khi nhìn ảnh, validate vẫn PASS.")
    return 0 if sot == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
