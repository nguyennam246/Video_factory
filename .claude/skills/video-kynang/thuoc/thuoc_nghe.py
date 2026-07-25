#!/usr/bin/env python3
"""THƯỚC NGHỀ GIỮ MẮT — 0 API, tất định. Luật gốc: `video/nghe/`.

Ba chế độ:

  # 1. đo KỊCH BẢN + khai báo NGHE trong README
  thuoc_nghe.py <loi.txt> <README_slug.md> [--thuatngu "skill,plugin"]

  # 2. đo TRÙNG SCENE giữa deck mới và deck liền trước
  thuoc_nghe.py --trung <deck_moi> <deck_truoc>

  # 3. tính lại MỐC RƠI cho một nhịp khác (khi góc đổi nhịp)
  thuoc_nghe.py --moc "1,3,3,2,3,3,3,3,3,3" [--tu 330,450]

Vì sao có thước này (đo thật 25/07/2026, đừng đoán lại):
- Dự án chặn rất chặt giây 0-3 rồi BỎ TRỐNG giây 3-70. Quy mốc rơi của video ngắn
  (giây 8-15 và 45-60) về khuôn `[1,3,3,2,3,3,3,3,3,3]` ở nhịp 3,56 từ/giây thì
  MỐC 1 nằm gọn trong DÒNG 2, MỐC 2 ở DÒNG 5-7 tâm DÒNG 6. Nên luật là:
  mở món nợ ở dòng 2, trả ở dòng 6.
- Dò 12 deck: sp03→sp08 (6 bài liền) dùng chung LÕI 4 mẫu scene, độ trùng với bài
  liền trước 80-88%, mỗi bài mới chỉ thêm ĐÚNG MỘT mẫu. Số mẫu/bài không thiếu
  (6-9) — cái sai là trùng với bài trước. sp05→sp06 đạt 57% ⇒ ngưỡng 60% làm được.
- 6 bài liền cùng kiểu hook `mat_mat` (kho có 10 kiểu, 9 kiểu chưa dùng lần nào).
"""
import re
import sys

NHIP_DOC = 3.56          # từ/giây, giọng edge:vi-VN-NamMinhNeural:+14%, đo 8 bài
MOC_ROI = [(8, 15), (45, 60)]

MA_HOOK = ['mat_mat', 'nghich_ly_so', 'phu_dinh', 'giua_hanh_dong', 'thu_nhan',
           'mot_moc', 'truoc_sau', 'cau_hoi_gai', 'dung_lam', 'cai_gia']
HOOK_CAM_TAICHINH = ['dung_lam', 'cai_gia']     # khuyến nghị / dọa dẫm đội lốt

# Dòng TRẢ NỢ: 3-7. Nới từ (5,7) sau khi đo bài sp02 (BOSS đã duyệt "video tốt"):
# bài đó trả nợ ở DÒNG 3 ("lỗi nằm ở chỗ cuốn sổ chưa được mang vào công trường") rồi dùng
# dòng 6 cho VÍ DỤ THẬT. Đó không phải lỗi của bài — là phép đo cũ gộp hai thứ khác nhau:
#   · "trả món nợ mở ở dòng 2"  → dùng lại chữ của dòng 2, có thể ở dòng 3
#   · "chỗ mạnh nhất đỡ mốc rơi 2 (giây 45-60)" → phải có SỐ ở dòng 5 hoặc 6
# Nay đo tách làm hai. Luật bị số đo sửa, không phải bài bị luật sửa.
TRA_HOP_LE = (3, 7)
DONG_MOC2 = (5, 6)       # dòng đỡ mốc rơi 2 — phải có ví dụ thật có số
CHIA_SE_HOP_LE = (3, 10)
TRAN_CAU_CHIA_SE = 14    # từ

# Lời hứa rỗng — dòng 2 mà chứa cái này thì đang HỨA chứ không MỞ NỢ
HUA_RONG = ['bài này sẽ', 'bạn sẽ học', 'chúng ta sẽ', 'tôi sẽ chỉ', 'sẽ giúp bạn',
            'hãy cùng', 'video này', 'rất quan trọng', 'vô cùng quan trọng']
