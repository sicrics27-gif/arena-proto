# 그림·소리 출처와 사용 조건

확인한 날: 2026-11-18

## 그림 — 전부 직접 만든 것

| 파일 | 내용 |
|---|---|
| `chr_m.webp`, `chr_f.webp` | 우리 캐릭터 2명(남자·여자, v0.10에서 새로 만듦). 방향 8개 × 동작 15칸 + 쓰러짐·승리. v0.12에서 맵과 같은 45도 각도로 다시 찍음(`tools/render/build_chars45.py`). 예전 털모자 캐릭터(`chr_p`, `chr_e`)는 뺌 |
| `chr_m_m.webp`, `chr_m_c.webp`, `chr_m_t.webp`, `chr_f_m.webp`, `chr_f_c.webp`, `chr_f_t.webp` | 같은 두 캐릭터가 둔기(m)·석궁(c)·지팡이(t)를 든 그림(v0.11). 검을 든 그림은 `chr_m`·`chr_f`. 무기 모형도 직접 빚음. `tools/render/build_chars3.py`로 찍음 |
| `map_g.webp`, `map_f.webp`, `map_p.webp` | 맵 '깨비골 마당'(v0.12, 임시 이름). 바닥 한 장, 늘 앞에 오는 아래쪽 울타리·나무, 지형물 21개 묶음. 돌바닥·말뚝과 금줄·돌탑·석등·우물·평상·짚더미·장독대·연못·대문과 담·단풍나무·초롱·지킴이 말뚝 모두 직접 빚은 모형이고 배치도 우리 것. 옛이야기·옛집 소재(도깨비, 장독대, 초롱 등)만 빌렸고 다른 게임의 지도를 본뜨지 않음. `tools/render/build_map.py`로 찍음 |
| `chr_d.webp`, `chr_s.webp`, `chr_r.webp`, `chr_g.webp`, `pt_d/s/r/g.webp` | v0.15 새 캐릭터 4명(도담·소이·미르·가온, 임시 이름). 같은 3D 모형 틀에 머리 모양(짧은 머리·묶은 머리·긴 머리·틀어 올린 머리)·옷(조끼·도포)·몸집을 더해 직접 빚음. 다른 게임·만화 캐릭터를 본뜨지 않음 |
| `pt_m.webp`, `pt_f.webp` | 대기실·캐릭터 고르기 화면에 쓰는 큰 그림 |
| `misc.webp` | 얼음 덩어리, 눈 덮인 바위·나무, 눈 더미, 속성별 한방, 얼굴, 깨비 4종(불·물·바람·흙, 2칸씩), 깨비 구슬 4종. (하트·별·날개 신발은 v0.8까지 쓰던 아이템 그림으로, 지금은 안 씀) |
| (`floor.webp`) | 돌 타일 바닥. v0.11까지 쓰던 그림으로, v0.12에서 뺌 |
| `mob.webp` | 사냥 모드 몬스터 묶음(v0.17): 밤톨이·도토리 포수·호박 덩이(2칸씩), 허수아비 대장(3칸). 3D 모형을 직접 빚어 30도 각도로 찍음(`tools/render/build_mobs.py`, 모형은 `render.html`의 `mobBuild`) |
| `sprites.json` | 그림 조각 위치표 |

- 새 캐릭터(v0.10): 남자(남색 뻗친 머리·파란 겉옷·빨간 목도리), 여자(분홍 양 갈래 머리·빨간 치마·노란 리본). 모형·얼굴 그림·색 모두 직접 만든 것이고, 실존 인물이나 다른 게임·만화의 캐릭터를 본뜨지 않음. `tools/render/render.html`의 `makeChar2()`·`faceTex()`와 `build_chars2.py`로 다시 찍을 수 있음.
- 깨비(v0.9): 뿔 하나 달린 동그란 몸의 작은 생물로, 우리가 새로 디자인함. 도깨비라는 옛이야기 소재에서 이름만 땄고, 다른 게임·만화의 캐릭터를 본뜨지 않음. `tools/render/render.html`의 `kkaebi()`와 `build_misc.py`로 다시 찍을 수 있음.
- 몬스터(v0.17): 밤송이·도토리·늙은 호박·허수아비라는 가을 들판의 흔한 사물에서 소재만 따서 우리가 새로 디자인함(눈·입·팔다리·모자 모두 직접 빚음). 이름(밤톨이, 도토리 포수, 호박 덩이, 허수아비 대장, 대장 호박, 대장 밤톨이)도 새로 지은 임시 이름. 옛 게임이나 다른 게임·만화의 몬스터를 본뜨지 않았고, 그런 그림 파일을 보거나 쓰지 않음.
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
