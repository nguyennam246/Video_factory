#!/usr/bin/env python3
"""Thước tất định cho bộ hook video/ — 0 API.
Chạy: python3 video/.claude/hooks/_thu_hook.py (từ gốc repo hay từ video/ đều được).
"""
import json
import os
import subprocess
import sys

VIDEO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NAP = os.path.join(VIDEO, ".claude/hooks/nap_handoff.py")
NHAC = os.path.join(VIDEO, ".claude/hooks/nhac_nghi_thuc.py")
KHOA_CMD = 'p="$CLAUDE_PROJECT_DIR/../.claude/hooks/khoa_dulieu_tho.py"; if [ -f "$p" ]; then python3 "$p"; else exit 0; fi'


def chay_py(hook, payload):
    p = subprocess.run(
        [sys.executable, hook],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        env={**os.environ, "CLAUDE_PROJECT_DIR": VIDEO},
    )
    return p.stdout.strip(), p.stderr.strip(), p.returncode


def chay_khoa(payload):
    """Chạy đúng chuỗi lệnh shell đấu trong settings.json — thử cả wrapper."""
    p = subprocess.run(
        ["/bin/sh", "-c", KHOA_CMD],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        env={**os.environ, "CLAUDE_PROJECT_DIR": VIDEO},
    )
    return p.stdout.strip(), p.returncode


loi = 0

print("=== NẠP HANDOFF (video/) ===")
out, err, rc = chay_py(NAP, {"hook_event_name": "SessionStart", "source": "startup"})
try:
    o = json.loads(out)
    ctx = o["hookSpecificOutput"]["additionalContext"]
    assert o["hookSpecificOutput"]["hookEventName"] == "SessionStart"
    print(f"  ✓ trả JSON đúng khoá; dài {len(ctx)} ký tự (~{len(ctx)//4} token)")
    for phai_co in ("TRẠNG THÁI HIỆN TẠI", "ĐANG THI CÔNG DỞ", "AI KHÔNG NGHE ĐƯỢC"):
        if phai_co in ctx:
            print(f"  ✓ có: {phai_co}")
        else:
            loi += 1
            print(f"  ✗ THIẾU: {phai_co}")
    if "CÔNG THỨC VIẾT KỊCH BẢN" in ctx:
        loi += 1
        print("  ✗ LẤY LẸM sang mục tham khảo (cắt khoang sai)")
    else:
        print("  ✓ không lấn sang mục tham khảo")
    if len(ctx) > 13000:
        loi += 1
        print(f"  ✗ VƯỢT trần token: {len(ctx)}")
except Exception as e:
    loi += 1
    print(f"  ✗ output hỏng: {e}\n      stdout={out!r} stderr={err!r}")

print("\n=== KHOÁ DỮ LIỆU THÔ (wrapper gọi xuyên lên gốc) ===")
phai_chan = [
    ("rm BCTC.db từ video/", {"tool_name": "Bash", "tool_input": {"command": "rm ../dulieu/BCTC.db"}}),
    ("Write vào NQ", {"tool_name": "Write", "tool_input": {"file_path": f"{VIDEO}/../state/results_nq/x.md"}}),
]
phai_lot = [
    ("ghi kịch bản", {"tool_name": "Write", "tool_input": {"file_path": f"{VIDEO}/kichban/01_hooks.md"}}),
    ("render video", {"tool_name": "Bash", "tool_input": {"command": ".venv/bin/python video/lam_video.py video/kichban/01_hooks.md"}}),
    ("ghi results/video", {"tool_name": "Bash", "tool_input": {"command": "ffmpeg -i a.mp4 ../results/video/out.mp4"}}),
]
for ten, pl in phai_chan:
    out, rc = chay_khoa(pl)
    if '"deny"' in out:
        print(f"  ✓ chặn: {ten}")
    else:
        loi += 1
        print(f"  ✗ LỌT (đáng lẽ chặn): {ten} → {out!r}")
for ten, pl in phai_lot:
    out, rc = chay_khoa(pl)
    if '"deny"' in out:
        loi += 1
        print(f"  ✗ CHẶN NHẦM: {ten} → {out}")
    elif rc != 0:
        loi += 1
        print(f"  ✗ exit {rc} (đáng lẽ 0 — exit≠0 ở PreToolUse là chặn nhầm): {ten}")
    else:
        print(f"  ✓ lọt: {ten}")

# Wrapper phải im lặng cho qua khi KHÔNG tìm thấy hook gốc (video/ tách repo sau này)
p = subprocess.run(
    ["/bin/sh", "-c", KHOA_CMD],
    input="{}",
    capture_output=True,
    text=True,
    env={**os.environ, "CLAUDE_PROJECT_DIR": "/tmp/khong_ton_tai_xyz"},
)
if p.returncode == 0:
    print("  ✓ thiếu hook gốc → exit 0 (không chặn oan cả phiên)")
else:
    loi += 1
    print(f"  ✗ thiếu hook gốc mà exit {p.returncode} → sẽ CHẶN MỌI tool call!")

print("\n=== NHẮC NGHI THỨC (video/) ===")
sid = "thu_hook_video_test"
track = f"/tmp/claude_nghithuc_video_{sid}.txt"
for f in (track, track + ".reminded"):
    if os.path.exists(f):
        os.remove(f)
# 1. PostToolUse ghi file kỹ thuật
chay_py(NHAC, {"hook_event_name": "PostToolUse", "session_id": sid,
               "tool_name": "Edit", "tool_input": {"file_path": f"{VIDEO}/lam_video.py"}})
out, err, rc = chay_py(NHAC, {"hook_event_name": "Stop", "session_id": sid})
if '"block"' in out and "patch_history" in out:
    print("  ✓ sửa .py chưa ghi sổ → block kèm lời nhắc")
else:
    loi += 1
    print(f"  ✗ đáng lẽ block: {out!r}")
# 2. Đã ghi sổ → cho qua (xoá marker để không dính cooldown)
os.remove(track + ".reminded")
chay_py(NHAC, {"hook_event_name": "PostToolUse", "session_id": sid,
               "tool_name": "Edit",
               "tool_input": {"file_path": f"{VIDEO}/../tri_thuc/patch_history.md"}})
out, err, rc = chay_py(NHAC, {"hook_event_name": "Stop", "session_id": sid})
if '"block"' not in out:
    print("  ✓ đã ghi patch_history → cho dừng êm")
else:
    loi += 1
    print(f"  ✗ chặn nhầm dù đã ghi sổ: {out!r}")
# 3. Chỉ sửa kịch bản .md → không nhắc
for f in (track, track + ".reminded"):
    if os.path.exists(f):
        os.remove(f)
chay_py(NHAC, {"hook_event_name": "PostToolUse", "session_id": sid,
               "tool_name": "Write", "tool_input": {"file_path": f"{VIDEO}/kichban/05.md"}})
out, err, rc = chay_py(NHAC, {"hook_event_name": "Stop", "session_id": sid})
if '"block"' not in out:
    print("  ✓ chỉ sửa kịch bản .md → không nhắc")
else:
    loi += 1
    print(f"  ✗ nhắc nhầm với file nội dung: {out!r}")
for f in (track, track + ".reminded"):
    if os.path.exists(f):
        os.remove(f)

print(f"\n{'✅ SẠCH' if loi == 0 else f'❌ {loi} LỖI'}")
sys.exit(1 if loi else 0)
