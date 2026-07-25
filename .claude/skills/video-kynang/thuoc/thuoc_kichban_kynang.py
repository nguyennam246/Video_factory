#!/usr/bin/env python3
"""THƯỚC KỊCH BẢN DẠY KỸ NĂNG — 0 API, tất định.

    python3 thuoc_kichban_kynang.py <file_loi.txt> [--thuatngu "skill,plugin,hook"]

Đo 10 thứ mà khuôn bài dạy BẮT BUỘC. In KETLUAN|<cau>|<tu>|DAT hoặc HONG ở dòng cuối.

Vì sao có thước này (đo thật, đừng đoán lại):
- Bài `superpowers_01` ra 93,3 giây với **332 từ** ⇒ nhịp đọc thật của giọng
  `edge:vi-VN-NamMinhNeural:+14%` là **~3,56 từ/giây**. Suy ra: 3 GIÂY ĐẦU chỉ đọc
  được **~11 từ**. Muốn "hấp dẫn ngay 3 giây đầu" thì cái mất mát phải nằm trong
  11 từ đầu tiên, không phải trong cả dòng hook.
- Bản nháp bài HPD viết "đúng ý" ra 521 từ, vượt trần 37%, siết 3 vòng mới về được.
  Đừng ước lượng độ dài bằng cảm giác.
- Bẫy đắt nhất của dự án: BOSS xem bản 1 bài Hook và KHÔNG HIỂU, vì tên kỹ thuật
  ném ra từ cảnh 4 trước khi có ẩn dụ sờ được. Thước này chặn đúng cái đó
  (`--thuatngu`, phép đo 8).
"""
import re
import sys

KHUON = [1, 3, 3, 2, 3, 3, 3, 3, 3, 3]   # 10 slide = 27 reveal (khuôn deck_sp01)
TRAN_TU = (330, 450)          # 93-127 giây ở nhịp 3,56 từ/giây
TRAN_HOOK = 18                # cả dòng 1
TRAN_3GIAY = 11               # 11 từ đầu = 3 giây đầu
TRAN_DONG = 55                # 1 dòng quá dài thì phụ đề tràn + slide nặng

# Mở bài yếu — cấm tuyệt đối ở dòng 1 (BOSS chốt: 3 giây đầu vào thẳng)
MO_YEU = [
    'hãy tưởng tượng', 'bạn có biết', 'trong bài này', 'hôm nay chúng ta',
    'chúng ta sẽ cùng', 'có một', 'nhiều người thường', 'như các bạn đã biết',
    'đầu tiên,', 'trước hết', 'xin chào',
]
# Chữ lập trình — người mới không hiểu, cấm trong CẢ BÀI (nói bằng chữ thường)
CAM_LAP_TRINH = [
    'stdin', 'stdout', 'json', 'api', 'cli', 'parse', 'config', 'deploy',
    'commit', 'repo', 'runtime', 'framework', 'backend', 'frontend',
    'exit code', 'stack trace', 'endpoint', 'schema',
]
# Chữ AI tự khen / chữ rỗng
CAM_RONG = [
    'mạnh mẽ', 'tuyệt vời', 'cực kỳ hữu ích', 'thay đổi cuộc chơi', 'đột phá',
    'không thể thiếu', 'siêu việt', 'thần thánh',
]
DUNG_TU = {'là', 'và', 'có', 'một', 'của', 'cho', 'thì', 'mà', 'không', 'bạn', 'nó',
           'các', 'những', 'này', 'đó', 'với', 'khi', 'nhưng', 'ở', 'trong', 'ra',
           'được', 'người', 'cái', 'lại', 'còn', 'sẽ', 'đã', 'rồi', 'chỉ', 'vào'}


def tach_cau(dong):
    return [s for s in re.split(r'(?<=[.?!])\s+', dong.strip()) if s.strip()]


def tu_noi_dung(text):
    return {w for w in re.findall(r'[^\W\d_]+', text.lower(), re.UNICODE)
            if w not in DUNG_TU and len(w) > 1}


