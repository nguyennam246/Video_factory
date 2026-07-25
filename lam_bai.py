#!/usr/bin/env python3
"""LÀM MỘT BÀI VIDEO BẰNG MỘT LỆNH — xương sống dây chuyền escbase headless.

    python3 video/lam_bai.py --ma sp09 --ten dieu_phoi --loai kynang \
        --nguon video/nguon/superpowers_09.md

    # bài LÀM LẠI / bài gấp — đường rẻ (25/07/2026, BOSS lệnh):
    python3 video/lam_bai.py --ma pnj03 --ten hanhdong --loai baocao \
        --goc viec_can_lam --duong re

Vì sao có file này: dựng 1 bài đang phải gõ tay 6 lệnh nối nhau, mỗi chỗ nối là một
chỗ quên (đã quên phụ đề, quên remap palette, quên soi ảnh). Runner này giữ đúng thứ
tự + đóng CỔNG CHẶN ở chỗ đã từng trả giá.

════════════════════════════════════════════════════════════════════════════════
BA LOẠI BƯỚC — đọc kỹ chỗ này rồi hãy sửa file
  [MÁY]  chạy script thuần, 0 token, 0 API tiền. Chiếm 6/9 bước.
  [THỢ]  cần model viết chữ → gọi THỢ 2 (tài khoản Claude thứ 2 qua CLI).
         Hết quota / lỗi ⇒ KHÔNG tự đổi nhà khác, mà GHI BRIEF ra file rồi dừng
         với mã 20 để THỢ 1 (phiên đang chạy runner) tiếp quản. Lý do: việc này
         "có tay" — phải sửa file thật trên máy này; API free không có tay.
  [BOSS] người phải nhìn/nghe rồi phán. Runner DỪNG, không tự vượt.

Mã thoát: 0 xong · 1 hỏng · 10 cổng chặn không qua (thước FAIL) ·
          20 cần thợ 1 làm tiếp · 30 chờ soi ảnh · 40 chờ BOSS.
════════════════════════════════════════════════════════════════════════════════
"""
import argparse
import ast
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

VIDEO_DIR = Path(__file__).resolve().parent
ESC = VIDEO_DIR / "escbase_template"
PY = ESC / ".venv" / "bin" / "python"
HEADLESS = ESC / "headless"
KETQUA = VIDEO_DIR.parent / "results" / "video"
THUOC_BAOCAO = VIDEO_DIR / ".claude" / "skills" / "video-baocao" / "thuoc"
THUOC_KYNANG = VIDEO_DIR / ".claude" / "skills" / "video-kynang" / "thuoc"

# Giọng ĐÃ CHỐT — BOSS duyệt 2 vòng 20 giọng, và bác ElevenLabs ngày 24/07.
# ĐỪNG đổi ở đây. Muốn đổi thì dựng bài thử ngắn cho BOSS nghe TRƯỚC.
GIONG = ("edge", "vi-VN-NamMinhNeural", "+14%")

# Palette theo SERIES chứ không theo bài (remap_palette.py chỉ map TỪ bảng rose gốc).
PALETTE = {"kynang": "sp", "baocao": "tc"}

# Khuôn MẶC ĐỊNH khi không nêu --goc. Số câu = số reveal = số .slide-element phải dựng.
# ⚠️ Engine KHÔNG ép khuôn nào cả — nó chỉ ép `số câu dòng N == số .slide-element
# slide N` (auto_render.py:951). Khuôn cứng là ta TỰ TRÓI để tái dùng deck. Nêu --goc
# thì nhịp lấy từ `video/goc/<loai>/<ma>.md`, mỗi bài một nhịp khác nhau.
KHUON = {
    "kynang": [1, 3, 3, 2, 3, 3, 3, 3, 3, 3],   # 27 reveal
    "baocao": [1, 2, 3, 3, 3, 3, 2, 2, 3, 3],   # 25 reveal
}
GOC_DIR = {"baocao": VIDEO_DIR / "goc" / "taichinh",
           "kynang": VIDEO_DIR / "goc" / "kynang"}

# ═══════════════════ ĐƯỜNG RẺ (BOSS lệnh 25/07/2026) ═══════════════════
# BOSS hỏi "quy trình chuẩn rồi, render cũng nhanh, sao tổng thể tốn thời gian thế?".
# Đo thật: render KHÔNG tốn (186,9s máy chạy, 0 token). Tốn nằm ở 3 luật TA TỰ ĐẶT:
#   b1  spawn subagent Opus NGUỘI viết kịch bản, đề bài bảo "tự tra tài liệu trong repo"
#       ⇒ nó đọc lại từ đầu đúng những thứ phiên chính đang có sẵn trong ngữ cảnh.
#   b2  spawn Sonnet nguội + bắt ĐẺ ≥1 SCENE MỚI + tra catalogue BẰNG ẢNH (12 MB/18 ảnh)
#       ⇒ scene mới chưa ai test, hay vỡ safezone / sai nghĩa màu ⇒ đẻ thêm vòng vá.
#   b7  `Read` 10 PNG × 2-3 vòng = 20-30 lượt đọc ảnh (kho 1 bài 7,8 MB).
#
# `--duong re` đảo lại cả ba: thợ 1 (phiên chính) tự viết · chép deck ĐÃ GỠ LỖI và CHỈ
# THAY CHỮ · soi bằng contact sheet (LƯỚT 1 tấm → ZOOM slide đáng ngờ).
#
# 🔴 Đường rẻ KHÔNG cắt 3 cổng chặn: thước kịch bản (b3) · validate (b6) · soi ảnh (b7).
#    Nó chỉ đổi AI LÀM và THỨ TỰ SOI. Cắt cổng là mất khâu bắt lỗi, không phải tiết kiệm.
#
# Đánh đổi: đường rẻ KHÔNG đẻ scene mới ⇒ kho scene không lớn thêm, bài trùng nhịp bài cũ.
# ⇒ Bài MỞ ĐƯỜNG (mã mới, góc mới) vẫn nên đi `mo-duong`. Bài LÀM LẠI / gấp thì đi `re`.
#
# Deck đã ra video thật + đã gỡ hết lỗi soi ảnh — đường rẻ chỉ chép từ danh sách này.
# Thêm deck mới vào đây SAU KHI nó ra mp4 nghiệm thu đạt, đừng thêm deck chưa chạy.
DECK_DA_GO_LOI = {
    "baocao": ["deck_pnj02", "deck_msr01", "deck_hpd01", "deck_pnj01"],
    "kynang": ["deck_sp04", "deck_sp03", "deck_sp02", "deck_sp01"],
}

