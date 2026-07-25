#!/usr/bin/env python3
"""TỪ ĐIỂN PHÁT ÂM — đổi chữ TRƯỚC KHI gửi cho máy đọc, KHÔNG đụng phụ đề.

    from tts.phat_am import doc_am
    text_cho_may_doc = doc_am(line)        # "PNJ" -> "Pi En Giây"
    # còn `line` gốc vẫn đi vào timing.json ⇒ phụ đề vẫn hiện "PNJ"

Vì sao phải TÁCH HAI ĐƯỜNG (đo 25/07/2026): phụ đề lấy từ `timing.json["text"]`, mà
chuỗi đó chính là dòng thô trong `script-90s.txt` — đúng chuỗi được gửi cho TTS. Nên
nếu chỉ "viết lại cho dễ đọc" ngay trong kịch bản thì **phụ đề sẽ hiện "Pi En Giây"
thay vì "PNJ"**. Từ điển này chèn vào đúng một chỗ: ngay trước lời gọi engine.

BOSS chốt 25/07/2026 sau khi nghe 2 bài thử (`kichban/00c_*`, `00d_*`):
  · mã cổ phiếu  → **phương án C**: đọc tên chữ cái kiểu tiếng Anh ("Pi En Giây")
  · chữ tiếng Anh → **phương án B**: viết lại theo âm tiếng Việt ("su pơ pao ơ")

Bảng từ nằm ở `tts/phat_am.json` — **thêm từ là sửa JSON, không phải sửa code.**

Tự kiểm (0 API):  .venv/bin/python tts/phat_am.py --kiem
Thử một câu:      .venv/bin/python tts/phat_am.py "PNJ và hook trong Claude Code"
"""
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

BANG = Path(__file__).resolve().parent / "phat_am.json"

# Chữ có dấu tiếng Việt cũng phải tính là "chữ" khi dò biên từ, nếu không thì khoá
# "hook" sẽ khớp nhầm bên trong "hooka" mà lại không khớp "hook," ở cuối câu.
CHU = r"0-9A-Za-zÀ-ỹ"


@lru_cache(maxsize=1)
def _luat():
    """Trả list (regex đã biên dịch, chuỗi thay) — dài trước, ngắn sau.

    Sắp theo ĐỘ DÀI GIẢM DẦN là bắt buộc: "Claude Code" phải khớp trước "Claude",
    "slash command" trước "slash". Không sắp thì khoá ngắn ăn mất khoá dài.
    """
    if not BANG.is_file():
        return []
    data = json.loads(BANG.read_text(encoding="utf-8"))
    cap = []
    for nhom, muc in data.items():
        if nhom.startswith("_") or not isinstance(muc, dict):
            continue
        hoa_thuong = nhom != "phan_biet_hoa"
        for k, v in muc.items():
            if k.startswith("_"):
                continue
            cap.append((k, v, hoa_thuong))
    cap.sort(key=lambda x: -len(x[0]))
    ra = []
    for k, v, hoa_thuong in cap:
        pat = rf"(?<![{CHU}]){re.escape(k)}(?![{CHU}])"
        ra.append((re.compile(pat, re.IGNORECASE if hoa_thuong else 0), v))
    return ra


def doc_am(text: str) -> str:
    """Áp từ điển. Trả chuỗi để GỬI CHO MÁY ĐỌC. Không dùng cho phụ đề."""
    if not text:
        return text
    for pat, thay in _luat():
        text = pat.sub(thay.replace("\\", r"\\"), text)
    return text


def khac_gi(text: str):
    """Liệt kê (gốc, thay) đã áp — để in ra cho người soi, không dùng khi chạy thật."""
    ra = []
    for pat, thay in _luat():
        for m in pat.finditer(text):
            ra.append((m.group(0), thay))
    return ra


def _kiem() -> int:
    """Thước 0 API. Mỗi ca là một bẫy thật, đừng bỏ ca nào khi sửa."""
    ca = [
        # (vào, ra mong đợi)
        ("Giá cổ phiếu PNJ hôm nay", "Giá cổ phiếu Pi En Giây hôm nay"),
        ("PNJ vừa công bố.", "Pi En Giây vừa công bố."),          # đầu câu
        ("báo cáo của PNJ, quý một", "báo cáo của Pi En Giây, quý một"),  # dính dấu phẩy
        # khoá DÀI phải thắng khoá ngắn
        ("học Claude Code", "học Clốt Cốt"),
        ("hỏi Claude xem", "hỏi Clốt xem"),
        ("một slash command", "một xì lát com mừn"),
        # KHÔNG được ăn vào giữa từ khác
        ("PNJSC không phải mã", "PNJSC không phải mã"),
        ("hookah là thứ khác", "hookah là thứ khác"),
        # không phân biệt hoa thường
        ("dùng HOOK và Hook", "dùng húc và húc"),
        # chuỗi rỗng / không có gì để đổi
        ("Doanh thu thuần quý một", "Doanh thu thuần quý một"),
        ("", ""),
    ]
    hong = 0
    for vao, mong in ca:
        that = doc_am(vao)
        ok = that == mong
        hong += not ok
        print(f"  {'✅' if ok else '❌'} {vao!r}")
        if not ok:
            print(f"      mong: {mong!r}\n      thật: {that!r}")
    print(f"\n{'✅ ĐẠT' if not hong else f'❌ HỎNG {hong} ca'} · "
          f"{len(_luat())} khoá trong {BANG.name}")
    return 1 if hong else 0


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--kiem":
        sys.exit(_kiem())
    if len(sys.argv) == 2:
        vao = sys.argv[1]
        print("gốc (phụ đề)  :", vao)
        print("đọc (cho máy) :", doc_am(vao))
        for g, t in khac_gi(vao):
            print(f"   {g!r} -> {t!r}")
        sys.exit(0)
    print(__doc__)
    sys.exit(2)
