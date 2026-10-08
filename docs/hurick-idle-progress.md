---
title: Sword Emperor Hurick — 진행 기록 & PC 이전 안내
date: 2026-10-08
status: active
tags: [game, idle-rpg, progress, handoff]
---

# Sword Emperor Hurick — 진행 기록

> 클라우드 세션(Crawl_site 저장소, 브랜치 `claude/idle-rpg-game-design-33m7xq`)에서 진행한 내용을 정리한 문서입니다.
> PC의 Claude Code로 옮겨서 이어갈 때 이 문서부터 읽으면 됩니다.

## 1. 지금까지 한 일

| 날짜 | 내용 | 결과물 |
|---|---|---|
| 10-06 | 세로형 방치 RPG PRD 초안 + 스토리 후보 5종(A~E) | `idle-rpg-prd.md` v0.1 |
| 10-08 | 스토리 A(탑 등반) + 중세 유럽 판타지 확정, 도트·Android 확정 | PRD v0.2 |
| 10-08 | 전투·무기·스탯 설계 문서 작성 | `idle-rpg-combat.md` v0.1 |
| 10-08 | 스탯을 STAB·HACK·INT로 변경, 무기 8종·스탯 비율·공속 반비례, 적 방어 특성, Stage 해금 | PRD v0.3, combat v0.2 |
| 10-08 | 주인공 이름 Hurick 해외 정서 검토, 제목 후보 검토 | PRD §9 |
| 10-08 | Claude Code로 도트 샘플 제작 (휴릭 × 무기 5종) | `assets/hurick-weapon-swap-sample.png` |
| 10-08 | **제목 Sword Emperor Hurick / 저장소 이름 `hurick-idle` 확정** | PRD 결정 기록 |
| 10-08 | GitHub 저장소 생성 시도 → 권한 없음(403)으로 실패. PC에서 진행하기로 결정 | 이 문서 |
| 10-08 | 기능 요구사항 정의서 작성 | `hurick-idle-frd.md` |

## 2. 확정된 사항

| 항목 | 결정 |
|---|---|
| 제목 | **Sword Emperor Hurick** / KR **검제 키우기: 휴릭** (출시 전 상표 검색 필요) |
| 장르 | 세로형 픽셀 방치형 RPG, Android 우선, 한·영 지원 |
| 스토리 | 중세 유럽풍 알베른 왕국, 잿빛 역병, 성 아르멜의 종탑. 검사 휴릭이 동생 엘라를 위해 탑을 오르며 "검제"가 됨 |
| 스탯 | STAB(찌르기) · HACK(베기) · INT(마력, Stage 100 해금) |
| 무기 | 평도(시작) → 세검(20) → 대검(40) → 둔기(70) → 마검(100) → 마단검(130) → 마법대검(170) → 마법둔기(200) |
| 무기 균형 | 종류 간 상하 관계 없음, 공속↔1타 공격력 반비례, 기본 DPS 동일 |
| 적 방어 | 물리 방어력 · 마법 방어력 · 결계 · 슈퍼아머 · 재생 |
| 기술 스택 | Phaser + TypeScript + Vite → Capacitor → Android |
| 저장소 | `hurick-idle` (영어 이름) |

## 3. 아직 안 한 일 / 결정 필요

- [ ] PC에 `hurick-idle` 프로젝트 폴더 만들기 (§5)
- [ ] (선택) GitHub에 `hurick-idle` 저장소 만들기
- [ ] Phaser 버전 결정: 현재 최신은 **Phaser 4.2.1** (2026-10 기준). Phaser 3은 자료·예제가 많고, 4는 최신 렌더러. → 새 프로젝트이므로 **Phaser 4 추천**, 막히는 부분이 많으면 3.x로 전환
- [ ] AI 도트 도구 선택: PixelLab / Retro Diffusion / 에셋 구매 (약관에서 상업 이용·소유권 확인)
- [ ] 영문 제목 상표 검색 (KIPRIS, USPTO)
- [ ] **1주차 개발 — 아직 시작 전** (환경 확인만 함)

