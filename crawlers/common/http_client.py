"""robots.txt 확인과 요청 간 지연을 강제하는 HTTP 클라이언트."""
from __future__ import annotations

import time

import requests

from crawlers.common.robots import RobotsChecker

DEFAULT_USER_AGENT = "CrawlSiteBot/0.1 (+contact: audrms5745@gmail.com)"


class PolitelyFetchBlocked(Exception):
    """robots.txt가 해당 URL에 대한 접근을 허용하지 않을 때 발생."""


class RateLimitedSession:
    def __init__(
        self,
        user_agent: str = DEFAULT_USER_AGENT,
        min_delay_seconds: float = 2.0,
        timeout: float = 10.0,
    ):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": user_agent})
        self.robots = RobotsChecker(user_agent=user_agent)
        self.min_delay_seconds = min_delay_seconds
        self.timeout = timeout
        self._last_request_at: float | None = None

    def get(self, url: str, **kwargs) -> requests.Response:
        if not self.robots.can_fetch(url):
            raise PolitelyFetchBlocked(f"robots.txt에 의해 접근이 차단됨: {url}")

        delay = self.robots.crawl_delay(url) or self.min_delay_seconds
        if self._last_request_at is not None:
            remaining = delay - (time.monotonic() - self._last_request_at)
            if remaining > 0:
                time.sleep(remaining)

        response = self.session.get(url, timeout=self.timeout, **kwargs)
        self._last_request_at = time.monotonic()
        response.raise_for_status()
        return response
