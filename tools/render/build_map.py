# 넓은 맵(깨비골 마당)을 찍는다: 바닥 한 장(map_g), 늘 앞에 오는 것(map_f), 지형물 묶음(map_p) + 자리표(map.json)
import asyncio, io, base64, json, math, os, sys
from PIL import Image
from drv import run
OUT = sys.argv[1]; P = 72
O = {'gw': 2016, 'gh': 1930, 'half': 14, 'lz': -2.36, 'cell': 324, 'cu': 4.5, 'ay': 0.72}
def img(url): return Image.open(io.BytesIO(base64.b64decode(url.split(',')[1]))).convert('RGBA')
async def job(pg):
    r = await pg.evaluate('(o)=>mapBake(o)', O)
    g = img(r['g']).convert('RGB'); g.save(f'{OUT}/map_g.webp', 'WEBP', quality=84, method=6)
    f = img(r['f']); bb = f.getbbox(); y0 = bb[1]; f = f.crop((0, y0, O['gw'], O['gh'])); f.save(f'{OUT}/map_f.webp', 'WEBP', quality=84, method=6)
    n = len(r['props']); cols = 6; rows = math.ceil(n / cols); at = Image.new('RGBA', (cols * O['cell'], rows * O['cell']), (0, 0, 0, 0)); props = []
    for i, q in enumerate(r['props']):
        im = img(q['url']); at.paste(im, ((i % cols) * O['cell'], (i // cols) * O['cell'])); bb = im.getbbox(); props.append({'x': round(q['x'], 2), 'z': round(q['z'], 2), 'bb': bb})
    at.save(f'{OUT}/map_p.webp', 'WEBP', quality=86, method=6)
    meta = dict(O, P=P, fy0=y0, cols=cols, props=props); json.dump(meta, open(f'{OUT}/map.json', 'w'))
    print('g', g.size, os.path.getsize(f'{OUT}/map_g.webp'), 'f', f.size, y0, os.path.getsize(f'{OUT}/map_f.webp'), 'p', at.size, n, os.path.getsize(f'{OUT}/map_p.webp'))
    for q in props: print(q)
asyncio.run(run(job))
