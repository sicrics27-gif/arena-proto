# misc 그림 묶음만 다시 만든다 (캐릭터·바닥 그림은 그대로 둠). 뒤에 깨비 8칸과 구슬 4칸을 덧붙인다
import asyncio, io, base64, json, os, sys
from PIL import Image
from drv import run
OUT = sys.argv[1]
def img(url): return Image.open(io.BytesIO(base64.b64decode(url.split(',')[1]))).convert('RGBA')
async def job(pg):
    cosp = await pg.evaluate('window.PITCH_COS')
    meta = json.load(open(f'{OUT}/sprites.json')); old = dict(meta['spr']); meta['spr'] = {}
    items = []   # (name, image, half, ay)
    for n, half, ly, size in [('ice', 0.8, 0.5, 128), ('rock', 0.9, 0.45, 144), ('pine', 1.1, 0.95, 176), ('pile', 0.8, 0.2, 128), ('heart', 0.62, 0.5, 96), ('star', 0.62, 0.5, 96), ('boot', 0.62, 0.45, 96)]:
        items.append((n, img(await pg.evaluate('([n,h,l,s])=>propShot(n,h,l,s,0)', [n, half, ly, size])), half, 0.5 + ly * cosp / (2 * half)))
    for el in ['fire', 'water', 'wind', 'earth']:
        for f in range(6):
            items.append((f's_{el}{f}', img(await pg.evaluate('([n,t])=>propShot(n,0.7,0.5,96,t)', ['s_' + el, f / 6])), 0.7, 0.5))
    for k in ['m', 'f']: items.append((f'face_{k}', img(await pg.evaluate('(k)=>charOne2(k,"idle",0,2,112,0.52,1.40)', k)), 0.52, 0.5))   # 표시줄 얼굴 (새 캐릭터)
    for el in ['fire', 'water', 'wind', 'earth']:
        for f in range(2):
            items.append((f'k_{el}{f}', img(await pg.evaluate('([n,t])=>propShot(n,0.78,0.5,120,t)', ['k_' + el, f / 2])), 0.78, 0.5 + 0.5 * cosp / (2 * 0.78)))
    for el in ['fire', 'water', 'wind', 'earth']:
        items.append((f'b_{el}', img(await pg.evaluate('([n])=>propShot(n,0.4,0.33,72,0)', ['b_' + el])), 0.4, 0.5 + 0.33 * cosp / (2 * 0.4)))
    W = 1024; x = y = rowh = 0
    for n, im, half, ay in items:
        if x + im.width > W: x = 0; y += rowh; rowh = 0
        meta['spr'][n] = [x, y, im.width, im.height, half, round(ay, 4)]; x += im.width; rowh = max(rowh, im.height)
    moved = [n for n in old if n in meta['spr'] and old[n][:4] != meta['spr'][n][:4]]
    sheet = Image.new('RGBA', (W, y + rowh), (0, 0, 0, 0))
    for n, im, half, ay in items: sheet.paste(im, tuple(meta['spr'][n][:2]))
    sheet.save(f'{OUT}/misc.webp', 'WEBP', quality=92, method=6); print('misc', sheet.size, os.path.getsize(f'{OUT}/misc.webp'), '자리 바뀐 기존 그림:', moved)
    meta['sheet'] = [sheet.width, sheet.height]
    json.dump(meta, open(f'{OUT}/sprites.json', 'w'), separators=(',', ':'))
    bg = Image.new('RGBA', sheet.size, (74, 62, 56, 255)); bg.alpha_composite(sheet); bg.save('/home/claude/preview/misc.png')
asyncio.run(run(job))
