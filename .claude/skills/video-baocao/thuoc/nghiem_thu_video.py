#!/usr/bin/env python3
"""NGHIỆM THU VIDEO BẰNG MÁY — chạy SAU khi render, ĐỪNG tin exit code của render.

    <repo>/escbase_template/.venv/bin/python nghiem_thu_video.py <video.mp4> [giọng.mp3]

Cần Pillow ⇒ phải chạy bằng python của `.venv` trong `escbase_template/`, không phải
python3 hệ thống. Cần `ffmpeg`/`ffprobe` trong PATH.

Đo 7 việc (đều là bẫy ĐÃ TRẢ GIÁ, không phải nghi lễ):
  ① khổ hình / fps / bt709 đủ bộ
  ② mean & max dB      — đích mean −17,0 dB
  ③ lệch thời lượng video so với giọng (tính ra KHUNG)
  ④ hụt khung: dải sáng 133-255 ở nhiều mốc, mốc nào =0 là khung hỏng/đen
  ⑤ đứng hình 4 giây đầu: đếm khung có delta=0 (bệnh giật đã trị 24/07/2026)
  ⑥ PHỤ ĐỀ CÓ THẬT: đếm pixel sáng vùng y1330-1520.
     ⚠️ BẮT BUỘC với deck MỚI. Lỗi phụ đề 24/07/2026 là lỗi IM LẶNG: dây chuyền chỉ
     đọc cache, deck mới ra video KHÔNG có phụ đề mà vẫn PASS mọi phép đo khác.
  ⑦ ĐUÔI: 0,8s cuối phải IM (≤ −45 dB). BOSS nghe PNJ_02 (25/07) phán "video hình như
     chưa hết mà đã dừng rồi" — đo ra đuôi chỉ 0,024s, giọng chạm đúng khung cuối rồi
     cắt phựt. Bệnh có ở MỌI bài trước mà 6 phép đo cũ không cái nào bắt.

Cái KHÔNG đo được: mượt hay giật khi xem bằng mắt người, và giọng đọc hay/dở/sai dấu.
Hai thứ đó BOSS nghe rồi phán. Số ở đây chỉ chứng minh "không còn nguyên nhân kỹ thuật".
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

MOC = [0.5, 1.2, 2.0, 2.8, 3.6, 30, 60, 90, 110]
SUB_Y = (1330, 1520)


def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout + \
           subprocess.run(cmd, shell=True, capture_output=True, text=True).stderr


def main(mp4, giong=None):
    from PIL import Image, ImageChops
    ok = True

    print('=== ① KHỔ HÌNH / MÀU ===')
    p = subprocess.run(
        f'ffprobe -v error -select_streams v:0 -show_entries '
        f'stream=width,height,r_frame_rate,color_space,color_primaries,color_transfer '
        f'-show_entries format=duration,size -of default=nw=1 "{mp4}"',
        shell=True, capture_output=True, text=True).stdout
    d = dict(l.split('=', 1) for l in p.strip().split('\n') if '=' in l)
    dur = float(d.get('duration', 0))
    print(f"  {d.get('width')}x{d.get('height')} · {d.get('r_frame_rate')} · "
          f"{dur:.3f}s · {int(d.get('size', 0))/1e6:.1f} MB")
    bt = [d.get('color_space'), d.get('color_primaries'), d.get('color_transfer')]
    print(f"  bt709 đủ bộ: {bt.count('bt709') == 3}  {bt}")
    if bt.count('bt709') != 3:
        ok = False

    print('=== ② TIẾNG ===')
    a = sh(f'ffmpeg -hide_banner -i "{mp4}" -af volumedetect -f null /dev/null')
    mean = re.search(r'mean_volume:\s*(-?[\d.]+)', a)
    mx = re.search(r'max_volume:\s*(-?[\d.]+)', a)
    print(f"  mean {mean.group(1) if mean else '?'} dB · max {mx.group(1) if mx else '?'} dB "
          f"(đích mean −17,0)")

    if giong and os.path.exists(giong):
        g = subprocess.run(
            f'ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "{giong}"',
            shell=True, capture_output=True, text=True).stdout.strip()
        lech = dur - float(g)
        print(f'=== ③ LỆCH SO VỚI GIỌNG ===\n  video {dur:.4f}s · giọng {float(g):.4f}s '
              f'⇒ lệch {lech:+.4f}s = {lech*30:+.3f} khung')

    tmp = tempfile.mkdtemp(prefix='nghiemthu_')
    try:
        print('=== ④ HỤT KHUNG + ⑥ PHỤ ĐỀ ===')
        print(f"  {'mốc':>8s} {'dải sáng 133-255':>18s} {'pixel phụ đề':>14s}")
        for t in MOC:
            if t > dur:
                continue
            f = os.path.join(tmp, f'{t}.png')
            subprocess.run(f'ffmpeg -v error -ss {t} -i "{mp4}" -frames:v 1 -y "{f}"',
                           shell=True, capture_output=True)
            if not os.path.exists(f):
                continue
            im = Image.open(f).convert('L')
            w, _ = im.size
            sang = sum(im.histogram()[133:256])
            sub = im.crop((0, SUB_Y[0], w, SUB_Y[1]))
            px = sum(1 for v in sub.get_flattened_data() if v > 140) \
                if hasattr(sub, 'get_flattened_data') else \
                sum(1 for v in list(sub.getdata()) if v > 140)
            co = '' if sang and px else '  ← ❌'
            if not sang or not px:
                ok = False
            print(f'  {t:>8} {sang:>18d} {px:>14d}{co}')
        print('  (mốc nào dải sáng=0 ⇒ khung hỏng; pixel phụ đề=0 ⇒ MẤT PHỤ ĐỀ)')

        print('=== ⑤ ĐỨNG HÌNH 4 GIÂY ĐẦU ===')
        mv = os.path.join(tmp, 'mv')
        os.makedirs(mv, exist_ok=True)
        subprocess.run(f'ffmpeg -v error -i "{mp4}" -t 4 -vf scale=270:480 -y '
                       f'"{mv}/%04d.png"', shell=True, capture_output=True)
        fs = sorted(os.listdir(mv))
        dung = run = mxrun = 0
        prev = Image.open(os.path.join(mv, fs[0])).convert('L')
        for f in fs[1:]:
            cur = Image.open(os.path.join(mv, f)).convert('L')
            s = sum(i * c for i, c in enumerate(ImageChops.difference(prev, cur).histogram()))
            if s == 0:
                dung += 1
                run += 1
                mxrun = max(mxrun, run)
            else:
                run = 0
            prev = cur
        print(f'  khung đứng hình: {dung}/{len(fs)-1} · chuỗi dài nhất {mxrun} khung '
              f'({mxrun/30:.2f}s)')
        if dung:
            ok = False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # ⑦ ĐUÔI — có im lặng sau câu cuối không?
    # BOSS nghe PNJ_02 (25/07): "video hình như chưa hết mà đã dừng rồi". Đo ra đúng:
    # đuôi 0,024s, một giây cuối vẫn còn tiếng ở max −4,8 dB. Bệnh có ở MỌI bài trước
    # mà không phép đo nào bắt — đúng kiểu lỗi IM LẶNG. Nay đóng thành cổng.
    print('=== ⑦ ĐUÔI (im lặng sau câu cuối) ===')
    DUOI_TT, NGUONG_IM = 0.8, -45.0     # giây · dB (TAIL_SECONDS=1,4 nên còn dư biên)
    # 🔴 PHẢI ĐO FILE GIỌNG, KHÔNG ĐO MP4. Bản mix của mp4 có NHẠC NỀN chạy suốt tới
    # khung cuối — mà nhạc chạy qua đuôi mới ĐÚNG, đó chính là khoảng thở. Đo mp4 thì
    # nhạc che mất câu trả lời: bài PNJ 02b đo mp4 ra −19,0 dB (tưởng hỏng), đo file
    # giọng ra −91,0 dB (im hẳn, đuôi đúng). Bẫy đã dính ngay lần chạy đầu của cổng này.
    if giong and os.path.exists(giong):
        r = sh(f'ffmpeg -sseof -{DUOI_TT} -i "{giong}" -af volumedetect -f null /dev/null')
        m = re.search(r'max_volume:\s*(-?[\d.]+) dB', r)
        if not m:
            print('  ⚠️ không đo được mức âm đuôi giọng (bỏ qua, không chặn)')
        else:
            mx = float(m.group(1))
            print(f'  giọng, {DUOI_TT}s cuối: max {mx:.1f} dB (đích ≤ {NGUONG_IM:.0f} dB)')
            if mx > NGUONG_IM:
                print(f'  ❌ giọng vẫn nói ở {DUOI_TT}s cuối ⇒ video cắt ngay lúc dứt câu.')
                print('     Sửa `TAIL_SECONDS` trong escbase_template/tts/common.py, sinh lại')
                print('     giọng (bước 4) rồi render lại. ĐỪNG nối im lặng vào mp4 sau khi')
                print('     render — làm vậy là lệch timing.json.')
                ok = False
    else:
        print('  ⚠️ KHÔNG truyền file giọng ⇒ không đo được đuôi.')
        print('     Đo trên mp4 là vô nghĩa: nhạc nền chạy tới khung cuối sẽ che mất.')
        print('     Chạy lại kèm đường dẫn output/voiceover_concat.mp3.')

    print(f"\n{'✅ ĐẠT hết phép đo máy' if ok else '❌ CÓ PHÉP ĐO HỎNG — xem dấu ❌ ở trên'}")
    print('⚠️ MƯỢT & GIỌNG: máy không phán được, để BOSS nghe rồi phán.')
    return 0 if ok else 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
