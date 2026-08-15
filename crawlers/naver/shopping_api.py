"""네이버 쇼핑 공식 오픈 API로 상품 정보를 조회.

HTML 스크레이핑 대신 공식 API를 쓰는 이유: shopping.naver.com은 이용약관상
자동화된 스크레이핑을 제한하며, 네이버는 검색 결과에 한해 공식 오픈 API
(개발자센터, https://developers.naver.com)를 제공한다. API 키는
.env의 NAVER_CLIENT_ID / NAVER_CLIENT_SECRET로 설정한다.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass

import requests

API_URL = "https://openapi.naver.com/v1/search/shop.json"
_TAG_RE = re.compile(r"</?b>")


@dataclass
class ShoppingItem:
    title: str
    link: str
    lprice: str
    mall_name: str
    brand: str
    category: str


def _strip_highlight_tags(text: str) -> str:
    return _TAG_RE.sub("", text)


def search(query: str, display: int = 20, sort: str = "sim") -> list[ShoppingItem]:
    client_id = os.environ.get("NAVER_CLIENT_ID")
    client_secret = os.environ.get("NAVER_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise RuntimeError("NAVER_CLIENT_ID / NAVER_CLIENT_SECRET 환경변수가 필요합니다.")

    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
    }
    params = {"query": query, "display": display, "sort": sort}
    response = requests.get(API_URL, headers=headers, params=params, timeout=10)
    response.raise_for_status()

    return [
        ShoppingItem(
            title=_strip_highlight_tags(raw.get("title", "")),
            link=raw.get("link", ""),
            lprice=raw.get("lprice", ""),
            mall_name=raw.get("mallName", ""),
            brand=raw.get("brand", ""),
            category=raw.get("category1", ""),
        )
        for raw in response.json().get("items", [])
    ]
