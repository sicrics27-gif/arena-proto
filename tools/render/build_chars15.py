# v0.15 새 캐릭터 4명(도담 d=둔기, 소이 s=석궁, 미르 r=지팡이, 가온 g=지팡이): 45도 그림 묶음 + 대기실 큰 그림
import asyncio, io, base64, json, os, sys
from PIL import Image
from drv import run
OUT = sys.argv[1]; WT = {'d': 'm', 's': 'c', 'r': 't', 'g': 't'}
KEYS = sys.argv[2].split(',') if len(sys.argv) > 2 else list(WT)
def img(url): return Image.open(io.BytesIO(base64.b64decode(url.split(',')[1]))).convert('RGBA')
async def job(pg):
    meta = json.load(open(f'{OUT}/sprites.json'))
    for k in KEYS:
        pt = img(await pg.evaluate('([k,wt])=>charOne2(k,"idle",0,2,400,1.08,0.93,wt)', [k, WT.get(k)])); pt.save(f'{OUT}/pt_{k}.webp', 'WEBP', quality=90, method=6)
        if k in WT:
            await pg.evaluate('window.PITCH_OVR = 45 * Math.PI / 180')
            r = await pg.evaluate('([k,c,n,wt])=>charSheet2(k,c,n,wt)', [k, meta['cell'], meta['cols'], WT[k]]); im = img(r['url']); assert r['n'] == meta['frames']
            im.save(f'{OUT}/chr_{k}.webp', 'WEBP', quality=88, method=6); await pg.evaluate('window.PITCH_OVR = 0')
        print('done', k, flush=True)
asyncio.run(run(job))
