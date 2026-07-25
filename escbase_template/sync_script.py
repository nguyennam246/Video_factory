#!/usr/bin/env python3
"""Đồng bộ LỜI của một deck vào ĐÚNG 3 NƠI mà validate_slide.py so khớp từng chữ:

  1. <deck>/script-90s.txt
  2. const slideScripts = [...] trong <deck>/app.js
  3. slides.scriptLines trong <deck>/preview-settings.json

Vì sao có file này: chép tay vào 3 nơi là nguồn lỗi kinh điển của dây chuyền escbase
(lệch 1 dấu phẩy là validate FAIL, mò rất lâu). Dùng nó thì 3 nơi luôn giống hệt nhau.

Cách dùng:
    .venv/bin/python sync_script.py slide/<deck> ../kichban/escbase_10dong/06_mcp.txt

File lời đầu vào: mỗi DÒNG = 1 slide (thường 10 dòng). Số câu trong dòng
(tách theo . ? !) = số reveal, tức số thẻ .slide-element phải dựng trong slide đó.
Script in ra bảng đếm để đối chiếu trước khi sửa index.html.
"""
import json
import re
import sys
from pathlib import Path


def dem_cau(line: str) -> int:
    return len([s for s in re.split(r"(?<=[.?!])\s+", line.strip()) if s])


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2

    deck = Path(sys.argv[1])
    src = Path(sys.argv[2])
    if not deck.is_dir():
        print(f"❌ Không thấy deck: {deck}")
        return 1
    if not src.is_file():
        print(f"❌ Không thấy file lời: {src}")
        return 1

    lines = [l.strip() for l in src.read_text(encoding="utf-8").splitlines() if l.strip()]
    if not lines:
        print("❌ File lời rỗng")
        return 1

    xau = [l for l in lines if "—" in l]
    if xau:
        print("❌ Có dòng dính gạch dài '—' (TTS đọc xấu). Sửa trước khi đồng bộ:")
        for l in xau:
            print("   ", l[:70])
        return 1

    # 1. script-90s.txt
    (deck / "script-90s.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # 2. app.js
    app_path = deck / "app.js"
    app = app_path.read_text(encoding="utf-8")
    block = (
        "const slideScripts = [\n"
        + "".join("  " + json.dumps(l, ensure_ascii=False) + ",\n" for l in lines).rstrip(",\n")
        + "\n];"
    )
    app_new, n = re.subn(r"const slideScripts = \[.*?\n\];", block, app, count=1, flags=re.S)
    if n != 1:
        print("❌ Không tìm thấy khối 'const slideScripts = [...]' trong app.js")
        return 1
    app_path.write_text(app_new, encoding="utf-8")

    # 3. preview-settings.json
    ps_path = deck / "preview-settings.json"
    data = json.loads(ps_path.read_text(encoding="utf-8"))
    data.setdefault("slides", {})["scriptLines"] = lines
    ps_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"✅ Đã đồng bộ {len(lines)} slide vào 3 nơi của {deck.name}\n")
    print("slide | số câu = số .slide-element phải dựng trong index.html")
    tong = 0
    for i, l in enumerate(lines, 1):
        c = dem_cau(l)
        tong += c
        print(f"  {i:>2}  | {c}")
    print(f"TỔNG reveal = {tong}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