# `goc/` = KỂ CHUYỆN GÌ (ra nhịp).  `nghe/` = GIỮ MẮT BẰNG CÁCH NÀO (ra kiểu hook +
# 4 luật chung). Hai trục ĐỘC LẬP: cùng một góc vẫn mở được bằng 4-5 kiểu hook khác nhau.
NGHE_DIR = VIDEO_DIR / "nghe"
HOOK_CAM_TAICHINH = ("dung_lam", "cai_gia")   # khuyến nghị / dọa dẫm đội lốt

CLAUDE_TK2 = "/Users/simple/.claude-tk2"

# Chuỗi báo hết quota trong log CLI. Bắt hụt thì runner tưởng thợ làm xong mà file
# rỗng ⇒ luôn kiểm cả "file có ra không", đừng chỉ tin exit code.
# Mã 50 = KHOÁ RENDER đang bị tiến trình khác giữ (video/khoa_render.py). KHÔNG phải
# render hỏng — báo nhầm hai cái này là lần sau có người đi sửa deck trong khi lỗi thật
# chỉ là "đợi 3 phút". Đặt riêng để runner nói đúng bệnh.
MA_BI_KHOA = 50


def bao_bi_khoa(ten_buoc: str) -> int:
    noi(f"\n🔒 {ten_buoc} BỊ CHẶN — tiến trình khác đang quay/render.")
    noi("   Deck KHÔNG hỏng, kịch bản KHÔNG sai. Chỉ là đang xếp hàng.")
    noi("   Xem ai giữ : python3 video/khoa_render.py --kiem")
    noi("   Chạy lại   : thêm --tu-buoc <bước này> khi khoá rảnh")
    return MA_BI_KHOA


DAU_HET_QUOTA = (
    "usage limit", "rate limit", "quota", "exceeded your",
    "upgrade to", "try again later", "credit balance",
)


# ───────────────────────────── tiện ích ─────────────────────────────

def noi(*a):
    print(*a, flush=True)


def doc_goc(loai, ma_goc):
    """Đọc file góc → (nhịp, tên, toàn văn). Góc quyết định NHỊP KỂ của bài."""
    f = GOC_DIR[loai] / f"{ma_goc}.md"
    if not f.is_file():
        co = sorted(p.stem for p in GOC_DIR[loai].glob("*.md"))
        noi(f"❌ Không có góc '{ma_goc}' cho loại {loai}. Đang có: {', '.join(co) or '(rỗng)'}")
        return None
    txt = f.read_text(encoding="utf-8")
    m = re.search(r"^nhip:\s*\[([\d,\s]+)\]", txt, re.M)
    if not m:
        noi(f"❌ File góc {f} thiếu dòng `nhip: [...]`")
        return None
    ten = re.search(r"^ten:\s*(.+)$", txt, re.M)
    return ([int(x) for x in m.group(1).split(",")],
            ten.group(1).strip() if ten else ma_goc, txt)


def doc_hook(loai, ma_hook):
    """Đọc khối kiểu hook trong nghe/KIEU_HOOK.md → (tên, toàn văn khối).

    Danh sách mã đọc TỪ FILE, không hardcode ở đây — thêm kiểu hook thì sửa 1 chỗ.
    """
    f = NGHE_DIR / "KIEU_HOOK.md"
    if not f.is_file():
        noi(f"❌ Không thấy {f} — thư viện nghề giữ mắt chưa dựng?")
        return None
    txt = f.read_text(encoding="utf-8")
    # mã lấy từ tiêu đề khối:  ## `mat_mat` — MẤT MÁT
    khoi = re.findall(r"^##\s+`([a-z0-9_]+)`\s+—\s+(.+?)$", txt, re.M)
    co = [m for m, _ in khoi]
    if ma_hook not in co:
        noi(f"❌ Không có kiểu hook '{ma_hook}'. Đang có: {', '.join(co)}")
        return None
    if loai == "baocao" and ma_hook in HOOK_CAM_TAICHINH:
        noi(f"❌ Kiểu hook '{ma_hook}' CẤM cho bài tài chính (khuyến nghị/dọa dẫm đội lốt).")
        return None
    # cắt đúng khối của mã này: từ tiêu đề tới tiêu đề `## ` kế tiếp
    m = re.search(r"^##\s+`%s`\s+—.*?(?=^##\s+`|\Z)" % re.escape(ma_hook), txt, re.M | re.S)
    ten = dict(khoi)[ma_hook]
    return ten.strip(), m.group(0).strip()


def nhip_cua(a):
    """Nhịp đang áp dụng: của góc nếu có, không thì khuôn mặc định của loại."""
    return a.goc_nhip if a.goc_nhip else KHUON[a.loai]


def dem_reveal(deck: Path):
    """Đếm số .slide-element từng slide trong index.html. Trả [] nếu chưa có file.

    Đây là ràng buộc DUY NHẤT engine thật sự ép (auto_render.py:951):
    số câu dòng N phải bằng số .slide-element slide N.
    """
    f = deck / "index.html"
    if not f.is_file():
        return []
    # Bỏ BÌNH LUẬN trước rồi mới đếm, và chỉ đếm trong thuộc tính class.
    # Đếm chuỗi thô là sai: một dòng `<!-- ... KHÔNG phải .slide-element ... -->`
    # cũng bị tính thành 1 reveal (dính thật 25/07 khi thêm dòng miễn trừ).
    s = re.sub(r"<!--.*?-->", "", f.read_text(encoding="utf-8"), flags=re.S)
    return [len(re.findall(r'class="[^"]*\bslide-element\b[^"]*"', p))
            for p in re.split(r'<div class="slide[ "]', s)[1:]]


def bang_remap(palette):
    """Đọc NGUON + DICH[palette] THẲNG TỪ remap_palette.py — một nguồn sự thật.

    Chép lại bảng màu sang đây là chắc chắn lệch: bảng kia sửa thì chỗ này quên.
    """
    f = ESC / "remap_palette.py"
    if not f.is_file():
        return None
    s = f.read_text(encoding="utf-8")
    try:
        nguon = ast.literal_eval(re.search(r"^NGUON\s*=\s*(\[.*?\])", s, re.S | re.M).group(1))
        dich = ast.literal_eval(re.search(r"^DICH\s*=\s*(\{.*?^\})", s, re.S | re.M).group(1))
    except (AttributeError, ValueError, SyntaxError):
        return None
    return (nguon, dich.get(palette)) if dich.get(palette) else None


