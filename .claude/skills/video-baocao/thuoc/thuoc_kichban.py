#!/usr/bin/env python3
"""THƯỚC KỊCH BẢN — 0 API, tất định. Chạy NGAY sau bản nháp đầu, trước khi dựng deck.

    python3 thuoc_kichban.py <đường_dẫn_file_lời.txt> [--goc <mã góc>]

Đo 6 thứ: số dòng · số câu mỗi dòng · tổng câu · tổng từ · độ dài hook · dấu — · từ cấm.
In KETLUAN|<câu>|<từ>|DAT hoặc HONG ở dòng cuối.

Vì sao có thước này: bản nháp bài HPD (24/07/2026) viết "đúng ý" ra 521 từ, vượt trần
380 tới 37%, phải siết 3 vòng. Số tiếng Việt viết ra chữ đội từ rất nhanh — một số như
"hai mươi bảy phẩy bảy tỷ" = 6 từ. Đừng ước lượng bằng cảm giác.

🆕 25/07/2026 — NHỊP LẤY TỪ GÓC, KHÔNG CÒN LÀ HẰNG SỐ.
Trước ngày này `KHUON` là hằng số cứng ⇒ MSR, HPD, TCL, SKV, MCF kể chuyện gì cũng
phải nhét vừa một cái khung, xem 3 bài liền là thấy "cùng một khuôn". Sự thật kỹ thuật:
engine chỉ ép `số câu dòng N == số .slide-element slide N` (auto_render.py:951), KHÔNG
ép khuôn nào cả. Nay `--goc nghich_ly_so` thì thước đọc `nhip:` trong
`video/goc/taichinh/nghich_ly_so.md`. Không truyền `--goc` thì quay về khuôn cũ.
"""
import re
import sys
from pathlib import Path

KHUON = [1, 2, 3, 3, 3, 3, 2, 2, 3, 3]   # khuôn tài chính cũ — dùng khi không nêu góc
GOC_DIR = Path(__file__).resolve().parents[4] / "goc" / "taichinh"


def doc_nhip(ma_goc):
    """Đọc `nhip:` trong header file góc. Trả (nhịp, tên). Không thấy thì thoát."""
    f = GOC_DIR / f"{ma_goc}.md"
    if not f.is_file():
        co = sorted(p.stem for p in GOC_DIR.glob("*.md"))
        print(f"❌ Không có góc '{ma_goc}'. Đang có: {', '.join(co) or '(rỗng)'}")
        sys.exit(2)
    txt = f.read_text(encoding="utf-8")
    m = re.search(r"^nhip:\s*\[([\d,\s]+)\]", txt, re.M)
    if not m:
        print(f"❌ File góc {f} thiếu dòng `nhip: [...]` trong header")
        sys.exit(2)
    ten = re.search(r"^ten:\s*(.+)$", txt, re.M)
    return [int(x) for x in m.group(1).split(",")], (ten.group(1).strip() if ten else ma_goc)
TRAN_TU = (300, 380)
TRAN_HOOK = 16

# (a) mã + ngôn ngữ hệ thống nội bộ — người xem không cần biết, BOSS cấm 24/07/2026
CAM_HE_THONG = [
    'hội tụ', '2/2', 'hai máy soi', 'máy độc lập', 'hai nhánh', 'hội đồng', 'quan tòa',
    'phán quyết', 'watchlist', 'chờ soi', 'tranh chấp', 'chữ ký mẫu', 'ngưỡng',
    'mô hình của chúng tôi', 'hệ thống chấm', 'AI soi', 'thuật toán', 'phễu',
    'lọc tử thần', 'Z-Score', 'M-Score', 'DuPont', 'Dickinson', 'percentile', 'RORE',
    'spread', 'nhóm II', 'nhóm III', 'nhóm IV', 'nhóm V',
]
# (c) ngôn ngữ dọa dẫm
CAM_DOA = ['sập', 'bốc hơi', 'mất trắng', 'thảm họa', 'bẫy chết người']
# (e) khuyến nghị mua bán dưới mọi hình thức
CAM_KHUYEN = ['nên mua', 'nên bán', 'tránh xa', 'đáng tiền', 'cơ hội', 'giá mục tiêu',
              'khuyến nghị', 'đáng mua', 'đáng đầu tư']
# lưu ý: "hội đồng quản trị" là danh từ THẬT của doanh nghiệp nhưng vẫn dính luật cấm
# "hội đồng" → viết vòng ("đại hội cổ đông cho phép…"), đừng xin miễn trừ.


def do(path, ma_goc=None):
    khuon, ten_goc = (doc_nhip(ma_goc) if ma_goc else (KHUON, 'khuôn cũ (không nêu góc)'))
    lines = [l for l in open(path, encoding='utf-8').read().split('\n') if l.strip()]
    cau = [len([s for s in re.split(r'(?<=[.?!])\s+', l.strip()) if s.strip()]) for l in lines]
    tu = [len(l.split()) for l in lines]
    full = '\n'.join(lines)
    low = full.lower()

    hit = [w for w in CAM_HE_THONG + CAM_DOA + CAM_KHUYEN if w.lower() in low]
    hit += [w for w in ['N%d' % i for i in range(1, 22)] + ['T%d' % i for i in range(1, 7)]
            if re.search(r'\b%s\b' % w, full)]

    hook_tu = len(lines[0].split()) if lines else 0
    loi = []
    if len(lines) != len(khuon):
        loi.append(f'phải đúng {len(khuon)} dòng (theo góc), đang {len(lines)}')
    if cau != khuon:
        loi.append(f'số câu/dòng phải {khuon}, đang {cau}')
    if not (TRAN_TU[0] <= sum(tu) <= TRAN_TU[1]):
        loi.append(f'tổng từ phải {TRAN_TU[0]}-{TRAN_TU[1]}, đang {sum(tu)}')
    if hook_tu > TRAN_HOOK:
        loi.append(f'hook phải ≤{TRAN_HOOK} từ, đang {hook_tu}')
    if '—' in full:
        loi.append('còn dấu — (máy đọc rất xấu), thay bằng dấu phẩy hoặc chấm')
    if hit:
        loi.append(f'TỪ CẤM: {hit}')

    print(f'GÓC: {ten_goc} | nhịp cần: {khuon}')
    print(f'dòng: {len(lines)} | câu/dòng: {cau} | tổng câu: {sum(cau)} | TỪ: {sum(tu)}')
    print(f'từ/dòng: {tu}')
    print(f'hook: {hook_tu} từ -> {lines[0] if lines else "(rỗng)"}')
    print(f'có dấu — : {"—" in full} | TỪ CẤM: {hit or "KHÔNG"}')
    if loi:
        print('\n❌ CHƯA ĐẠT:')
        for x in loi:
            print('  ·', x)
    else:
        print('\n✅ ĐẠT hết 6 thước.')
    print(f'\nKETLUAN|{sum(cau)}|{sum(tu)}|{"HONG" if loi else "DAT"}')
    return 1 if loi else 0


if __name__ == '__main__':
    args = sys.argv[1:]
    goc = None
    if '--goc' in args:
        i = args.index('--goc')
        if i + 1 >= len(args):
            print('❌ --goc thiếu giá trị')
            sys.exit(2)
        goc = args[i + 1]
        del args[i:i + 2]
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)
    sys.exit(do(args[0], goc))
