"""무신사 랭킹 페이지에서 순위/브랜드/상품명/가격/리뷰 등 텍스트 정보만 수집.

이미지는 수집하지 않는다 (프로젝트 원칙: 브랜드 사이트 이미지 직접 크롤링 금지).

주의: 아래 CSS 셀렉터는 라이브 검증이 안 된 상태다. 이 코드를 작성한 환경은
네트워크 정책상 musinsa.com에 접근할 수 없어 실제 페이지 구조를 확인하지
못했다. 실행 전 브라우저 개발자 도구로 실제 셀렉터를 확인해 갱신할 것.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass

from bs4 import BeautifulSoup

from crawlers.common.http_client import RateLimitedSession
from crawlers.common.storage import save_json

RANKING_URL = "https://www.musinsa.com/main/musinsa/ranking"


@dataclass
class RankingItem:
    rank: int
    brand: str
    product_name: str
    price: str | None
    review_count: str | None
    rating: str | None
    product_url: str | None


def fetch_ranking(session: RateLimitedSession, url: str = RANKING_URL) -> list[RankingItem]:
    response = session.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    items: list[RankingItem] = []
    for rank, card in enumerate(soup.select(".ranking-item"), start=1):  # TODO: 실제 셀렉터 확인 필요
        brand = card.select_one(".brand")
        name = card.select_one(".product-name")
        price = card.select_one(".price")
        review_count = card.select_one(".review-count")
        rating = card.select_one(".rating")
        link = card.select_one("a")

        items.append(
            RankingItem(
                rank=rank,
                brand=brand.get_text(strip=True) if brand else "",
                product_name=name.get_text(strip=True) if name else "",
                price=price.get_text(strip=True) if price else None,
                review_count=review_count.get_text(strip=True) if review_count else None,
                rating=rating.get_text(strip=True) if rating else None,
                product_url=link["href"] if link and link.has_attr("href") else None,
            )
        )
    return items


def run(url: str = RANKING_URL) -> None:
    session = RateLimitedSession()
    items = fetch_ranking(session, url)
    out_path = save_json([asdict(item) for item in items], source="musinsa", category="ranking")
    print(f"저장 완료: {out_path} ({len(items)}건)")


if __name__ == "__main__":
    run()
