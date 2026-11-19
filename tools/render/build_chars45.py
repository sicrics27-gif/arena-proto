# 캐릭터 그림 8장을 맵과 같은 각도(45도)로 다시 찍는다
import asyncio, io, base64, json, os, sys
from PIL import Image
from drv import run
OUT = sys.argv[1]
def img(url): return Image.open(io.BytesIO(base64.b64decode(url.split(',')[1]))).convert('RGBA')
async def job(pg):
    meta = json.load(open(f'{OUT}/sprites.json')); await pg.evaluate('window.PITCH_OVR = 45 * Math.PI / 180')
    for k in ['m', 'f']:
        for wt in [None, 'm', 'c', 't']:
            r = await pg.evaluate('([k,c,n,wt])=>charSheet2(k,c,n,wt||undefined)', [k, meta['cell'], meta['cols'], wt]); im = img(r['url']); assert r['n'] == meta['frames'], r['n']
            fn = f'{OUT}/chr_{k}' + (f'_{wt}' if wt else '') + '.webp'; im.save(fn, 'WEBP', quality=88, method=6); print('chr', k, wt, im.size, os.path.getsize(fn), flush=True)
asyncio.run(run(job))
