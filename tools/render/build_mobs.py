# 사냥 모드 몬스터 그림 묶음(mob.webp)을 찍는다. 자리표는 화면에 찍어 주므로 index.html의 MOBSPR에 옮겨 적는다
import asyncio, io, base64, json, math, os, sys
from PIL import Image
from drv import run
OUT = sys.argv[1]
def img(url): return Image.open(io.BytesIO(base64.b64decode(url.split(',')[1]))).convert('RGBA')
SPEC = [('bam', 2, 0.78, 0.44, 112), ('doto', 2, 0.78, 0.5, 112), ('hobak', 2, 0.86, 0.44, 124), ('heosu', 3, 1.5, 1.3, 216)]
async def job(pg):
    await pg.evaluate('window.PITCH_OVR = 30 * Math.PI / 180'); cosp = math.cos(math.radians(30))   # 얼굴이 보이게 캐릭터(45도)보다 낮은 각도로 찍음
    items = []
    for name, n, half, ly, size in SPEC:
        for f in range(n): items.append((f'{name}{f}', img(await pg.evaluate('([t,f,h,l,s])=>mobShot(t,f,h,l,s)', [name, f, half, ly, size])), half, 0.5 + ly * cosp / (2 * half)))
    W = 720; x = y = rowh = 0; meta = {}
    for n, im, half, ay in items:
        if x + im.width > W: x = 0; y += rowh; rowh = 0
        meta[n] = [x, y, im.width, im.height, half, round(ay, 4)]; x += im.width; rowh = max(rowh, im.height)
    sheet = Image.new('RGBA', (W, y + rowh), (0, 0, 0, 0))
    for n, im, half, ay in items: sheet.paste(im, tuple(meta[n][:2]))
    sheet.save(f'{OUT}/mob.webp', 'WEBP', quality=90, method=6); print('mob', sheet.size, os.path.getsize(f'{OUT}/mob.webp'))
    print(json.dumps(meta, separators=(',', ':')))
    if os.path.isdir('/home/claude/preview'): bg = Image.new('RGBA', sheet.size, (203, 171, 122, 255)); bg.alpha_composite(sheet); bg.save('/home/claude/preview/mob.png')   # 눈으로 확인하는 그림(없어도 됨)
asyncio.run(run(job))
