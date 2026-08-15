"""크롤러 실행 진입점.

사용 예:
    python -m crawlers.run musinsa-ranking
    python -m crawlers.run naver-search --query "티셔츠"
"""
from __future__ import annotations

import argparse
from dataclasses import asdict

from crawlers.common.storage import save_json
from crawlers.musinsa.ranking import run as run_musinsa_ranking
from crawlers.naver.shopping_api import search as naver_search


def main() -> None:
    parser = argparse.ArgumentParser(description="크롤러 실행")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("musinsa-ranking", help="무신사 랭킹 페이지 수집")

    naver_parser = subparsers.add_parser("naver-search", help="네이버 쇼핑 검색 API 조회")
    naver_parser.add_argument("--query", required=True)
    naver_parser.add_argument("--display", type=int, default=20)

    args = parser.parse_args()

    if args.command == "musinsa-ranking":
        run_musinsa_ranking()
    elif args.command == "naver-search":
        items = naver_search(args.query, display=args.display)
        out_path = save_json([asdict(item) for item in items], source="naver", category="search")
        print(f"저장 완료: {out_path} ({len(items)}건)")


if __name__ == "__main__":
    main()
