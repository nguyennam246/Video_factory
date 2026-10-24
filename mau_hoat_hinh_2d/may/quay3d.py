#!/usr/bin/env python3
"""quay3d.py — quay phim3d.html thành khung JPEG 1080×1920, 24 khung/giây, CHẠY TRÊN MAC (GPU, BOSS cho phép 23/10).
  python quay3d.py khung            → toàn bộ
  python quay3d.py --anh soi 3 12   → vài khung để soi"""
import asyncio, json, subprocess, sys, time
from pathlib import Path
from playwright.async_api import async_playwright
FPS, CONG = 24, 8941

async def main():
    a = sys.argv[1:]; anh = a[0] == '--anh'
    if anh: a = a[1:]
    ra = Path(a[0]); ra.mkdir(parents=True, exist_ok=True)
    sv = subprocess.Popen([sys.executable, '-m', 'http.server', str(CONG), '--bind', '127.0.0.1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        time.sleep(0.8)
        async with async_playwright() as p:
            b = await p.chromium.launch(executable_path=str(Path.home() / 'Library/Caches/ms-playwright/chromium-1208/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'), args=['--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist', '--enable-unsafe-webgpu'])
            pg = await b.new_page(viewport={'width': 1080, 'height': 1920})
            pg.on('console', lambda m: print('console:', m.text) if m.type in ('error', 'warning') else None)
            pg.on('pageerror', lambda e: print('LỖI TRANG:', e))
            await pg.add_init_script(f"window.NHIP={Path('nhip.json').read_text()};window.HOP={Path('anh/hop.json').read_text()};")
            import os
            await pg.goto(f'http://127.0.0.1:{CONG}/' + os.environ.get('TRANG', 'phim3d.html'))
            await pg.wait_for_function('window.SAN_SANG===true', timeout=20000)
            print(await pg.evaluate("(()=>{const g=document.createElement('canvas').getContext('webgl2');const d=g.getExtension('WEBGL_debug_renderer_info');return g.getParameter(d.UNMASKED_RENDERER_WEBGL)})()"))
            tong = await pg.evaluate('window.TONG')
            sk = await pg.evaluate('window.SU_KIEN || null')
            if sk is not None: Path('su_kien.json').write_text(json.dumps(sk))
            ds = [float(x) for x in a[1:]] if anh else [i / FPS for i in range(int(tong * FPS))]
            t = time.time()
            for i, x in enumerate(ds):
                await pg.evaluate(f've({x})')
                ten = f't{x:07.2f}.png' if anh else f'{i:06d}.jpg'
                await pg.screenshot(path=str(ra / ten), type='png' if anh else 'jpeg', **({} if anh else {'quality': 92}))
                if not anh and i % 120 == 0: print(i, '/', len(ds), round((time.time() - t) / (i + 1), 3), 'giây/khung', flush=True)
            print('TONG', tong, 'khung', len(ds), 'giây/khung', round((time.time() - t) / max(1, len(ds)), 3))
            await b.close()
    finally:
        sv.terminate()

asyncio.run(main())
