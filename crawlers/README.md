# crawlers

무신사/네이버 등에서 상품 랭킹·순위·리뷰 텍스트 정보를 수집하는 크롤링 스크립트/모듈입니다.

- 브랜드 사이트 이미지 직접 크롤링 금지 — 텍스트 정보(순위, 브랜드, 상품명, 가격, 리뷰 수, 평점)만 수집
- 요청 전 매번 robots.txt를 확인하고, 사이트가 지정한 crawl-delay(없으면 기본 2초)를 지킴
- 네이버는 HTML 스크레이핑 대신 공식 오픈 API 사용

## 설치

```bash
pip install -r requirements.txt
cp .env.example .env  # NAVER_CLIENT_ID / NAVER_CLIENT_SECRET 입력
```

## 구조

```
crawlers/
  common/
    robots.py       robots.txt 확인
    http_client.py  robots.txt 준수 + 요청 간 지연을 강제하는 HTTP 세션
    storage.py      data/raw/<source>/ 아래 JSON 저장
  musinsa/
    ranking.py       무신사 랭킹 페이지 스크레이핑 (셀렉터 라이브 검증 필요, 코드 내 TODO 참고)
  naver/
    shopping_api.py  네이버 쇼핑 공식 오픈 API 조회
  run.py             CLI 진입점
```

## 실행

```bash
python -m crawlers.run musinsa-ranking
python -m crawlers.run naver-search --query "티셔츠"
```

## 알려진 제약

`musinsa/ranking.py`의 CSS 셀렉터는 실제 페이지에서 검증되지 않았습니다. 이 코드가 작성된
환경은 네트워크 정책상 musinsa.com에 접근할 수 없어, 실행 전 브라우저 개발자 도구로 실제
페이지 구조를 확인하고 셀렉터를 갱신해야 합니다.
