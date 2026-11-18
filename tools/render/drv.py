# 찍기 도구 실행기: 로컬 서버를 띄우고 render.html의 함수를 불러 그림을 저장한다
import asyncio, base64, subprocess, sys, time, json
from playwright.async_api import async_playwright
def save(url, path): open(path, 'wb').write(base64.b64decode(url.split(',')[1]))
async def run(job):
    srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8765', '--bind', '127.0.0.1'], cwd=__import__('os').path.dirname(__import__('os').path.abspath(__file__)), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    try:
        async with async_playwright() as p:
            b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
            pg = await b.new_page(); errs = []
            pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' and 'favicon' not in m.text and '404' not in m.text else None)
            await pg.goto('http://127.0.0.1:8765/render.html')
            try: await pg.wait_for_function('window.ready === true', timeout=20000)
            except Exception: print('준비 실패. 오류:', errs[:5]); await b.close(); return
            await job(pg)
            if errs: print('오류:', errs[:5])
            await b.close()
    finally:
        srv.terminate()
