"""수집 결과를 data/raw 아래 JSON으로 저장하는 유틸리티."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

DATA_RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def save_json(records: list[dict], source: str, category: str) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = DATA_RAW_DIR / source
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{category}_{timestamp}.json"
    out_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path
