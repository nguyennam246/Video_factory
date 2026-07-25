#!/usr/bin/env python3
"""Hook SessionStart (dự án con video/) — tự nạp TRẠNG THÁI + VIỆC CHỜ từ video/HANDOFF.md.

Đúc từ hook cùng tên ở gốc repo (bài học: nghi thức phụ thuộc trí nhớ thì có ngày
bị quên — hook biến nó thành tự động). Chỉ nạp 2 khoang SỐNG + trần ký tự riêng
từng khoang (kỷ luật token BOSS 22/07: nạp cả file = trả tiền lại mỗi lượt).

Chỉ chạy khi mở phiên TẠI video/ (CLAUDE_PROJECT_DIR = video/). Mở tại gốc repo
thì hook gốc lo, hook này không dính.

Đấu trong video/.claude/settings.json với matcher "startup|clear".
"""
import json
import os
import sys

# Trần RIÊNG từng khoang (bài học đo 23/07 ở gốc: trần chung → khoang đầu ăn hết
# quota, khoang việc-chờ bị cắt sạch). Việc-chờ là thứ AI phải hành động → ưu tiên.
KHOANG = [
    ("### 🎯 ĐANG THI CÔNG DỞ", 5000),
    ("## 📍 TRẠNG THÁI HIỆN TẠI", 7000),
]


def cap_heading(dong: str) -> int:
    """Số '#' đầu dòng; 0 nếu không phải heading."""
    n = 0
    for ch in dong:
        if ch == "#":
            n += 1
        else:
            break
    return n if n and dong[n : n + 1] == " " else 0


def lay_khoang(dong_list: list, tien_to: str) -> str:
    """Lấy từ dòng heading khớp tiền tố tới heading kế cùng cấp-hoặc-cao-hơn."""
    for i, d in enumerate(dong_list):
        if d.startswith(tien_to):
            cap = cap_heading(d)
            ket = len(dong_list)
            for j in range(i + 1, len(dong_list)):
                c = cap_heading(dong_list[j])
                if c and c <= cap:
                    ket = j
                    break
            return "\n".join(dong_list[i:ket]).rstrip()
    return ""


def main() -> None:
    try:
        json.load(sys.stdin)  # nuốt payload; hook này không cần trường nào
    except Exception:
        pass

    goc = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    handoff = os.path.join(goc, "HANDOFF.md")
    try:
        with open(handoff, encoding="utf-8") as f:
            dong_list = f.read().splitlines()
    except OSError:
        sys.exit(0)  # không có file thì im lặng, đừng chặn phiên

    phan = []
    for tien_to, tran in KHOANG:
        p = lay_khoang(dong_list, tien_to)
        if not p:
            continue
        if len(p) > tran:
            p = p[:tran] + (
                f"\n…[hook cắt khoang này ở {tran} ký tự để giữ kỷ luật token — "
                "đọc trực tiếp video/HANDOFF.md nếu cần phần sau]"
            )
        phan.append(p)
    than = "\n\n".join(phan)
    if not than:
        sys.exit(0)

    noi_dung = (
        "📋 NGHI THỨC ĐẦU PHIÊN dự án con video/ (hook tự nạp).\n"
        "Dưới đây là 2 khoang SỐNG trích từ video/HANDOFF.md, KHÔNG phải cả file.\n"
        "Còn lại tự đọc khi cần: video/HANDOFF.md (đủ) · video/CLAUDE.md (luật riêng) · "
        "video/README.md (cách chạy + định dạng kịch bản) · ../tri_thuc/kinh_nghiem.md "
        "(bẫy kỹ thuật).\n"
        "⚠️ 2 luật sống còn của dự án này: (1) AI KHÔNG NGHE ĐƯỢC — mọi phán xét giọng "
        "để BOSS nghe; (2) đầu ra là ẢNH thì phải MỞ RA SOI, không tin exit code.\n"
        "Nhận việc chờ rồi BÁO BOSS trước khi tự khởi động việc lớn.\n\n"
        f"{than}"
    )

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": noi_dung,
                }
            },
            ensure_ascii=False,
        )
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