## 4. 다음 작업: 1주차 개발 계획

| 순서 | 작업 | 관련 FRD |
|---|---|---|
| 1 | Vite + TypeScript + Phaser 프로젝트 생성, `npm run dev`로 브라우저 실행 | - |
| 2 | 세로 고정, 가로 180px 논리 해상도, 정수 배율·최근접 보간 | SCR-01~03 |
| 3 | 화면 레이아웃 뼈대 (상단 HUD / 전투 영역 / 스킬 바 / 하단 탭) | SCR-05~06 |
| 4 | 코드로 만든 임시 도트 (휴릭 몸 + 무기 레이어, 적 1종) — `tools/sample_sprite.py` 방식 | WPN-05 |
| 5 | 자동 전투: 일정 간격 공격, 적 HP 감소, 처치 시 다음 적 | CBT-01~02 |
| 6 | Stage 진행 + 클리어 시 위로 스크롤 연출 | STG-01~02 |
| 7 | 피해 공식 순수 함수 + Vitest 단위 테스트 (combat §4.1 표 재현) | CBT-04 |

PC의 Claude Code에서 이렇게 요청하면 됩니다:
> `docs/hurick-idle-progress.md`의 "1주차 개발 계획"대로 시작해줘

## 5. PC로 옮기는 방법

### 5.1 위치
- **추천 위치: `C:\Users\audrm\hurick-idle`**
- ⚠ `C:\Users\audrm\.claude\projects`는 **Claude Code가 대화 기록을 자동 저장하는 내부 폴더**입니다. 여기에 프로젝트를 두면 Claude Code 데이터와 섞이고, 정리·초기화 시 지워질 수 있으니 사용하지 마세요.

### 5.2 순서 (PowerShell)

```powershell
# 1) 기획 문서가 있는 브랜치 받기 (이미 받았다면 생략)
cd C:\Users\audrm
git clone -b claude/idle-rpg-game-design-33m7xq https://github.com/mklee-ai/crawl_site.git crawl_site_game

# 2) 새 프로젝트 폴더 만들고 문서 복사
mkdir hurick-idle\docs\assets, hurick-idle\tools
copy crawl_site_game\docs\idle-rpg-*.md      hurick-idle\docs\
copy crawl_site_game\docs\hurick-idle-*.md   hurick-idle\docs\
copy crawl_site_game\docs\assets\hurick-weapon-swap-sample.png hurick-idle\docs\assets\
copy crawl_site_game\docs\assets\sample_sprite.py hurick-idle\tools\

# 3) git 시작
cd hurick-idle
git init -b main
```

그다음 아래 §6의 `CLAUDE.md`, `README.md`, `.gitignore`를 만들고 (또는 Claude Code에게 "progress 문서 §6대로 파일 만들어줘"라고 요청), 첫 커밋을 하면 됩니다.

- 이전에 받은 `hurick-idle.zip`이 있다면 압축을 `C:\Users\audrm\`에 풀고, 이 진행 기록·FRD 문서만 `docs\`에 추가 복사해도 됩니다.
- 이 브랜치의 `docs/` 아래 게임 문서들은 Crawl_site 프로젝트 범위 밖이므로, 옮긴 뒤에는 Crawl_site 쪽 브랜치를 정리해도 됩니다.

## 6. 새 프로젝트 초기 파일

### 6.1 `CLAUDE.md`

```markdown
# CLAUDE.md

이 저장소에서 작업할 때 항상 아래 원칙을 확인하세요.

## 프로젝트

**Sword Emperor Hurick (검제 키우기: 휴릭)** — 세로(Portrait) 고정 픽셀 방치형 RPG, Android 우선.
전체 기획은 `docs/idle-rpg-prd.md`, 전투 공식·무기·스탯은 `docs/idle-rpg-combat.md`,
기능 요구사항은 `docs/hurick-idle-frd.md`, 진행 상황은 `docs/hurick-idle-progress.md`가 기준입니다.

