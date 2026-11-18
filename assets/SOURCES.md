# 그림·소리 출처와 사용 조건

확인한 날: 2026-11-18

## 그림 — 전부 직접 만든 것

| 파일 | 내용 |
|---|---|
| `chr_p.webp`, `chr_e.webp` | 우리 캐릭터 2명(털모자 쓴 아이). 방향 8개 × 동작 15칸 + 쓰러짐·승리 |
| `misc.webp` | 얼음 덩어리, 눈 덮인 바위·나무, 눈 더미, 속성별 한방, 얼굴, 깨비 4종(불·물·바람·흙, 2칸씩), 깨비 구슬 4종. (하트·별·날개 신발은 v0.8까지 쓰던 아이템 그림으로, 지금은 안 씀) |
| `floor.webp` | 돌 타일 바닥 |
| `sprites.json` | 그림 조각 위치표 |

- 깨비(v0.9): 뿔 하나 달린 동그란 몸의 작은 생물로, 우리가 새로 디자인함. 도깨비라는 옛이야기 소재에서 이름만 땄고, 다른 게임·만화의 캐릭터를 본뜨지 않음. `tools/render/render.html`의 `kkaebi()`와 `build_misc.py`로 다시 찍을 수 있음.
- 만든 방법: `tools/render/`의 3D 모형을 직접 빚어서 찍어 냄(2026-11-18). 모형·색·동작 모두 새로 만든 것이라 권리는 우리에게 있음.
- 찍는 데 쓴 도구: three.js (MIT 조건). 게임에는 들어가지 않고 그림을 찍을 때만 씀.
- 참고: 대표님이 보여 준 옛 게임 화면 한 장을 눈으로만 보고 "입체로 빚어 찍은 그림, 돌 타일 바닥, 눈" 같은 분위기만 참고함. 그 게임의 캐릭터·그림 파일은 쓰지도 따라 그리지도 않음.

## 소리 — Ninja Adventure - Asset Pack

- 만든 이: Pixel-boy, AAA / 공식 페이지: https://pixel-boy.itch.io/ninja-adventure-asset-pack
- 사용 조건: **CC0 (Creative Commons Zero)** — 공식 페이지에 "They are released under the Creative Commons Zero (CC0) license"라고 적혀 있고, 작가가 댓글에서 상업 이용도 된다고 답함.
- 가져온 곳: 작가 공식 저장소 https://github.com/pixel-boy/NinjaAdventure (커밋 6ac7823, 배경 음악), https://github.com/clear-code-projects/Zelda (커밋 5f4c57b, 효과음. README에 Pixel-boy·AAA의 CC0 자료라고 적혀 있음)

| 파일 | 내용 |
|---|---|
| `audio/hit.wav` `sword.wav` `shot.wav` `heal.wav` `ko.wav` | 효과음 (파일 이름만 바꿈: shot = fireball, ko = death) |
| `audio/music.ogg` | 배경 음악 (theme_lost_village) |

## 쓰지 않는 것

- v0.6에서 잠깐 썼던 같은 묶음의 도트 그림은 v0.7에서 모두 뺌.
- 옛 게임(서바이벌 프로젝트, 아이스랜드)의 그림·소리는 하나도 쓰지 않음.
