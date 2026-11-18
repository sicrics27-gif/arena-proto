# 그림 찍는 도구

게임 그림(캐릭터·바닥·물체·아이템·한방)은 여기서 3D 모형으로 빚어 찍어 낸 것입니다. 게임에는 찍힌 그림 파일만 들어갑니다.

- `render.html`: 모형과 동작을 정의하고 찍는 곳 (three.js 사용, MIT 조건의 개발 도구)
- `build_sheets.py`: 모든 그림을 찍어 `assets/`에 `chr_p.webp`, `chr_e.webp`, `misc.webp`, `floor.webp`, `sprites.json`으로 저장
- 다시 찍는 법: 이 폴더에서 `npm i three@0.170.0` 후 `python3 build_sheets.py ../../assets` (크롬과 playwright 필요). `sprites.json` 내용이 바뀌면 `index.html`의 `META`도 같이 바꿔야 합니다.
- `build_misc.py`: 물체 그림 묶음(`misc.webp`)만 다시 만들면서 깨비 4종·구슬 4종을 덧붙임. `build_sheets.py`를 돌린 뒤에는 `python3 build_misc.py ../../assets`도 꼭 돌려야 깨비 그림이 들어갑니다.
- `build_chars2.py`: 새 캐릭터(남자 `chr_m`, 여자 `chr_f`)와 대기실용 큰 그림(`pt_m`, `pt_f`)을 찍음. 표시줄 얼굴은 `build_misc.py`가 같이 찍음. v0.10부터 게임은 이 캐릭터만 씀(`build_sheets.py`의 예전 캐릭터 그림은 쓰지 않음).