def do(path, thuatngu):
    lines = [l for l in open(path, encoding='utf-8').read().split('\n') if l.strip()]
    cau = [len(tach_cau(l)) for l in lines]
    tu = [len(l.split()) for l in lines]
    full = '\n'.join(lines)
    low = full.lower()
    loi, canh = [], []

    # 1. đúng 10 dòng
    if len(lines) != 10:
        loi.append('SO_DONG: %d, phai la 10' % len(lines))
        return ket(loi, canh, sum(cau), sum(tu))

    # 2. số câu mỗi dòng khớp khuôn (= số reveal của deck_sp01)
    if cau != KHUON:
        loi.append('KHUON_CAU: %s, phai la %s' % (cau, KHUON))

    # 3. tổng từ trong trần
    tong = sum(tu)
    if not (TRAN_TU[0] <= tong <= TRAN_TU[1]):
        loi.append('TONG_TU: %d, phai trong %d-%d (~%.0f giay)'
                   % (tong, TRAN_TU[0], TRAN_TU[1], tong / 3.56))

    # 4. dòng nào quá dài
    for i, n in enumerate(tu, 1):
        if n > TRAN_DONG:
            loi.append('DONG_%d_DAI: %d tu, tran %d' % (i, n, TRAN_DONG))

    # 5. hook cả dòng
    if tu[0] > TRAN_HOOK:
        loi.append('HOOK_DAI: %d tu, tran %d' % (tu[0], TRAN_HOOK))

    # 6. 3 GIÂY ĐẦU — 11 từ đầu phải có danh từ cụ thể/số, không mở yếu
    ba_giay = ' '.join(lines[0].split()[:TRAN_3GIAY])
    for w in MO_YEU:
        if lines[0].lower().startswith(w) or w in lines[0].lower()[:60]:
            loi.append('MO_YEU: dong 1 chua "%s"' % w)
    if not re.search(r'\d', ba_giay) and len(tu_noi_dung(ba_giay)) < 4:
        canh.append('3GIAY_MO: 11 tu dau it danh tu cu the, kiem lai co "canh" chua')

    # 7. có ví dụ THẬT có số
    so = re.findall(r'\d+', full)
    so_chu = re.findall(r'(?:ngày thứ|lần thứ|một|hai|ba|bốn|năm|sáu|bảy|tám|chín|mười|'
                        r'hai mươi|ba mươi|trăm|nghìn|triệu|tỷ)\s', low)
    if not so and len(so_chu) < 3:
        loi.append('THIEU_SO: bai day phai co vi du THAT co so')

    # 8. ẨN DỤ TRƯỚC TÊN KỸ THUẬT — thuật ngữ cấm xuất hiện ở dòng 1-4
    for t in thuatngu:
        t = t.strip().lower()
        if not t:
            continue
        for i in range(4):
            if t in lines[i].lower():
                loi.append('THUATNGU_SOM: "%s" xuat hien o dong %d, phai tu dong 5'
                           % (t, i + 1))
                break

    # 9. câu chốt đối xứng — dòng 10 phải dội lại dòng 1
    chung = tu_noi_dung(lines[0]) & tu_noi_dung(lines[9])
    if len(chung) < 2:
        loi.append('KHONG_DOI_XUNG: dong 10 khong doi lai dong 1 (chung %d tu)'
                   % len(chung))

    # 10. dấu — và từ cấm
    if '—' in full:
        loi.append('DAU_GACH_DAI: TTS doc xau, bo het')
    hit = [w for w in CAM_LAP_TRINH + CAM_RONG if w in low]
    if hit:
        loi.append('TU_CAM: %s' % ', '.join(hit))

    return ket(loi, canh, sum(cau), tong)


def ket(loi, canh, cau, tu):
    for l in loi:
        print('LOI    | %s' % l)
    for c in canh:
        print('CANH   | %s' % c)
    if not loi and not canh:
        print('SACH   | khong loi, khong canh bao')
    print('KETLUAN|%d|%d|%s' % (cau, tu, 'HONG' if loi else 'DAT'))
    return 1 if loi else 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    tn = []
    if '--thuatngu' in sys.argv:
        tn = sys.argv[sys.argv.index('--thuatngu') + 1].split(',')
    sys.exit(do(sys.argv[1], tn))