CAM_RONG = ['mạnh mẽ', 'tuyệt vời', 'cực kỳ hữu ích', 'thay đổi cuộc chơi', 'đột phá',
            'không thể thiếu', 'siêu việt', 'thần thánh']

# Mẫu scene của template. `script-panel` là KHUNG chứa chữ, deck nào cũng có ⇒ KHÔNG đếm.
MAU_SCENE = ['mock-terminal', 'risk-cards-container', 'workflow-grid', 'flow-diagram',
             'core-module-grid', 'vpg-chat-message', 'glowing-conclusion', 'perf-compare',
             'speed-gauge', 'revenue-balance', 'cpu-chip', 'stream-visual',
             'vpg-traffic-pole', 'webui-frame', 'ask-github-mark', 'vpg-source-hero',
             'vpg-logo-hero']
NGUONG_TRUNG = 0.60     # trùng với bài liền trước
TOI_THIEU_MOI = 2       # số mẫu mới bắt buộc

DUNG_TU = {'là', 'và', 'có', 'một', 'của', 'cho', 'thì', 'mà', 'không', 'bạn', 'nó',
           'các', 'những', 'này', 'đó', 'với', 'khi', 'nhưng', 'ở', 'trong', 'ra',
           'được', 'người', 'cái', 'lại', 'còn', 'sẽ', 'đã', 'rồi', 'chỉ', 'vào'}


def tu_noi_dung(text):
    return {w for w in re.findall(r'[^\W\d_]+', text.lower(), re.UNICODE)
            if w not in DUNG_TU and len(w) > 1}


def ket(loi, canh):
    for l in loi:
        print('LOI    | %s' % l)
    for c in canh:
        print('CANH   | %s' % c)
    if not loi and not canh:
        print('SACH   | khong loi, khong canh bao')
    print('KETLUAN|%s' % ('HONG' if loi else 'DAT'))
    return 1 if loi else 0


# ─────────────────────────── chế độ 3: mốc rơi ───────────────────────────
def tinh_moc(nhip, tran_tu):
    """In bảng dòng → khoảng giây, và dòng nào chứa mốc rơi. Không phán DAT/HONG."""
    tong_cau = sum(nhip)
    print('nhip=%s  tong reveal=%d  nhip doc=%.2f tu/giay' % (nhip, tong_cau, NHIP_DOC))
    ket_qua = {}
    for tong_tu in tran_tu:
        print('\n=== bai %d tu = %.1f giay ===' % (tong_tu, tong_tu / NHIP_DOC))
        t, hit = 0.0, {i: [] for i, _ in enumerate(MOC_ROI)}
        for i, c in enumerate(nhip, 1):
            d = (tong_tu * c / tong_cau) / NHIP_DOC
            for k, (a, b) in enumerate(MOC_ROI):
                if t < b and t + d > a:
                    hit[k].append(i)
            print('  dong %2d (%d cau): giay %5.1f -> %5.1f' % (i, c, t, t + d))
            t += d
        ket_qua[tong_tu] = hit
    print('\n>>> MOC ROI roi vao dong nao:')
    for tong_tu, hit in ket_qua.items():
        for k, (a, b) in enumerate(MOC_ROI):
            print('  bai %d tu: moc giay %d-%d -> dong %s' % (tong_tu, a, b, hit[k]))
    print('\n=> LUAT: MO NO o dong dau cua moc 1 · TRA NO o dong tam cua moc 2.')
    return 0


# ─────────────────────── chế độ 2: trùng scene ───────────────────────
def doc_scene(deck):
    import pathlib
    p = pathlib.Path(deck)
    f = p / 'index.html' if p.is_dir() else p
    if not f.exists():
        sys.exit('❌ khong thay %s' % f)
    return f.read_text(encoding='utf-8', errors='ignore')


