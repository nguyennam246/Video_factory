#!/usr/bin/env python3
"""KHOÁ RENDER — chỉ cho MỘT tiến trình quay/render chạy một lúc (BOSS lệnh 25/07/2026).

    # trong script python
    from khoa_render import khoa_render
    with khoa_render("render deck_sp09"):
        ...   # việc dùng Chromium / ffmpeg

    # bọc một lệnh bất kỳ ngoài shell
    python3 video/khoa_render.py --viec "render tay" -- .venv/bin/python headless/render_headless.py deck_x

    # xem ai đang giữ khoá
    python3 video/khoa_render.py --kiem

═══════════════════════════════════════════════════════════════════════════════
VÌ SAO CẦN KHOÁ — không phải để cho gọn, mà vì tranh CPU LÀM HỎNG OUTPUT
  Sổ kinh nghiệm 23/07: render native 1080 trên máy này **GIÃN TIMELINE** —
  video ra 180,6s trong khi giọng chỉ 112,9s, vì main thread không kịp. Hai bản
  render chạy cùng lúc là đúng điều kiện gây ra nó, và **không script nào báo lỗi**:
  mp4 vẫn ra, vẫn exit 0, chỉ là hình lệch tiếng.
  Ngày 25/07 đã đụng thật: hai phiên Claude cùng làm video, một phiên render pnj02
  trong khi phiên kia sắp render sp07b.

VÌ SAO `ps` KHÔNG ĐỦ
  `ps` chỉ đúng vào đúng giây mình nhìn. Phiên khác bật render 5 giây sau là lọt.
  `flock` thì hỏi HỆ ĐIỀU HÀNH, và **tự nhả khi tiến trình chết** — nên không có
  chuyện file khoá cũ của một tiến trình đã tắt chặn cả máy (bẫy của khoá tự viết
  bằng "có file thì coi như đang chạy").

ĐẶT KHOÁ Ở ĐÂU
  Đặt TRONG script làm việc thật (`render_headless.py`, `auto_render.py`,
  `capture_slides.py`), KHÔNG đặt ở `lam_bai.py`. Lý do: khoá chỉ ăn khi MỌI đường
  gọi đều đi qua nó — và phiên khác vẫn gọi `render_headless.py` bằng tay.
  KHÔNG khoá `validate_slide.py` / `dung_nhac_synth.py`: chúng chạy vài giây, đo
  layout chứ không quay, chặn chúng chỉ làm phiên khác đứng chờ vô ích.
═══════════════════════════════════════════════════════════════════════════════
"""
from __future__ import annotations

import argparse
import contextlib
import errno
import fcntl
import json
import os
import subprocess
import sys
import time
from pathlib import Path

# state/ nằm ở thư mục CHA của video/ (cùng chỗ state/video_tts đang dùng)
KHOA = Path(__file__).resolve().parent.parent / "state" / "dang_render.lock"
MA_THOAT_BUSY = 50          # trùng dải mã thoát của lam_bai.py (10/20/30/40)


def _doc_chu_khoa() -> dict:
    """Đọc thông tin tiến trình đang giữ khoá. Chỉ để BÁO, không để quyết định."""
    try:
        return json.loads(KHOA.read_text(encoding="utf-8") or "{}")
    except Exception:
        return {}


def _mo_ta_chu_khoa() -> str:
    d = _doc_chu_khoa()
    if not d:
        return "(không đọc được thông tin, nhưng khoá đang bị giữ)"
    tuoi = time.time() - d.get("luc", 0)
    return (f"pid {d.get('pid', '?')} · việc \"{d.get('viec', '?')}\" · "
            f"bắt đầu {time.strftime('%H:%M:%S', time.localtime(d.get('luc', 0)))} "
            f"({tuoi / 60:.1f} phút trước)")


