# 그림 찍는 도구

게임 그림(캐릭터·바닥·물체·아이템·한방)은 여기서 3D 모형으로 빚어 찍어 낸 것입니다. 게임에는 찍힌 그림 파일만 들어갑니다.

- `render.html`: 모형과 동작을 정의하고 찍는 곳 (three.js 사용, MIT 조건의 개발 도구)
- `build_sheets.py`: 모든 그림을 찍어 `assets/`에 `chr_p.webp`, `chr_e.webp`, `misc.webp`, `floor.webp`, `sprites.json`으로 저장
- 다시 찍는 법: 이 폴더에서 `npm i three@0.170.0` 후 `python3 build_sheets.py ../../assets` (크롬과 playwright 필요). `sprites.json` 내용이 바뀌면 `index.html`의 `META`도 같이 바꿔야 합니다.
