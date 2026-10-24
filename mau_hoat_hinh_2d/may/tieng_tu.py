#!/usr/bin/env python3
"""tieng_tu.py — giọng edge NamMinh +14 % từng câu KÈM mốc từng chữ (WordBoundary) cho phụ đề chạy chữ.
python tieng_tu.py loi.txt [C01,C11]  → tieng/<hash>.mp3 (bộ nhớ đệm theo chữ) + nhip.json {Cxx:{cau:[{bd,dai,chu,tu:[[bd,dai,chu]]}],dai}} + tieng/toan.wav"""
import asyncio, hashlib, json, re, subprocess, sys, time
from pathlib import Path
import edge_tts
GIONG, TOC, NGHI_CAU, NGHI_CANH = 'vi-VN-NamMinhNeural', '+14%', 0.28, 0.6
T = Path('tieng'); T.mkdir(exist_ok=True)

def dai(f):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(f)]))

async def doc(chu, f, fj):
    for lan in range(6):
        try:
            tu, buf = [], bytearray()
            async for m in edge_tts.Communicate(chu, GIONG, rate=TOC, boundary='WordBoundary').stream():
                if m['type'] == 'audio':
                    buf += m['data']
                elif m['type'] == 'WordBoundary':
                    tu.append([m['offset'] / 1e7, m['duration'] / 1e7, m['text']])
            if len(buf) > 1000 and tu:
                f.write_bytes(bytes(buf)); fj.write_text(json.dumps(tu, ensure_ascii=False)); return
        except Exception as e:  # noqa: BLE001
            print('  thử lại', lan, e)
        time.sleep(3 + 3 * lan)
    raise SystemExit('hỏng ' + chu)

async def main():
    chon = set(sys.argv[2].split(',')) if len(sys.argv) > 2 else None
    nhip, ds = {}, []
    for dong in Path(sys.argv[1]).read_text().strip().splitlines():
        c, chu = dong.split('|', 1)
        if chon and c not in chon:
            continue
        cau = [x.strip() for x in re.split(r'(?<=[.?!])\s+', chu) if x.strip()]
        t, mang = 0.0, []
        for k, x in enumerate(cau):
            h = hashlib.md5((GIONG + TOC + x).encode()).hexdigest()[:12]
            f, fj = T / f'{h}.mp3', T / f'{h}.json'
            if not f.exists() or not fj.exists():
                await doc(x, f, fj)
            d = dai(f)
            mang.append({'bd': round(t, 3), 'dai': round(d, 3), 'chu': x, 'tu': json.loads(fj.read_text())})
            nghi = NGHI_CAU if k < len(cau) - 1 else NGHI_CANH
            ds += [(f, d), (None, nghi)]
            t += d + nghi
        nhip[c] = {'cau': mang, 'dai': round(t, 3)}
        print(c, len(cau), 'câu', round(t, 1), 's')
    Path('nhip.json').write_text(json.dumps(nhip, ensure_ascii=False))
    with (T / 'ds.txt').open('w') as g:
        for i, (f, d) in enumerate(ds):
            w = T / f'_m{i:04d}.wav'
            src = ['-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=mono', '-t', str(d)] if f is None else ['-i', str(f)]
            subprocess.run(['ffmpeg', '-v', 'error', '-y', *src, '-ar', '48000', '-ac', '1', str(w)], check=True)
            g.write(f"file '{w.name}'\n")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(T / 'ds.txt'), '-c', 'copy', str(T / 'giong.wav')], check=True)
    for w in T.glob('_m*.wav'):
        w.unlink()
    print('giọng', round(dai(T / 'giong.wav'), 2), 's')

asyncio.run(main())
