#!/usr/bin/env python3
"""Hook nhắc NGHI THỨC CUỐI PHIÊN cho dự án con video/.

Đúc từ hook cùng tên ở gốc. 4 sổ của video/ vẫn ghi VỀ GỐC repo
(tri_thuc/patch_history.md · tri_thuc/kinh_nghiem.md) — dự án con không mở
sổ riêng, tránh tri thức phân mảnh. HANDOFF thì cập nhật video/HANDOFF.md.

Chạy cho 2 event (đấu trong video/.claude/settings.json):
- PostToolUse (Write|Edit|NotebookEdit): ghi đường dẫn file đã sửa vào
  /tmp/claude_nghithuc_video_{session_id}.txt
- Stop: nếu phiên sửa file KỸ THUẬT (.py/.sh) mà CHƯA ghi patch_history → block
  1 lần kèm lời nhắc. Chống lặp: stop_hook_active + marker 30 phút.
"""
import json
import os
import sys
import time

REMIND_COOLDOWN = 30 * 60  # giây — không nhắc lại dày hơn mức này


def duong_dan_theo_doi(sid: str) -> str:
    # Cứng /tmp để PostToolUse và Stop luôn thấy CÙNG một file (bài học macOS:
    # TMPDIR mỗi process một khác). Thêm "_video_" để không đụng hook gốc.
    return f"/tmp/claude_nghithuc_video_{sid}.txt"


def la_file_ky_thuat(p: str) -> bool:
    # Ghi sổ tri_thuc/ CHÍNH LÀ nghi thức → không tính; .claude/ là hạ tầng;
    # kichban/*.md là nội dung sáng tác, không phải kỹ thuật.
    if "/tri_thuc/" in p or "/.claude/" in p or "/scratchpad" in p:
        return False
    return p.endswith((".py", ".sh"))


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    sid = data.get("session_id") or "nosession"
    track = duong_dan_theo_doi(sid)
    event = data.get("hook_event_name") or ("PostToolUse" if "tool_name" in data else "Stop")

    if event == "PostToolUse":
        fp = (data.get("tool_input") or {}).get("file_path") or ""
        if fp:
            with open(track, "a") as f:
                f.write(fp + "\n")
        sys.exit(0)

    # ---- Stop ----
    if data.get("stop_hook_active"):
        sys.exit(0)  # vừa nhắc xong trong chính lượt này — cho dừng, tránh lặp vô hạn

    try:
        with open(track) as f:
            paths = f.read().splitlines()
    except FileNotFoundError:
        sys.exit(0)

    ky_thuat = sorted({p for p in paths if la_file_ky_thuat(p)})
    da_ghi_so = any(p.endswith("tri_thuc/patch_history.md") for p in paths)
    if not ky_thuat or da_ghi_so:
        sys.exit(0)

    marker = track + ".reminded"
    if os.path.exists(marker) and time.time() - os.path.getmtime(marker) < REMIND_COOLDOWN:
        sys.exit(0)
    with open(marker, "w") as f:
        f.write(str(time.time()))

    danh_sach = "\n".join(f"  - {p}" for p in ky_thuat[:15])
    reason = (
        "⚠️ NHẮC NGHI THỨC dự án con video/ (hook tự động): phiên này đã sửa file "
        "kỹ thuật nhưng CHƯA ghi tri_thuc/patch_history.md (sổ ở GỐC repo).\n"
        f"File đã sửa:\n{danh_sach}\n"
        "Nếu việc ĐÃ XONG: (1) mục mới LÊN ĐẦU ../tri_thuc/patch_history.md; "
        "(2) bẫy/bài học → ../tri_thuc/kinh_nghiem.md; "
        "(3) cập nhật TRẠNG THÁI + VIỆC CHỜ trong video/HANDOFF.md; "
        "(4) sửa lam_video.py hay đổi định dạng kịch bản → cập nhật video/README.md.\n"
        "Nếu việc ĐANG DỞ: nói ngắn 1 câu cho BOSS biết sẽ ghi sổ khi xong, "
        "rồi dừng bình thường — KHÔNG cần ghi ngay."
    )
    print(json.dumps({"decision": "block", "reason": reason}, ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
