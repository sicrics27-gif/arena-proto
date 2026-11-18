# 3D 모형을 찍어 게임용 그림 파일로 묶는다: chr_p / chr_e (캐릭터), misc (물체·아이템·한방·얼굴), floor (바닥)
import asyncio, io, base64, json, math, os, sys
from PIL import Image, features
from drv import run
OUT = sys.argv[1]
def img(url): return Image.open(io.BytesIO(base64.b64decode(url.split(',')[1]))).convert('RGBA')
CELL, COLS = 160, 12
async def job(pg):
    cosp = await pg.evaluate('window.PITCH_COS')
    meta = {'cell': CELL, 'cols': COLS, 'charHalf': 1.5, 'charAy': round(0.5 + 0.80 * cosp / 3.0, 4), 'spr': {}}
    for k in ['p', 'e']:
        r = await pg.evaluate('([k,c,n])=>charSheet(k,c,n)', [k, CELL, COLS]); im = img(r['url']); meta['frames'] = r['n']
        im.save(f'{OUT}/chr_{k}.webp', 'WEBP', quality=90, method=6); print('chr', k, im.size, r['n'], os.path.getsize(f'{OUT}/chr_{k}.webp'))
    fl = img(await pg.evaluate('floorTex(512)')).convert('RGB'); fl.save(f'{OUT}/floor.webp', 'WEBP', quality=88, method=6); print('floor', os.path.getsize(f'{OUT}/floor.webp'))
    items = []   # (name, image, half, ay)
    for n, half, ly, size in [('ice', 0.8, 0.5, 128), ('rock', 0.9, 0.45, 144), ('pine', 1.1, 0.95, 176), ('pile', 0.8, 0.2, 128), ('heart', 0.62, 0.5, 96), ('star', 0.62, 0.5, 96), ('boot', 0.62, 0.45, 96)]:
        items.append((n, img(await pg.evaluate('([n,h,l,s])=>propShot(n,h,l,s,0)', [n, half, ly, size])), half, 0.5 + ly * cosp / (2 * half)))
    for el in ['fire', 'water', 'wind', 'earth']:
        for f in range(6):
            items.append((f's_{el}{f}', img(await pg.evaluate('([n,t])=>propShot(n,0.7,0.5,96,t)', ['s_' + el, f / 6])), 0.7, 0.5))
    for k in ['p', 'e']: items.append((f'face_{k}', img(await pg.evaluate('(k)=>faceShot(k,112)', k)), 0.66, 0.5))
    W = 1024; x = y = rowh = 0
    for n, im, half, ay in items:
        if x + im.width > W: x = 0; y += rowh; rowh = 0
        meta['spr'][n] = [x, y, im.width, im.height, half, round(ay, 4)]; x += im.width; rowh = max(rowh, im.height)
    sheet = Image.new('RGBA', (W, y + rowh), (0, 0, 0, 0))
    for n, im, half, ay in items: sheet.paste(im, tuple(meta['spr'][n][:2]))
    sheet.save(f'{OUT}/misc.webp', 'WEBP', quality=92, method=6); print('misc', sheet.size, os.path.getsize(f'{OUT}/misc.webp'))
    json.dump(meta, open(f'{OUT}/sprites.json', 'w'), separators=(',', ':'))
print('webp 지원:', features.check('webp'))
asyncio.run(run(job))