def con_mau_can_doi(deck: Path, palette) -> int:
    """Đếm mã màu CÒN PHẢI ĐỔI trong style.css. 0 ⇒ deck đã đúng palette, remap là thừa.

    Hai bẫy đã đo 25/07:
      · Tin dấu `_DA_REMAP` là vô dụng — KHÔNG deck nào có dấu đó (đều dựng trước runner).
      · Đếm cả 8 mã NGUON cũng sai: bảng `tc` map `#34d399` VỀ CHÍNH NÓ (success giữ xanh
        lục cố ý) ⇒ deck đã đổi xong vẫn còn 7 lần `#34d399`, tưởng là chưa đổi.
    ⇒ Chỉ đếm những mã nguồn có ĐÍCH KHÁC CHÍNH NÓ.
    """
    b = bang_remap(palette)
    f = deck / "style.css"
    if not b or not f.is_file():
        return -1          # không biết ⇒ cứ để bước 5 chạy remap như cũ
    nguon, dich = b
    s = f.read_text(encoding="utf-8").lower()
    return sum(s.count(a.lower()) for a, d in zip(nguon, dich) if a.lower() != d.lower())


def mau_khop_nhip(loai, nhip):
    """Các deck ĐÃ GỠ LỖI có nhịp reveal trùng `nhip` — ứng viên cho đường rẻ."""
    ra = []
    for ten in DECK_DA_GO_LOI.get(loai, []):
        d = HEADLESS / ten
        if d.is_dir() and dem_reveal(d) == list(nhip):
            ra.append(ten)
    return ra


def buoc(n, ten, loai):
    noi(f"\n{'─' * 72}\n▶ BƯỚC {n} [{loai}] {ten}\n{'─' * 72}")


def chay(cmd, cwd=None, timeout=1800):
    """Chạy lệnh máy. In thẳng ra để BOSS thấy tiến độ. Trả (ma, log)."""
    noi("  $ " + " ".join(str(c) for c in cmd))
    p = subprocess.run([str(c) for c in cmd], cwd=str(cwd or ESC),
                       capture_output=True, text=True, timeout=timeout)
    log = (p.stdout or "") + (p.stderr or "")
    for d in log.splitlines():
        noi("    " + d)
    return p.returncode, log


# ───────────────────────────── gọi thợ 2 ─────────────────────────────