def do_trung(deck_moi, deck_truoc):
    loi, canh = [], []
    s_moi, s_truoc = doc_scene(deck_moi), doc_scene(deck_truoc)
    A = {m for m in MAU_SCENE if m in s_truoc}
    B = {m for m in MAU_SCENE if m in s_moi}
    print('deck truoc (%s): %d mau  %s' % (deck_truoc, len(A), ', '.join(sorted(A))))
    print('deck moi   (%s): %d mau  %s' % (deck_moi, len(B), ', '.join(sorted(B))))
    if not B:
        loi.append('DECK_MOI_KHONG_CO_SCENE: chi co khung script-panel, chua mo kho')
        return ket(loi, canh)

    trung, moi = A & B, B - A
    ti_le = len(trung) / len(B)
    print('\ntrung %d/%d = %.0f%%   moi: %s'
          % (len(trung), len(B), 100 * ti_le, ', '.join(sorted(moi)) or '(KHONG CO)'))
    if ti_le > NGUONG_TRUNG:
        loi.append('TRUNG_CAO: %.0f%% voi bai lien truoc, tran %.0f%% '
                   '(do that sp03-sp08: 80-88%% = "cung mot khuon")'
                   % (100 * ti_le, 100 * NGUONG_TRUNG))
    if len(moi) < TOI_THIEU_MOI:
        loi.append('IT_MAU_MOI: %d mau moi, toi thieu %d' % (len(moi), TOI_THIEU_MOI))

    # hai slide liền nhau cùng loại scene
    # ⚠️ Một slide dùng ĐƯỢC nhiều mẫu (deck sp07 slide 4 = flow-diagram + cpu-chip). Lấy
    # mẫu ĐẦU TIÊN theo thứ tự bảng rồi so là báo oan — slide 3 và 4 đều "flow-diagram"
    # trong khi slide 4 thật ra là scene cpu-chip. Nên so BỘ mẫu, chỉ kêu khi trùng HẾT.
    khoi = re.split(r'class="slide(?:\s+active)?"', s_moi)[1:]
    day = [frozenset(m for m in MAU_SCENE if m in k) for k in khoi]
    print('\nscene tung slide (%d slide): %s'
          % (len(day), ' · '.join('+'.join(sorted(x)) if x else '—' for x in day)))
    for i in range(len(day) - 1):
        if day[i] and day[i] == day[i + 1]:
            loi.append('SLIDE_LIEN_TRUNG: slide %d va %d dung y nguyen mot bo scene (%s)'
                       % (i + 1, i + 2, '+'.join(sorted(day[i]))))

    chua = [m for m in MAU_SCENE if m not in B]
    if chua:
        canh.append('MAU_CHUA_DUNG trong deck nay (%d): %s' % (len(chua), ', '.join(chua)))
    return ket(loi, canh)


# ──────────────── chế độ 1: kịch bản + khai báo NGHE ────────────────
def doc_khai_bao(path):
    """Đọc dòng NGHE: / CAU_CHIA_SE: / Y_MOI: trong README_{slug}.md."""
    txt = open(path, encoding='utf-8').read()
    kb = {'cau_chia_se': '', 'y_moi_text': ''}
    m = re.search(r'^\s*NGHE:\s*(.+)$', txt, re.M)
    if not m:
        return None, 'THIEU_KHAI_BAO: khong thay dong "NGHE: hook=... | mo=... | tra=... | chia_se=... | y_moi=..."'
    for phan in m.group(1).split('|'):
        if '=' in phan:
            k, v = phan.split('=', 1)
            kb[k.strip()] = v.strip()
    m = re.search(r'^\s*CAU_CHIA_SE:\s*(.+)$', txt, re.M)
    if m:
        kb['cau_chia_se'] = m.group(1).strip()
    m = re.search(r'^\s*Y_MOI:\s*(.+)$', txt, re.M)
    if m:
        kb['y_moi_text'] = m.group(1).strip()
    return kb, None