@contextlib.contextmanager
def khoa_render(viec: str, cho_giay: float = 0.0, im: bool = False):
    """Giữ khoá render trong khối `with`. Không lấy được thì raise KhoaBiGiu.

    cho_giay > 0  ⇒ chờ tối đa bao nhiêu giây rồi mới bỏ.
    """
    KHOA.parent.mkdir(parents=True, exist_ok=True)
    f = open(KHOA, "a+", encoding="utf-8")          # noqa: SIM115 — giữ mở suốt khối
    het = time.time() + cho_giay
    da_bao = False
    da_giu = False          # ⚠️ phải có: không có nó thì lúc XIN HỤT khoá, khối finally
                            # vẫn in "🔓 nhả khoá" — thông điệp sai trong đúng công cụ
                            # chống xung đột, đọc log sau này sẽ chẩn đoán nhầm.
    try:
        while True:
            try:
                fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError as e:
                if e.errno not in (errno.EAGAIN, errno.EACCES):
                    raise
                if not da_bao and not im:
                    print(f"⏳ KHOÁ RENDER đang bị giữ: {_mo_ta_chu_khoa()}", flush=True)
                    da_bao = True
                if time.time() >= het:
                    f.close()
                    raise KhoaBiGiu(_mo_ta_chu_khoa())
                time.sleep(2)

        da_giu = True
        f.seek(0)
        f.truncate()
        f.write(json.dumps({"pid": os.getpid(), "viec": viec, "luc": time.time()},
                           ensure_ascii=False))
        f.flush()
        if not im:
            print(f"🔒 giữ khoá render: {viec} (pid {os.getpid()})", flush=True)
        yield
    finally:
        if da_giu:
            with contextlib.suppress(Exception):
                f.seek(0)
                f.truncate()
                f.flush()
            with contextlib.suppress(Exception):
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)
        with contextlib.suppress(Exception):
            f.close()
        if da_giu and not im:
            print("🔓 nhả khoá render", flush=True)


class KhoaBiGiu(RuntimeError):
    """Không lấy được khoá vì tiến trình khác đang render."""


def bao_roi_thoat(viec: str, cho_giay: float = 0.0):
    """Dùng ở đầu script làm việc: lấy khoá, hoặc in lời khuyên rồi exit 50.

    Trả về context manager đã vào — script gọi `with bao_roi_thoat(...)`.
    """
    try:
        cm = khoa_render(viec, cho_giay=cho_giay)
        cm.__enter__()
        return cm
    except KhoaBiGiu as e:
        print(f"\n❌ KHÔNG RENDER LÚC NÀY — tiến trình khác đang quay/render.\n"
              f"   đang giữ: {e}\n"
              f"   Vì sao chặn: hai bản render cùng lúc làm GIÃN TIMELINE (hình dài hơn\n"
              f"   tiếng) mà KHÔNG script nào báo lỗi — mp4 vẫn ra, vẫn exit 0.\n"
              f"   Cách đi tiếp: chờ nó xong rồi chạy lại, hoặc thêm --cho-khoa <giây>\n"
              f"   để tự xếp hàng. Xem ai giữ: python3 video/khoa_render.py --kiem",
              file=sys.stderr)
        sys.exit(MA_THOAT_BUSY)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--kiem", action="store_true", help="xem khoá có đang bị giữ không")
    p.add_argument("--viec", default="lệnh ngoài", help="mô tả việc, để phiên khác biết ai giữ")
    p.add_argument("--cho-khoa", type=float, default=0.0, dest="cho",
                   help="chờ tối đa bao nhiêu giây (0 = không chờ, thoát ngay)")
    p.add_argument("lenh", nargs="*", help="đặt sau `--`: lệnh cần bọc trong khoá")
    a = p.parse_args()

    if a.kiem:
        if not KHOA.exists():
            print("✓ chưa từng có ai render (chưa có file khoá)")
            return 0
        f = open(KHOA, "a+", encoding="utf-8")       # noqa: SIM115
        try:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
            print("✓ KHOÁ ĐANG RẢNH — được phép render")
            return 0
        except OSError:
            print(f"🔒 KHOÁ ĐANG BỊ GIỮ: {_mo_ta_chu_khoa()}")
            return MA_THOAT_BUSY
        finally:
            f.close()

    if not a.lenh:
        p.error("cần một lệnh sau `--`, hoặc dùng --kiem")
    cm = bao_roi_thoat(a.viec, cho_giay=a.cho)
    try:
        return subprocess.run(a.lenh).returncode
    finally:
        cm.__exit__(None, None, None)


if __name__ == "__main__":
    sys.exit(main())