def goi_tho2(de_bai: str, model: str, timeout=2400):
    """Gọi tài khoản Claude thứ 2 qua CLI.

    model: 'opus' cho việc SÁNG TẠO (kịch bản — quyết định chất lượng cả bài),
           'sonnet' cho việc CƠ KHÍ có khuôn sẵn (thay chữ trong index.html).
    Trả ('XONG'|'HET_QUOTA'|'HONG', log).

    ⚠️ acceptEdits cho GHI FILE nhưng KHÔNG cho chạy bash (trả giá 25/07). Runner
    tự chạy mọi lệnh, nên thợ 2 chỉ cần quyền ghi ⇒ acceptEdits là đủ và an toàn hơn.
    """
    if not Path(CLAUDE_TK2).is_dir():
        return "HONG", f"Không thấy CLAUDE_CONFIG_DIR của thợ 2: {CLAUDE_TK2}"

    env = dict(os.environ, CLAUDE_CONFIG_DIR=CLAUDE_TK2)
    cmd = ["claude", "-p", "--model", model,
           "--permission-mode", "acceptEdits", de_bai]
    noi(f"  → giao THỢ 2 (model={model}), chờ tối đa {timeout // 60} phút…")
    t0 = time.time()
    try:
        p = subprocess.run(cmd, cwd=str(VIDEO_DIR.parent), env=env,
                           capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return "HONG", "thợ 2 quá giờ"
    except FileNotFoundError:
        return "HONG", "không thấy lệnh `claude` trong PATH"

    log = (p.stdout or "") + (p.stderr or "")
    noi(f"  ← thợ 2 xong sau {time.time() - t0:.0f}s (mã {p.returncode})")
    thap = log.lower()
    if any(d in thap for d in DAU_HET_QUOTA):
        return "HET_QUOTA", log
    if p.returncode != 0:
        return "HONG", log
    return "XONG", log


def ban_giao_tho1(deck: Path, tieu_de: str, de_bai: str, ly_do: str, a=None):
    """Thợ 2 không làm được (HOẶC đường rẻ cố ý không gọi) ⇒ ghi brief ra file cho
    THỢ 1 (phiên đang chạy) tiếp quản.

    Không đổi sang API free: việc này cần TAY trên máy này (sửa file thật), mà
    Gemini/Groq/Antigravity đều không có tay.
    """
    # Lệnh chạy tiếp phải mang ĐỦ cờ, nếu không lần sau chạy nhầm sang đường mặc định
    # ⇒ b2 lại spawn thợ 2 và đòi đẻ scene mới, đúng thứ đường rẻ tránh.
    co = ""
    if a is not None:
        for ten, gt, mac_dinh in (("--ten", a.ten, a.ma), ("--loai", a.loai, "kynang"),
                                  ("--goc", a.goc, ""), ("--nghe", a.hook, ""),
                                  ("--duong", a.duong, "mo-duong")):
            if gt and gt != mac_dinh:
                co += f" {ten} {gt}"
    f = deck / "_VIEC_CHO_THO1.md"
    f.write_text(
        f"# VIỆC BÀN GIAO CHO THỢ 1 — {tieu_de}\n\n"
        f"**Vì sao bàn giao:** {ly_do}\n\n"
        f"Làm xong việc dưới đây rồi chạy tiếp:\n\n"
        f"```bash\npython3 video/lam_bai.py --ma {deck.name.replace('deck_', '')}"
        f"{co} --tu-buoc <bước kế>\n```\n\n---\n\n{de_bai}\n",
        encoding="utf-8")
    noi(f"\n🟡 ĐÃ BÀN GIAO THỢ 1 → {f}")
    noi(f"   Lý do: {ly_do}")
    return 20


# ───────────────────────────── các bước ─────────────────────────────

def b1_kichban(a, deck: Path) -> int:
    buoc(1, "VIẾT KỊCH BẢN 10 DÒNG", "THỢ")
    script = deck / "script-90s.txt"
    if script.exists() and script.read_text("utf-8").strip() and not a.lam_lai:
        noi("  ✓ đã có script-90s.txt — bỏ qua (thêm --lam-lai để viết lại)")
        return 0

    khuon = nhip_cua(a)
    nguon = f"Tài liệu nguồn: {a.nguon}" if a.nguon else "Tự tra tài liệu trong repo."
    phan_goc = ""
    if a.goc_van:
        phan_goc = (
            f"\n════════ GÓC TIẾP CẬN BẮT BUỘC: {a.goc_ten} ════════\n"
            "Viết ĐÚNG theo góc dưới đây — nhịp kể từng dòng, cách mở 11 từ đầu, và\n"
            "bẫy phải tránh đều nằm trong đó. Góc quyết định bài này KHÁC các bài trước.\n\n"
            f"{a.goc_van}\n"
            "════════ hết phần góc ════════\n")

    phan_nghe = ""
    if a.hook_van:
        phan_nghe = (
            f"\n════════ NGHỀ GIỮ MẮT — KIỂU HOOK BẮT BUỘC: {a.hook_ten} ════════\n"
            "ĐỌC 3 file này TRƯỚC KHI VIẾT, đừng viết theo trí nhớ:\n"
            f"  {NGHE_DIR}/DUONG_CONG.md   (hai mốc rơi thật: mở nợ dòng 2, trả nợ dòng 3-7)\n"
            f"  {NGHE_DIR}/CO_CHIA_SE.md   (câu đáng chụp màn hình)\n"
            f"  {NGHE_DIR}/TRAN_Y.md       (một bài một ý)\n\n"
            "BỐN VIỆC BẮT BUỘC — thước `thuoc_nghe.py` đo được cả bốn:\n"
            f"  1. Mở bài ĐÚNG kiểu hook dưới đây (11 TỪ đầu, nhịp đọc 3,56 từ/giây).\n"
            "  2. DÒNG 2 mở một MÓN NỢ (câu hỏi / nghịch lý / số chưa giải thích) và\n"
            "     KHÔNG giải thích ngay. Dòng 2 CẤM là lời hứa ('bài này sẽ giúp bạn').\n"
            "  3. TRẢ món nợ ở dòng 3-7, dùng lại ÍT NHẤT 2 TỪ NỘI DUNG của dòng 2.\n"
            "     Và DÒNG 5 hoặc 6 phải có SỐ (đó là chỗ đỡ mốc rơi giây 45-60).\n"
            "  4. MỘT câu đáng chụp màn hình ở dòng 3 hoặc dòng 10: ≤14 từ, không thuật\n"
            "     ngữ, có cặp đối hoặc có số, không hứa hẹn gì.\n\n"
            f"{a.hook_van}\n\n"
            f"GHI THÊM file {deck / '_NGHE.md'} với ĐÚNG 3 dòng máy đọc được này:\n"
            f"  NGHE: hook={a.hook} | mo=2 | tra=<3-7> | chia_se=<3 hoặc 10> | y_moi=1\n"
            "  CAU_CHIA_SE: <nguyên văn câu đó, phải CÓ THẬT trong dòng đã khai>\n"
            "  Y_MOI: <ý mới duy nhất của bài, một câu>\n"
            "Thiếu file này là bước 3 chặn.\n"
            "════════ hết phần nghề giữ mắt ════════\n")

    de_bai = f"""Viết kịch bản video dọc 9:16 tiếng Việt, ghi ra ĐÚNG file:
{script}

{nguon}
Chủ đề bài: {a.ten}
{phan_goc}{phan_nghe}
LUẬT CỨNG (sai một điều là cả bài phải làm lại):
- ĐÚNG {len(khuon)} dòng, mỗi dòng = 1 slide, không dòng trống, không đánh số, không tiêu đề.
- Số câu mỗi dòng phải ĐÚNG: {khuon} (tách câu theo . ? !). Đây là số reveal.
- CẤM ký tự gạch dài "—" (TTS đọc xấu, thước sẽ chặn).
- Viết cho TAI nghe, không cho mắt đọc: câu ngắn, không ngoặc đơn, không viết tắt,
  số phải viết cách đọc được.
- Đọc trước file khuôn: {VIDEO_DIR}/.claude/skills/video-{a.loai}/SKILL.md
  (mục công thức 7 nhịp: cảnh đời thường trước, ẩn dụ sờ được trước tên kỹ thuật,
  ví dụ THẬT có số, đi chậm qua 1 lần chạy thử, câu chốt đối xứng).
- Ẩn dụ xuyên suốt cả bộ: "người thợ mới mỗi sáng". ĐỪNG đổi ẩn dụ.
- Nhịp đọc đo thật: 3,56 từ/giây. Bài 100-165 giây là bình thường, đừng ép ngắn.

Chỉ ghi file, KHÔNG chạy lệnh nào."""

    if a.duong == "re":
        de_bai += f"""

════════ ĐƯỜNG RẺ — THỢ 1 TỰ VIẾT, KHÔNG SPAWN AI KHÁC ════════
Số liệu của bài này ĐANG NẰM SẴN trong ngữ cảnh phiên chính. Spawn một agent nguội
để nó đọc lại từ đầu là trả tiền hai lần cho cùng một thứ.

⭐ NHỊP LÀ RÀNG BUỘC CỨNG, KHÔNG PHẢI GỢI Ý: deck `{deck.name}` đã có sẵn
{dem_reveal(deck)} thẻ .slide-element. **Viết lời VỪA nhịp đó** — đừng viết theo ý rồi
định bẻ deck cho vừa, bẻ deck là quay lại đường đắt.

Viết xong chạy NGAY (trước khi làm gì khác):
  cd {VIDEO_DIR}
  python3 .claude/skills/video-{a.loai}/thuoc/thuoc_kichban.py \\
      {script}{f' --goc {a.goc}' if a.goc else ''}
Phải ra DAT rồi mới sang bước 2.
════════ hết phần đường rẻ ════════"""
        return ban_giao_tho1(deck, "Viết kịch bản 10 dòng", de_bai,
                             "ĐƯỜNG RẺ (--duong re) — cố ý KHÔNG spawn thợ 2, "
                             "phiên chính tự viết vì đã có sẵn số liệu trong ngữ cảnh", a)

    tt, log = goi_tho2(de_bai, "opus")
    if tt != "XONG" or not (script.exists() and script.read_text("utf-8").strip()):
        return ban_giao_tho1(deck, "Viết kịch bản 10 dòng", de_bai,
                             f"thợ 2 {tt} ({log.strip().splitlines()[-1][:120] if log.strip() else 'không rõ'})", a)
    noi("  ✓ thợ 2 đã ghi script-90s.txt")
    return 0


def b2_deck(a, deck: Path) -> int:
    buoc(2, "DỰNG DECK (thay chữ" + (")" if a.duong == "re" else " + THAY SCENE)"), "THỢ")
    if (deck / "_DA_SUA_HTML").exists() and not a.lam_lai:
        noi("  ✓ deck đã sửa — bỏ qua")
        return 0

    if a.duong == "re":
        return b2_deck_re(a, deck)

    ban_do = ""
    if a.goc_van:
        ban_do = (
            f"\n════════ GÓC: {a.goc_ten} — có BẢN ĐỒ SCENE riêng ════════\n"
            "Dùng đúng bản đồ scene trong phần dưới. Góc chọn hình theo VAI của từng\n"
            "dòng, đó là thứ làm bài này khác bài trước — đừng bê nguyên scene bài cũ.\n\n"
            f"{a.goc_van}\n"
            "════════ hết phần góc ════════\n")

    de_bai = f"""Sửa deck slide tại: {deck}

Nguồn lời: {deck}/script-90s.txt ({len(nhip_cua(a))} dòng, mỗi dòng 1 slide).
{ban_do}

VIỆC:
1. Sửa {deck}/index.html: thay toàn bộ chữ trên slide cho khớp lời từng dòng.
   Số thẻ .slide-element trong mỗi slide phải ĐÚNG bằng số câu của dòng đó.
2. THAY SCENE cho khác bài trước. Mở catalogue TRA BẰNG ẢNH trước khi chọn:
   {ESC}/docs/CATALOGUE_SCENE.md và ảnh {ESC}/docs/assets/catalogue/slideN.png
   Lấy DOM + CSS từ {ESC}/template/visual-pattern-gallery/
   Mẫu CHƯA dùng lần nào (ưu tiên lấy): speed-gauge, và 4 hero.
3. Đổi <title>, <meta>, và CẢ HAI chuỗi ?v= (ép trình duyệt nạp lại).
4. Chữ tiếng Việt DÀI HƠN nhãn mẫu ⇒ mẫu gallery hay tràn safezone.
   Safezone: padding 100px 28px 200px trên khung 390x693. Nửa dưới để phụ đề.
   Tính trước 2-3 vòng siết cỡ chữ, đó là bình thường không phải hỏng.
5. Hai slide liền nhau KHÔNG được cùng một dạng hộp.
6. ⭐ KỶ LUẬT KHO: bài nào cũng phải ĐẺ RA ÍT NHẤT 1 SCENE MỚI (tự dựng bằng HTML/CSS,
   không có sẵn trong kho). Kho escbase chỉ còn 5 mẫu chưa đụng — không tự đẻ thì cạn.
   Danh sách scene đang được đặt hàng: {VIDEO_DIR}/goc/NHAT_KY.md
   Đẻ xong ghi tên scene mới vào cuối {deck}/_DA_SUA_HTML.
7. Xong thì tạo file {deck}/_DA_SUA_HTML (ghi tên scene mới đã đẻ vào trong).

CSS của phần lớn mẫu ĐÃ CÓ SẴN trong style.css — kiểm trước, đừng chép đè cả khối.
Chép thêm thì đặt CUỐI FILE (style.css có 4 khối :root chồng nhau).

Chỉ sửa file, KHÔNG chạy lệnh nào — runner tự chạy thước và chụp ảnh."""

    tt, log = goi_tho2(de_bai, "sonnet")
    if tt != "XONG" or not (deck / "_DA_SUA_HTML").exists():
        return ban_giao_tho1(deck, "Dựng deck: thay chữ + thay scene", de_bai,
                             f"thợ 2 {tt}", a)
    noi("  ✓ thợ 2 đã sửa index.html")
    return 0


def b2_deck_re(a, deck: Path) -> int:
    """ĐƯỜNG RẺ: chép deck đã gỡ lỗi, CHỈ THAY CHỮ. Không catalogue ảnh, không scene mới.

    Bảng class mang MÀU/NGHĨA dưới đây là thứ đắt nhất của skill — mỗi dòng là một lỗi
    đã trả giá bằng một vòng soi ảnh. Nhét thẳng vào brief để thợ 1 chặn TRƯỚC khi chụp,
    thay vì soi ảnh xong mới phát hiện.
    """
    de_bai = f"""Sửa deck slide tại: {deck}

Nguồn lời: {deck}/script-90s.txt ({len(nhip_cua(a))} dòng, mỗi dòng 1 slide).
Deck này chép từ `{a.mau}` — deck ĐÃ RA VIDEO THẬT và đã gỡ hết lỗi soi ảnh.

════════ ĐƯỜNG RẺ — CHỈ THAY CHỮ ════════
KHÔNG đẻ scene mới. KHÔNG mở catalogue ảnh. KHÔNG đổi cấu trúc scene.
Lý do: scene mới là HTML/CSS chưa ai test ⇒ hay vỡ safezone hoặc sai nghĩa màu ⇒ đẻ
thêm vòng vá, mà mỗi vòng vá là một lượt chụp + soi lại. Deck cũ đã trả giá đó rồi.
(Muốn kho scene lớn thêm thì chạy bài đó bằng `--duong mo-duong`.)

VIỆC — đúng 3 thứ:
1. Sửa {deck}/index.html: thay chữ từng slide cho khớp lời dòng tương ứng.
   🔴 GIỮ NGUYÊN số thẻ .slide-element mỗi slide: {dem_reveal(deck)}
2. Đổi <title>, <meta name="description">, và CẢ HAI chuỗi ?v= (style.css và app.js)
   sang mã bài mới — không đổi thì trình duyệt nạp lại file cũ.
3. Xong thì tạo file rỗng {deck}/_DA_SUA_HTML

🔴 CHÉP DECK CŨ LÀ THỪA KẾ CẢ *NGHĨA* CỦA MÀU, KHÔNG CHỈ HÌNH.
Sau khi thay chữ, duyệt lại TỪNG class mang màu/nghĩa và hỏi "câu MỚI nằm trong đó có
đúng sắc thái đó không". Mỗi dòng dưới đây là một lỗi đã dính thật:

  hk-answer-no · hk-vs-old · sg-warn · hk-lockup-a  = ĐỎ, nghĩa "xấu / bị bác bỏ"
      → câu trung tính hoặc câu ĐÚNG mà bọc đỏ là màn hình nói ngược lời đọc.
      Ca PNJ 02: hk-lockup-a bọc câu dạy nghề đứng vững. Ca HPD: sg-warn bọc câu tích cực.
  hk-answer-ok · glowing-orb · core-module khi sáng  = XANH, nghĩa "tốt"
      → chỉ dùng khi lời đọc THẬT SỰ đang khen. glowing-orb kho là xanh lá, deck tài
      chính palette tc (vàng+đỏ) phải đổi sang rgba(255,176,32,…).
  hk-strike  = gạch ngang, nghĩa PHỦ ĐỊNH → ca MSR gạch ngang câu chốt ĐÚNG.
  core-module  = MẶC ĐỊNH TẮT ĐÈN (opacity .3 + grayscale) → ca PNJ 01 dùng để nói
      "những thứ KHÔNG đổi vẫn còn nguyên" ⇒ 3 ô mờ gần như vô hình, ngược hẳn lời đọc.
  sg-num  = huy hiệu 1 KÝ TỰ → nhét "KH 2026" vào là tràn chữ.
  cm-names-big code  = badge KEY NGẮN, 24px/900, monospace → nhét cả câu định nghĩa vào
      là vỡ 3-4 dòng chữ khổng lồ ăn hết slide. Câu thì cho vào <p class="cm-caption">.

⚠️ Bài tài chính BỊ CẤM kết luận đắt/rẻ ⇒ MÀU cũng không được kết luận hộ. Hai vế chỉ
để đặt cạnh nhau thì cho CÙNG MỘT MÀU trung tính; màu tương phản chỉ dùng khi lời đọc
thật sự đang phán một bên. Cần lớp trung tính thì chép mẫu `.vcl-flat` ở cuối
{HEADLESS}/deck_pnj02/style.css (đặt CUỐI FILE — style.css có 4 khối :root chồng nhau).

Chữ tiếng Việt dài hơn nhãn mẫu ⇒ tính trước 2-3 vòng siết cỡ chữ, đó là bình thường.
Safezone: padding 100px 28px 200px trên khung 390x693, nửa dưới để phụ đề.

Chỉ sửa file, KHÔNG chạy lệnh nào — runner tự chạy thước và chụp ảnh."""

    return ban_giao_tho1(deck, "Dựng deck ĐƯỜNG RẺ: chỉ thay chữ", de_bai,
                         "ĐƯỜNG RẺ (--duong re) — cố ý KHÔNG spawn thợ 2 và KHÔNG đẻ "
                         "scene mới; phiên chính đang giữ lời nên sửa HTML thẳng là rẻ nhất", a)


def b3_dongbo(a, deck: Path) -> int:
    buoc(3, "ĐỒNG BỘ LỜI VÀO 3 NƠI", "MÁY")
    ma, log = chay([PY, "sync_script.py", deck, deck / "script-90s.txt"])
    if ma != 0:
        noi("\n❌ sync_script FAIL — kịch bản sai khuôn. Sửa script-90s.txt rồi chạy lại.")
        return 10
    # sync_script in ra bảng "slide | số câu". Đối chiếu với KHUÔN ở đây, vì
    # sync_script KHÔNG biết khuôn — nó chỉ đếm. Lệch khuôn mà đi tiếp thì tới
    # bước render mới vỡ (validate_mapping), đã mất công sinh giọng.
    dem = [int(m.group(2)) for m in re.finditer(r"^\s*(\d+)\s*\|\s*(\d+)\s*$", log, re.M)]
    can = nhip_cua(a)
    if dem and dem != can:
        noi(f"\n❌ SỐ CÂU LỆCH KHUÔN\n   đang có: {dem}\n   cần    : {can}")
        noi("   Sửa script-90s.txt cho đúng số câu từng dòng rồi chạy lại bước 3.")
        return 10
    noi(f"  ✓ số câu khớp khuôn {can}")

    # Cổng NGHỀ GIỮ MẮT — chỉ bật khi nêu --nghe. Đặt Ở ĐÂY (không để tới bước 6) vì
    # sai kiểu hook / thiếu món nợ là phải VIẾT LẠI LỜI, mà bước 4 đã sinh giọng rồi.
    if a.hook:
        khai = deck / "_NGHE.md"
        if not khai.is_file():
            noi(f"\n❌ THIẾU KHAI BÁO NGHỀ GIỮ MẮT: không thấy {khai}")
            noi("   Thợ 2 phải ghi 3 dòng NGHE:/CAU_CHIA_SE:/Y_MOI: — xem video/nghe/README.md")
            return 10
        thuoc = (VIDEO_DIR / ".claude" / "skills" / "video-kynang"
                 / "thuoc" / "thuoc_nghe.py")
        lenh = ["python3", str(thuoc), str(deck / "script-90s.txt"), str(khai)]
        if a.loai == "baocao":
            lenh.append("--taichinh")
        ma, log = chay(lenh)
        if ma != 0:
            noi("\n❌ THƯỚC NGHỀ GIỮ MẮT FAIL — sửa lời + _NGHE.md rồi chạy lại bước 3.")
            noi("   Luật gốc: video/nghe/ · KHÔNG nới thước, nới là mất luôn khâu này.")
            return 10
        noi("  ✓ thước nghề giữ mắt DAT")
    return 0


def b4_giong(a, deck: Path) -> int:
    buoc(4, "SINH GIỌNG (edge NamMinh +14%)", "MÁY")
    engine, voice, rate = GIONG
    ma, _ = chay([PY, "generate_tts.py", deck,
                  "--engine", engine, "--voice", voice, "--rate", rate])
    if ma != 0:
        noi("\n❌ generate_tts FAIL. Endpoint edge-tts hay chập chờn — thử lại 1-2 lần.")
        return 1
    return 0


def b5_mau(a, deck: Path) -> int:
    buoc(5, "ĐỔI PALETTE THEO SERIES", "MÁY")
    if (deck / "_DA_REMAP").exists():
        noi("  ✓ đã remap rồi — BỎ QUA. Remap lần 2 sẽ ra DECK LAI MÀU mà vẫn báo thành công.")
        return 0
    ma, _ = chay([PY, "remap_palette.py", deck, PALETTE[a.loai]])
    if ma != 0:
        return 1
    (deck / "_DA_REMAP").touch()
    return 0


def b6_thuoc(a, deck: Path) -> int:
    buoc(6, "THƯỚC TỰ KIỂM (cổng chặn)", "MÁY")
    ma, log = chay([PY, "validate_slide.py", deck, "--semantic-report"])
    if ma != 0 or "PASS" not in log:
        noi("\n❌ THƯỚC FAIL — KHÔNG được đi tiếp. Thường là chữ tràn safezone.")
        noi("   Sửa index.html rồi: python3 video/lam_bai.py --ma {} --tu-buoc 6".format(a.ma))
        return 10
    noi("  ✓ PASS")

    # CỔNG MIỄN TRỪ — chỉ bài TÀI CHÍNH (BOSS lệnh 25/07/2026).
    # Vì sao là CỔNG chứ không phải lời nhắc trong SKILL: quên một dòng chữ thì video
    # vẫn render sạch, vẫn qua mọi phép đo khác, và chỉ phát hiện ra khi ĐÃ ĐĂNG.
    # Bối cảnh pháp lý: khoản 4 Điều 12 Luật Chứng khoán 2019 cấm cung cấp dịch vụ
    # chứng khoán khi chưa được cấp phép; UBCKNN cảnh báo 17/04/2026 nhắm vào tài khoản
    # mạng xã hội "đưa ra khuyến nghị mua, bán, nắm giữ cổ phiếu".
    # ⚠️ Dòng miễn trừ KHÔNG hợp pháp hoá nội dung khuyến nghị — nó chỉ nói rõ ý định.
    # Thứ thật sự bảo vệ là danh sách CAM_KHUYEN trong thuoc_kichban.py (chạy ở bước 3).
    if a.loai == "baocao":
        html = (deck / "index.html").read_text(encoding="utf-8")
        if "mien-tru" not in html:
            noi("\n❌ THIẾU DÒNG MIỄN TRỪ TRÁCH NHIỆM (bắt buộc với video tài chính).")
            noi("   Thêm vào CUỐI slide 10, NGOÀI .slide-content và KHÔNG mang class")
            noi("   .slide-element (để không tính là reveal, không đổi nhịp):")
            noi('     <p class="mien-tru">Video này không phải là khuyến nghị mua bán. '
                'Chỉ là tổng hợp thông tin.</p>')
            noi(f"   CSS `.mien-tru` chép từ cuối {HEADLESS}/deck_pnj02/style.css")
            return 10
        noi("  ✓ có dòng miễn trừ trách nhiệm")
    return 0


def b7_anh(a, deck: Path) -> int:
    buoc(7, "CHỤP SLIDE → THỢ 1 SOI MẮT (LƯỚT rồi ZOOM)", "BOSS/THỢ 1")
    out = Path("/tmp") / "escbase-qa" / deck.name
    ma, _ = chay([PY, "capture_slides.py", deck, "--out", out])
    if ma == MA_BI_KHOA:
        return bao_bi_khoa("CHỤP SLIDE")
    if ma != 0:
        return 1
    anh = sorted(out.glob("slide*.png"))

    # Contact sheet: ghép cả loạt thành 1 tấm. Ảnh là thứ đắt token nhất dây chuyền —
    # `Read` 10 file × 2-3 vòng vá = 20-30 lượt. Lướt 1 tấm bắt được gần hết lỗi
    # (chữ tràn, hộp lệch, màu mâu thuẫn nghĩa), rồi mới zoom slide đáng ngờ.
    # Đo thật PNJ 02: 2 lượt đọc ảnh, vẫn bắt được lỗi nghĩa. (BOSS lệnh 25/07)
    sheet = out / "_contact_sheet.png"
    ma_cs, _ = chay([PY, "contact_sheet.py", out])
    if ma_cs != 0 or not sheet.is_file():
        noi("  ⚠️ contact_sheet lỗi — quay về soi từng ảnh (không chặn bước).")
        sheet = None

    if a.bo_qua_soi:
        noi("\n  ⚠️ --bo-qua-soi: nhảy qua khâu soi. Thước và validate ĐỀU PASS mà màn hình")
        noi("     vẫn nói sai — đã dính 3 lần ở lượt 03→08. Chỉ dùng khi render lại y hệt.")
        return 0

    noi("\n🟡 DỪNG — THỢ 1 SOI MẮT. Thứ tự: LƯỚT cả loạt rồi mới ZOOM chỗ nghi ngờ.")
    if sheet:
        noi(f"\n   ① LƯỚT — `Read` ĐÚNG MỘT file này trước:\n      {sheet}")
        noi(f"   ② ZOOM — chỉ `Read` slide nào thấy nghi ở bước ①:\n      {out}/slideN.png")
        noi("      (đừng đọc cả 10 file khi tấm lướt không báo gì — đó là chỗ đốt token)")
    else:
        for p in anh:
            noi(f"    {p}")
    noi("\n   Soi 4 thứ: ① chữ có khớp lời dòng đó không  ② tràn/đè/ngắt dòng xấu")
    noi("   ③ MÀU có mâu thuẫn với NGHĨA của câu không (đỏ bọc câu đúng, xanh bọc câu xấu,")
    noi("      gạch ngang câu đúng, ô core-module tắt đèn khi lời đọc bảo 'còn nguyên')")
    noi("   ④ số trên màn hình có khớp số trong lời đọc không")
    noi(f"\n   Soi xong: python3 video/lam_bai.py --ma {a.ma} --tu-buoc 8"
        + (f" --duong {a.duong}" if a.duong == "re" else ""))
    return 30


def b8_render(a, deck: Path) -> int:
    buoc(8, "RENDER HEADLESS (~3 phút)", "MÁY")
    ma, _ = chay([PY, HEADLESS / "render_headless.py", deck], timeout=3600)
    if ma == MA_BI_KHOA:
        return bao_bi_khoa("RENDER")
    mp4 = deck / "output_headless" / "final_headless.mp4"
    if ma != 0 or not mp4.exists():
        noi("\n❌ render FAIL")
        return 1
    KETQUA.mkdir(parents=True, exist_ok=True)
    dich = KETQUA / f"{a.ma}_{a.ten}.mp4"
    shutil.copy2(mp4, dich)
    noi(f"  ✓ {dich}")
    return 0


def b9_nghiemthu(a, deck: Path) -> int:
    buoc(9, "NGHIỆM THU BẰNG MÁY (đừng tin exit code của render)", "MÁY")
    mp4 = KETQUA / f"{a.ma}_{a.ten}.mp4"
    giong = deck / "output" / "voiceover.mp3"
    cmd = [PY, THUOC_BAOCAO / "nghiem_thu_video.py", mp4]
    if giong.exists():
        cmd.append(giong)
    ma, log = chay(cmd)
    if ma != 0:
        noi("\n❌ CÓ PHÉP ĐO HỎNG — xem dấu ❌ ở trên. ĐỪNG báo BOSS là xong.")
        return 1
    noi("\n" + "=" * 72)
    noi(f"✅ XONG PHẦN MÁY: {mp4}")
    noi("🟡 CÒN LẠI LÀ VIỆC CỦA BOSS — máy không nghe được:")
    noi("   giọng có đọc sai dấu không · nhạc to/nhỏ · xem có mượt không · nội dung có hiểu được không")
    noi("=" * 72)
    return 40


BUOC = [b1_kichban, b2_deck, b3_dongbo, b4_giong, b5_mau, b6_thuoc, b7_anh,
        b8_render, b9_nghiemthu]


# ───────────────────────────── main ─────────────────────────────

def main() -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--ma", required=True, help="mã bài, vd sp09 / msr02")
    p.add_argument("--ten", default="", help="tên file ra, vd dieu_phoi")
    p.add_argument("--loai", choices=["kynang", "baocao"], default="kynang")
    p.add_argument("--nguon", default="", help="tài liệu nguồn cho kịch bản")
    p.add_argument("--goc", default="", help="mã góc tiếp cận (KỂ CHUYỆN GÌ) — video/goc/README.md")
    p.add_argument("--nghe", default="", dest="hook",
                   help="mã kiểu hook (GIỮ MẮT CÁCH NÀO) — video/nghe/KIEU_HOOK.md. "
                        "Nêu thì bật cổng thước nghề giữ mắt ở bước 3")
    p.add_argument("--mau", default="", help="deck mẫu để chép (mặc định deck_thu; "
                                             "đường rẻ tự chọn deck đã gỡ lỗi khớp nhịp)")
    p.add_argument("--duong", choices=["mo-duong", "re"], default="mo-duong",
                   help="mo-duong (mặc định): spawn thợ 2 + đẻ scene mới — cho mã/góc MỚI. "
                        "re: phiên chính tự viết, chép deck đã gỡ lỗi chỉ thay chữ, soi "
                        "bằng contact sheet — cho bài LÀM LẠI / bài gấp. Không cắt cổng chặn nào")
    p.add_argument("--tu-buoc", type=int, default=1, dest="tu_buoc")
    p.add_argument("--den-buoc", type=int, default=9, dest="den_buoc")
    p.add_argument("--lam-lai", action="store_true", dest="lam_lai",
                   help="làm lại cả bước THỢ dù đã có kết quả")
    p.add_argument("--bo-qua-soi", action="store_true", dest="bo_qua_soi")
    a = p.parse_args()
    a.ten = a.ten or a.ma
    a.goc_nhip = a.goc_ten = a.goc_van = None
    if a.goc:
        g = doc_goc(a.loai, a.goc)
        if not g:
            return 1
        a.goc_nhip, a.goc_ten, a.goc_van = g

    a.hook_ten = a.hook_van = None
    if a.hook:
        h = doc_hook(a.loai, a.hook)
        if not h:
            return 1
        a.hook_ten, a.hook_van = h

    if not PY.exists():
        noi(f"❌ Không thấy python của escbase: {PY}")
        return 1

    nhip = nhip_cua(a)
    khop = mau_khop_nhip(a.loai, nhip)

    # ĐƯỜNG RẺ: mẫu mặc định = deck ĐÃ GỠ LỖI có nhịp TRÙNG nhịp đang dùng.
    # Đây là chỗ đảo chiều: thay vì bẻ deck cho vừa lời, ta viết lời vừa deck sẵn có.
    if not a.mau:
        if a.duong == "re":
            if not khop:
                noi(f"❌ ĐƯỜNG RẺ KHÔNG CHẠY ĐƯỢC: nhịp {nhip} không trùng deck đã gỡ lỗi nào.")
                noi(f"   Deck đã gỡ lỗi ({a.loai}): {', '.join(DECK_DA_GO_LOI.get(a.loai, [])) or '(rỗng)'}")
                for t in DECK_DA_GO_LOI.get(a.loai, []):
                    if (HEADLESS / t).is_dir():
                        noi(f"     {t}: {dem_reveal(HEADLESS / t)}")
                noi("   Chọn 1 trong 3 cách:")
                noi("     ① đổi --goc sang góc có nhịp trùng một deck ở trên")
                noi("     ② sửa `nhip:` trong file góc cho khớp (nhịp là quy ước, engine không ép)")
                noi("     ③ đi --duong mo-duong: chấp nhận tốn hơn để dựng scene mới")
                return 1
            a.mau = khop[0]
        else:
            a.mau = "deck_thu"

    deck = HEADLESS / f"deck_{a.ma}"
    moi_chep = False
    if not deck.is_dir():
        mau = HEADLESS / a.mau
        if not mau.is_dir():
            noi(f"❌ Không thấy deck mẫu: {mau}")
            return 1
        if a.duong == "re" and dem_reveal(mau) != nhip:
            noi(f"❌ ĐƯỜNG RẺ: deck mẫu {mau.name} có nhịp {dem_reveal(mau)}, cần {nhip}.")
            noi(f"   Deck khớp nhịp: {', '.join(khop) or '(không có)'}")
            return 1
        noi(f"▶ chép deck mẫu {mau.name} → {deck.name}")
        shutil.copytree(mau, deck)
        moi_chep = True
        giu_remap = a.duong == "re" and con_mau_can_doi(mau, PALETTE[a.loai]) == 0
        don = ["output", "output_headless", "_DA_REMAP", "_DA_SUA_HTML"]
        if a.duong == "re":
            # Đường rẻ chép deck ĐÃ RA VIDEO ⇒ chép luôn LỜI của bài cũ. Không dọn thì
            # b1 thấy script-90s.txt có sẵn và bỏ qua ⇒ bài mới đi tiếp bằng lời bài cũ,
            # tới bước chụp ảnh mới lộ. (Bắt được lúc chạy thử chính nó, 25/07.)
            don += ["script-90s.txt", "_NGHE.md", "_VIEC_CHO_THO1.md"]
        for r in don:
            t = deck / r
            shutil.rmtree(t, ignore_errors=True) if t.is_dir() else t.unlink(missing_ok=True)
        # Mẫu đường rẻ cùng `loai` ⇒ cùng palette, đã remap rồi. Remap lần 2 chỉ map TỪ
        # bảng rose gốc mà bảng đó không còn ⇒ vô ích, và là chỗ đẻ ra deck lai màu.
        if giu_remap:
            (deck / "_DA_REMAP").touch()
            noi(f"  ✓ đường rẻ: mẫu còn 0 mã cần đổi ⇒ đã đúng palette "
                f"{PALETTE[a.loai]}, đặt dấu _DA_REMAP để bước 5 bỏ qua")

    # Cổng chặn đường rẻ: deck phải khớp nhịp ở MỌI lần chạy, không chỉ lúc chép.
    # Bắt sớm ở đây rẻ hơn nhiều so với vỡ ở bước render (đã sinh giọng, đã chụp ảnh).
    if a.duong == "re" and not moi_chep:
        dem = dem_reveal(deck)
        if dem and dem != nhip:
            noi(f"❌ ĐƯỜNG RẺ: deck {deck.name} có nhịp {dem}, nhưng nhịp đang dùng là {nhip}.")
            noi("   Đường rẻ = viết lời VỪA nhịp deck. Sửa lời, hoặc sửa `nhip:` trong file góc.")
            return 1

    noi(f"\n╔{'═' * 70}╗")
    noi(f"║ LÀM BÀI: {a.ma} ({a.loai})  ·  deck: {deck.name}")
    noi(f"║ góc : {a.goc_ten or 'KHÔNG NÊU → dùng khuôn cũ (mọi bài cùng một nhịp)'}")
    noi(f"║ hook: {a.hook_ten or 'KHÔNG NÊU → không có cổng nghề giữ mắt (bài dễ nhạt khúc giữa)'}")
    noi(f"║ nhịp: {nhip_cua(a)}  ·  {sum(nhip_cua(a))} reveal")
    noi("║ đường: " + ("RẺ — phiên chính tự viết · chép %s chỉ thay chữ · 0 scene mới · "
                       "soi contact sheet" % a.mau if a.duong == "re"
                       else "MỞ ĐƯỜNG — spawn thợ 2 (opus+sonnet) · đẻ ≥1 scene mới"))
    noi(f"║ bước {a.tu_buoc} → {a.den_buoc}  ·  giọng {GIONG[1]} {GIONG[2]}  ·  palette {PALETTE[a.loai]}")
    noi(f"╚{'═' * 70}╝")

    for i in range(a.tu_buoc, a.den_buoc + 1):
        ma = BUOC[i - 1](a, deck)
        if ma != 0:
            return ma
    return 0


if __name__ == "__main__":
    sys.exit(main())
