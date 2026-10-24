#!/usr/bin/env python3
"""am_thanh2.py — tiếng động theo su_kien.json (phim2d.html xuất qua quay3d.py) + trộn giọng ×2,0 + nhạc nền meta.mp3 ×0,9 (công thức escbase).
python am_thanh2.py → tieng/sfx2.wav, tieng/tron2.wav"""
import json, subprocess
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt
SR = 48000
N = json.load(open('nhip.json')); TONG = sum(v['dai'] for v in N.values())
SK = json.load(open('su_kien.json'))
rng = np.random.default_rng(7); out = np.zeros(int((TONG + 2) * SR))
def dat(sig, t, g=1.0):
    i = int(max(0, t) * SR); n = min(len(sig), len(out) - i); out[i:i + n] += sig[:n] * g
def loc(x, lo=None, hi=None):
    if lo and hi: return sosfilt(butter(4, [lo, hi], 'band', fs=SR, output='sos'), x)
    if lo: return sosfilt(butter(4, lo, 'high', fs=SR, output='sos'), x)
    return sosfilt(butter(4, hi, 'low', fs=SR, output='sos'), x)
def bao(n, a, d):
    t = np.arange(n) / SR; return np.minimum(t / max(a, 1e-4), 1) * np.exp(-np.maximum(t - a, 0) / d)
def sap():
    n = int(1.2 * SR); t = np.arange(n) / SR
    return (loc(rng.standard_normal(n), lo=2500) * bao(n, .0005, .012) + sum(np.sin(2 * np.pi * f * t) * np.exp(-t * k) for f, k in [(1830, 9), (2710, 12), (3950, 16)]) * .09
            + np.sin(2 * np.pi * 70 * t * (1 - .3 * t)) * bao(n, .002, .18) * .9) * .55
def vut():
    n = int(.9 * SR); x = rng.standard_normal(n); y = np.zeros(n)
    for k in range(9):
        a, b = k * n // 9, (k + 1) * n // 9; f = 300 * (12 ** (k / 8)); y[a:b] = loc(x, lo=f, hi=min(f * 2.2, 20000))[a:b]
    return y * np.sin(np.linspace(0, np.pi, n)) ** 2 * .3
def dap():
    n = int(.8 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 95 * t * (1 - .4 * t)) * bao(n, .001, .09) + loc(rng.standard_normal(n), 200, 1800) * bao(n, .0005, .03) * .6) * .75
def pop_():
    n = int(.25 * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * (520 + 900 * t) * t) * bao(n, .002, .05) * .35
def dem():
    m = int(.03 * SR); s = np.sin(2 * np.pi * 2200 * np.arange(m) / SR) * bao(m, .0005, .006); y = np.zeros(int(1.8 * SR))
    for i in range(14):
        tt = 1.1 * (1 - (1 - i / 13) ** 2); j = int(tt * SR); y[j:j + m] += s * .1
    n = int(.7 * SR); t = np.arange(n) / SR; j = int(1.1 * SR); y[j:j + n] += np.sin(2 * np.pi * 48 * t) * bao(n, .005, .4) * .5
    return y
LOAI = {'sap': sap, 'vut': vut, 'dap': dap, 'pop': pop_, 'dem': dem}
for e in SK: dat(LOAI[e['loai']](), e['t'])
n = int(3 * SR); t = np.arange(n) / SR
dat((np.sin(2 * np.pi * 41 * t) * bao(n, .02, 1.2) + loc(rng.standard_normal(n), hi=300) * bao(n, .01, .6) * .3) * .45, .6)
out = out / max(1e-9, np.abs(out).max()) * .9
wavfile.write('tieng/sfx2.wav', SR, (out * 32767).astype(np.int16))
BGM = '/Users/simple/Desktop/Cloud/video/escbase_template/headless/deck_hpd02/preview-assets/bgm/meta.mp3'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'tieng/giong.wav', '-stream_loop', '-1', '-i', BGM, '-i', 'tieng/sfx2.wav',
  '-filter_complex', f'[0:a]volume=2.0,apad[g];[1:a]volume=0.9,afade=t=in:d=1.5,afade=t=out:st={TONG - 2:.2f}:d=2[n];[2:a]volume=0.8[s];'
  f'[g][n][s]amix=inputs=3:normalize=0:duration=longest,atrim=0:{TONG:.3f},alimiter=limit=0.95[o]',
  '-map', '[o]', '-ar', '48000', '-ac', '2', 'tieng/tron2.wav'], check=True)
print('sự kiện', len(SK), {k: sum(e['loai'] == k for e in SK) for k in LOAI}, 'tổng', round(TONG, 2))
