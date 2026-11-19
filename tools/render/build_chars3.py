# 무기별 캐릭터 그림 묶음(둔기 m, 석궁 c, 지팡이 t)을 찍는다. 검은 chr_m·chr_f 그대로.
import asyncio, io, base64, json, os, sys
from PIL import Image
from drv import run
OUT = sys.argv[1]
def img(url): return Image.open(io.BytesIO(base64.b64decode(url.split(',')[1]))).convert('RGBA')
async def job(pg):
    meta = json.load(open(f'{OUT}/sprites.json'))
    for k in ['m', 'f']:
        for wt in ['m', 'c', 't']:
            r = await pg.evaluate('([k,c,n,wt])=>charSheet2(k,c,n,wt)', [k, meta['cell'], meta['cols'], wt]); im = img(r['url']); assert r['n'] == meta['frames'], r['n']
            fn = f'{OUT}/chr_{k}_{wt}.webp'; im.save(fn, 'WEBP', quality=88, method=6); print('chr', k, wt, im.size, r['n'], os.path.getsize(fn), flush=True)
asyncio.run(run(job))
