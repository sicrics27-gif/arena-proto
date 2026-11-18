# 새 캐릭터(남자 m, 여자 f) 그림 묶음과 대기실용 큰 그림을 찍는다
import asyncio, io, base64, json, os, sys
from PIL import Image
from drv import run
OUT = sys.argv[1]
def img(url): return Image.open(io.BytesIO(base64.b64decode(url.split(',')[1]))).convert('RGBA')
async def job(pg):
    meta = json.load(open(f'{OUT}/sprites.json'))
    for k in ['m', 'f']:
        r = await pg.evaluate('([k,c,n])=>charSheet2(k,c,n)', [k, meta['cell'], meta['cols']]); im = img(r['url']); assert r['n'] == meta['frames'], r['n']
        im.save(f'{OUT}/chr_{k}.webp', 'WEBP', quality=90, method=6); print('chr', k, im.size, r['n'], os.path.getsize(f'{OUT}/chr_{k}.webp'))
        pt = img(await pg.evaluate('(k)=>charOne2(k,"idle",0,2,400,1.08,0.93)', k)); pt.save(f'{OUT}/pt_{k}.webp', 'WEBP', quality=90, method=6); print('pt', k, pt.size, os.path.getsize(f'{OUT}/pt_{k}.webp'))
    c = Image.open(f'{OUT}/chr_f.webp').convert('RGBA'); bg = Image.new('RGBA', c.size, (206, 216, 228, 255)); bg.alpha_composite(c); bg.crop((0, 320, 1920, 800)).save('/home/claude/preview/chr_f.png')
asyncio.run(run(job))
