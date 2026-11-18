# 그림·소리 출처와 사용 조건

확인한 날: 2026-11-18

## Ninja Adventure - Asset Pack

- 만든 이: Pixel-boy, AAA
- 공식 페이지: https://pixel-boy.itch.io/ninja-adventure-asset-pack
- 사용 조건: **CC0 (Creative Commons Zero)** — 공식 페이지에 "They are released under the Creative Commons Zero (CC0) license"라고 적혀 있고, 작가가 댓글에서 상업 이용도 된다고 답함. 출처 표기는 의무가 아니지만 여기에 적어 둠.
- 가져온 곳
  1. 작가의 공식 저장소 https://github.com/pixel-boy/NinjaAdventure (커밋 6ac7823): 캐릭터 2종, 그림자, 검·도끼, 하트, 돌 조각, 눈·얼음 바닥 타일, 배경 음악
  2. https://github.com/clear-code-projects/Zelda (커밋 5f4c57b, "15 - fixes audio.zip"): 같은 묶음의 효과 그림(불꽃·번개·빛·연기·베기·회복·잎), 눈 덮인 나무·덤불·바위, 효과음. 이 저장소 README에 그림과 소리가 Pixel-boy·AAA의 CC0 자료라고 적혀 있음

## 이 저장소의 파일

| 파일 | 내용 | 손댄 것 |
|---|---|---|
| `atlas.png` | 위 그림 조각을 한 장으로 모은 것 | 4배로 키워져 있던 효과·물체 그림을 원래 크기로 줄임. 상대 캐릭터는 파란 갑옷을 붉은색으로 바꿈 |
| `atlas.json` | 조각 위치표(`index.html` 안에도 같은 내용이 들어 있음) | 직접 만듦 |
| `audio/hit.wav` `sword.wav` `shot.wav` `heal.wav` `ko.wav` | 효과음 | 파일 이름만 바꿈(shot = fireball, ko = death) |
| `audio/music.ogg` | 배경 음악(theme_lost_village) | 파일 이름만 바꿈 |

## 직접 만든 것

- 둥근 얼음판과 테두리, 충격 벽의 점선 고리, 체력 막대·표시줄·버튼, 휘두른 자국, 속성 색 표시는 코드로 그림.
- 옛 게임(서바이벌 프로젝트, 아이스랜드)의 그림·소리는 하나도 쓰지 않음.