## 핵심 설계 원칙 (변경 시 사용자 확인 필요)

- 스탯은 STAB(찌르기)·HACK(베기)·INT(마력) 3종
- 무기 종류 사이에 상하 관계 없음 — 모든 종류의 기본 DPS 동일, 공속과 1타 공격력은 반비례
- 무기 차이는 적의 방어 특성(물리/마법 방어력, 결계, 슈퍼아머, 재생)에서 드러나야 함
- 강해지는 축은 무기 아이템의 등급·강화·옵션 (종류가 아님)
- 시작 무기는 평도, Stage 진행으로 새 무기 해금

## 기술 스택

- Phaser + TypeScript (`pixelArt: true`), Vite, Capacitor(Android)
- 논리 해상도 가로 180px 고정, 정수 배율 확대, 최근접 보간
- 수치·텍스트는 코드에 하드코딩하지 말고 `src/data/*.json`, `src/locales/{ko,en}.json`으로 관리
- 피해 계산 등 게임 공식은 순수 함수로 두고 `tests/`에 단위 테스트 (문서의 예시 표 수치를 테스트로 고정)

## 폴더 구조

- `docs/` — 기획서/설계 문서 (옵시디언용, 마크다운 + frontmatter)
- `src/scenes/`, `src/systems/`, `src/data/`, `src/locales/`, `src/ui/` — 게임 코드
- `assets/sprites/`, `assets/fonts/` — 그래픽·폰트
- `tools/` — 도트 생성·팔레트 변환 등 보조 스크립트
- `tests/` — 단위 테스트

## 규칙

- 저장소·폴더·파일 이름은 영어. 문서 내용과 게임 텍스트는 한글 사용 가능
- 외부 에셋·폰트·AI 생성 그래픽은 상업적 이용 라이선스를 확인한 뒤에만 추가하고, 출처를 `assets/CREDITS.md`에 기록
- 작업이 끝나면 `docs/hurick-idle-progress.md`의 진행 기록을 갱신
- 코드는 함수/모듈 단위로 작게 유지
```

### 6.2 `README.md`

```markdown
# Sword Emperor Hurick (검제 키우기: 휴릭)

세로형 픽셀 방치형 RPG. Android 우선, 한국어·영어 지원.

떠돌이 검사 휴릭이 하늘에 닿은 종탑을 오르며, 모든 무기를 다루는 "검제"가 되어 가는 이야기.

- 기획서: docs/idle-rpg-prd.md
- 전투·무기·스탯 설계: docs/idle-rpg-combat.md
- 기능 요구사항: docs/hurick-idle-frd.md
- 진행 기록: docs/hurick-idle-progress.md
```

### 6.3 `.gitignore`

```
node_modules/
dist/
.vite/
*.log
.DS_Store
android/app/build/
android/.gradle/
*.keystore
*.jks
```

## 7. 문서 목록

| 파일 | 내용 |
|---|---|
| `idle-rpg-prd.md` | PRD v0.3 — 개요, 스토리, 화면, 루프, 아트, 기술, MVP, 이름 검토 |
| `idle-rpg-combat.md` | 전투·무기·스탯 v0.2 — 공식, 무기 8종, 방어 특성, 스킬, 옵션 |
| `hurick-idle-frd.md` | FRD v0.1 — 기능 요구사항 ID·우선순위·완료 기준 |
| `hurick-idle-progress.md` | 이 문서 — 진행 기록, 다음 작업, PC 이전 방법 |
| `assets/hurick-weapon-swap-sample.png` | Claude Code 도트 샘플 |
| `assets/sample_sprite.py` | 샘플 도트 생성 스크립트 (새 프로젝트에서는 `tools/`로 이동). 실행: `python sample_sprite.py out.png` (Pillow 필요) |
