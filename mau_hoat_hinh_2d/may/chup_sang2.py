#!/usr/bin/env python3
"""chup_sang2.py — bản 6 (24/10): thêm SWC, CDN nhóm rời sàn. Chụp dòng bẫy trên thẻ bát cơm bản khách GIAO DIỆN SÁNG (Mac), độ nét ×4, cho video mẫu 2.
python chup_sang.py <thư mục html *_sang.html> anh/   → anh/<tên>.png + gộp hộp vào anh/hop.json"""
import asyncio, json, sys
from pathlib import Path
from playwright.async_api import async_playwright
EXE = str(Path.home() / 'Library/Caches/ms-playwright/chromium-1208/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing')
CA = [('swc', 'SWC', 'SOWATCO công bố không đạt điều kiện công ty đại chúng do cơ cấu cổ đông', 393, 4),
      ('cdn', 'CDN', 'HNX thông báo CDN không đáp ứng đủ điều kiện công ty đại chúng', 393, 4)]
TIM = """(cum)=>{const chuan=s=>s.replace(/\\s+/g,' ');let best=null;
 for(const e of document.querySelectorAll('body *')){if(['STYLE','SCRIPT'].includes(e.tagName))continue;if(chuan(e.textContent).includes(cum)){if(!best||best.contains(e))best=e;}}
 if(!best)return null; if(best.tagName==='TD'){best=best.closest('tr');}
 let d=best.closest('details');while(d){d.open=true;d=d.parentElement&&d.parentElement.closest('details');}
 document.querySelectorAll('[data-dich]').forEach(x=>x.removeAttribute('data-dich'));best.setAttribute('data-dich','1');
 document.documentElement.style.scrollBehavior='auto';best.scrollIntoView({block:'center',behavior:'instant'});return best.tagName}"""
async def m():
    goc, ra = Path(sys.argv[1]), Path(sys.argv[2]); hf = ra / 'hop.json'
    hop = json.loads(hf.read_text()) if hf.exists() else {}
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=EXE)
        for ten, ma, cum, w, s in CA:
            pg = await b.new_page(viewport={'width': w, 'height': 1000}, device_scale_factor=s)
            await pg.goto(f'file://{(goc / f"{ma}_sang.html").resolve()}', wait_until='networkidle'); await pg.wait_for_timeout(500)
            tag = await pg.evaluate(TIM, cum)
            if not tag: print('KHÔNG THẤY', ten); await pg.close(); continue
            await pg.wait_for_timeout(250)
            r = await pg.evaluate("()=>{const r=document.querySelector('[data-dich]').getBoundingClientRect();return [r.left,r.top,r.width,r.height]}")
            await pg.screenshot(path=str(ra / f'{ten}_s.png'))
            hop[ten + '_s'] = {'ma': ma, 'cum': cum, 'tag': tag, 'hop_px': [round(v * s) for v in r], 'anh': [round(w * s), round(1000 * s)]}
            print(ten, tag, hop[ten + '_s']['hop_px']); await pg.close()
        await b.close()
    hf.write_text(json.dumps(hop, ensure_ascii=False))
asyncio.run(m())