def do_kichban(path_loi, path_readme, thuatngu, taichinh):
    loi, canh = [], []
    lines = [l for l in open(path_loi, encoding='utf-8').read().split('\n') if l.strip()]
    kb, err = doc_khai_bao(path_readme)
    if err:
        return ket([err], [])

    def so_dong(k, mac_dinh=None):
        v = kb.get(k, '')
        if not v.isdigit():
            loi.append('KHAI_BAO_SAI: %s="%s", phai la so dong' % (k, v))
            return mac_dinh
        n = int(v)
        if not (1 <= n <= len(lines)):
            loi.append('KHAI_BAO_SAI: %s=%d, bai chi co %d dong' % (k, n, len(lines)))
            return mac_dinh
        return n

    # 1. kiểu hook hợp lệ
    hook = kb.get('hook', '')
    if hook not in MA_HOOK:
        loi.append('HOOK_LA: "%s" khong co trong 10 ma (%s)' % (hook, ', '.join(MA_HOOK)))
    elif taichinh and hook in HOOK_CAM_TAICHINH:
        loi.append('HOOK_CAM_TAICHINH: "%s" la khuyen nghi/doa dam doi lot, '
                   'cam cho bai tai chinh' % hook)

    # 2. mở nợ phải ở dòng 2 (dòng chứa gọn mốc rơi 1)
    mo = so_dong('mo')
    if mo is not None and mo != 2:
        loi.append('MO_SAI_DONG: mo=%d, phai la 2 (moc roi giay 8-15 nam gon trong dong 2)'
                   % mo)

    # 3. trả nợ trong dòng 5-7
    tra = so_dong('tra')
    if tra is not None and not (TRA_HOP_LE[0] <= tra <= TRA_HOP_LE[1]):
        loi.append('TRA_SAI_DONG: tra=%d, phai trong %d-%d (moc roi giay 45-60)'
                   % (tra, *TRA_HOP_LE))

    # 4. TRẢ phải dội lại MỞ — cùng cơ chế phép đo đối xứng dòng 1/dòng 10
    if mo and tra and mo != tra:
        chung = tu_noi_dung(lines[mo - 1]) & tu_noi_dung(lines[tra - 1])
        if len(chung) < 2:
            loi.append('KHONG_TRA_NO: dong %d khong doi lai dong %d (chung %d tu, can >=2) '
                       '=> mo no ma khong tra la hook lua' % (tra, mo, len(chung)))
        else:
            print('OK     | tra no: dong %d doi lai dong %d qua %d tu (%s)'
                  % (tra, mo, len(chung), ', '.join(sorted(chung)[:5])))

    # 4b. MỐC RƠI 2 (giây 45-60) — dòng 5 hoặc 6 phải có ví dụ THẬT CÓ SỐ đỡ chỗ đó
    SO_CHU = (r'(?:một|hai|ba|bốn|năm|sáu|bảy|tám|chín|mười|trăm|nghìn|triệu|tỷ|'
              r'phần trăm|thứ nhất|thứ hai|thứ ba)')
    co_so = False
    for i in range(DONG_MOC2[0], DONG_MOC2[1] + 1):
        if i <= len(lines) and (re.search(r'\d', lines[i - 1])
                                or re.search(SO_CHU, lines[i - 1].lower())):
            co_so = True
            print('OK     | moc roi 2: dong %d co so, do duoc cho giay 45-60' % i)
            break
    if not co_so:
        loi.append('MOC2_TRONG: dong %d-%d khong co so nao — day la moc roi giay 45-60, '
                   'phai co vi du THAT CO SO do cho do' % DONG_MOC2)

    # 5. dòng mở nợ không được là lời hứa rỗng
    if mo:
        d = lines[mo - 1].lower()
        for h in HUA_RONG:
            if h in d:
                loi.append('HUA_RONG: dong %d chua "%s" — day la HUA, khong phai MO NO' % (mo, h))
        # Dấu hiệu ĐÃ MỞ NỢ: câu hỏi · số · phủ định. "chưa" là dấu mạnh nhất trong tiếng
        # Việt cho một trạng thái CHƯA GIẢI QUYẾT — đúng định nghĩa món nợ. Thiếu nó thì
        # thước cảnh báo oan (bắt được khi dựng bài sp07b: dòng 2 mở nợ bằng "chưa ai đo").
        PHU_DINH = ('không', 'chưa', 'chẳng', 'nào đâu')
        if (not re.search(r'[?]', d) and not re.search(r'\d', d)
                and not any(x in d for x in PHU_DINH)):
            canh.append('MO_NO_YEU: dong %d khong co dau hoi, khong co so, khong co phu dinh '
                        '— kiem lai da dat mot mon no chua' % mo)

    # 6. trần ý mới
    y = kb.get('y_moi', '')
    if y != '1':
        loi.append('Y_MOI: khai "%s", phai la 1 (mot bai mot y — xem nghe/TRAN_Y.md)' % y)
    if not kb['y_moi_text']:
        canh.append('THIEU_Y_MOI_TEXT: nen ghi "Y_MOI: <y moi cua bai, mot cau>" de truy vet')

    # 7. câu đáng chụp màn hình
    cs = so_dong('chia_se')
    if cs is not None and cs not in CHIA_SE_HOP_LE:
        loi.append('CHIA_SE_SAI_DONG: chia_se=%d, phai la 3 hoac 10 '
                   '(dong 5-8 la than bai, cau dep bi chi tiet nuot)' % cs)
    cau = kb['cau_chia_se']
    if not cau:
        loi.append('THIEU_CAU_CHIA_SE: khong thay dong "CAU_CHIA_SE: <cau>"')
    elif cs is not None:
        n_tu = len(cau.split())
        if n_tu > TRAN_CAU_CHIA_SE:
            loi.append('CAU_CHIA_SE_DAI: %d tu, tran %d' % (n_tu, TRAN_CAU_CHIA_SE))
        goc = re.sub(r'\s+', ' ', lines[cs - 1]).lower()
        if re.sub(r'\s+', ' ', cau).lower() not in goc:
            loi.append('CAU_CHIA_SE_KHONG_CO_THAT: khai o dong %d nhung dong %d khong '
                       'chua cau do' % (cs, cs))
        low = cau.lower()
        hit = [t.strip() for t in thuatngu if t.strip() and t.strip().lower() in low]
        if hit:
            loi.append('CAU_CHIA_SE_CO_THUATNGU: %s — nguoi nhan chua xem video, '
                       'thuat ngu la buc tuong' % ', '.join(hit))
        hit = [w for w in CAM_RONG if w in low]
        if hit:
            loi.append('CAU_CHIA_SE_RONG: %s' % ', '.join(hit))
        # cặp đối nhận ra được: hoặc có số, hoặc có phủ định, hoặc có từ nối tương phản
        DOI = ['không', 'chỉ là', 'thì không', 'nhưng', 'vẫn', 'chưa phải', 'mới']
        if not re.search(r'\d', cau) and not any(d in low for d in DOI):
            canh.append('CAU_CHIA_SE_YEU: khong co so, khong co phu dinh, khong co tu noi '
                        'tuong phan — kiem lai co dang chup man hinh that khong')

    # 8. trùng câu chia sẻ với hook nghịch lý số
    if cau and hook == 'nghich_ly_so' and cs == 10:
        chung = tu_noi_dung(lines[0]) & tu_noi_dung(cau)
        if len(chung) >= 3:
            canh.append('CAU_CHIA_SE_TRUNG_HOOK: dung lai %d tu cua hook — bai chi co mot cau '
                        'noi hai lan, doi cong thuc khac (xem nghe/CO_CHIA_SE.md)' % len(chung))

    canh.append('KHONG_DO_DUOC: "moi dong co day khong" · "cau chia se chi dung voi bai nay '
                'hay dung voi moi bai" · "doi mau co dung nghia khong" — 3 cai nay PHAI doc mat')
    return ket(loi, canh)


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == '--moc':
        nhip = [int(x) for x in a[1].split(',')] if len(a) > 1 else [1, 3, 3, 2, 3, 3, 3, 3, 3, 3]
        tran = [int(x) for x in a[a.index('--tu') + 1].split(',')] if '--tu' in a else [330, 450]
        sys.exit(tinh_moc(nhip, tran))
    if a[0] == '--trung':
        if len(a) < 3:
            sys.exit('❌ can: --trung <deck_moi> <deck_truoc>')
        sys.exit(do_trung(a[1], a[2]))
    if len(a) < 2:
        sys.exit('❌ can: <loi.txt> <README_slug.md>')
    tn = a[a.index('--thuatngu') + 1].split(',') if '--thuatngu' in a else []
    sys.exit(do_kichban(a[0], a[1], tn, taichinh='--taichinh' in a))
