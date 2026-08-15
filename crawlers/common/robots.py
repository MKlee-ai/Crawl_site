"""robots.txt를 확인해 크롤링 허용 여부를 판단하는 유틸리티."""
from __future__ import annotations

from urllib import robotparser
from urllib.parse import urlparse


class RobotsChecker:
    def __init__(self, user_agent: str = "*"):
        self.user_agent = user_agent
        self._parsers: dict[str, robotparser.RobotFileParser] = {}

    def _get_parser(self, url: str) -> robotparser.RobotFileParser:
        parsed = urlparse(url)
        origin = f"{parsed.scheme}://{parsed.netloc}"
        if origin not in self._parsers:
            parser = robotparser.RobotFileParser()
            parser.set_url(f"{origin}/robots.txt")
            parser.read()
            self._parsers[origin] = parser
        return self._parsers[origin]

    def can_fetch(self, url: str) -> bool:
        return self._get_parser(url).can_fetch(self.user_agent, url)

    def crawl_delay(self, url: str) -> float | None:
        delay = self._get_parser(url).crawl_delay(self.user_agent)
        return float(delay) if delay is not None else None
