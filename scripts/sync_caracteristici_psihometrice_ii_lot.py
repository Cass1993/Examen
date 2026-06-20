"""Rescrie lotul Caracteristici psihometrice II în questions.json din cod."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.caracteristici_psihometrice_ii_exam_items import LOT_NAME, build_items  # noqa: E402

QUESTIONS_JSON = ROOT / "data" / "questions.json"


def main() -> int:
    built = build_items()
    data = json.loads(QUESTIONS_JSON.read_text(encoding="utf-8"))
    old_n = len(data.get("lots", {}).get(LOT_NAME, {}).get("questions") or [])
    data.setdefault("lots", {})[LOT_NAME] = {"questions": built}
    data["total_questions"] = sum(
        len(b.get("questions") or []) for b in data.get("lots", {}).values()
    )
    QUESTIONS_JSON.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with_expl = sum(1 for q in built if str(q.get("explanation") or "").strip())
    print(f"Lot: {LOT_NAME}")
    print(f"Înainte: {old_n} → acum: {len(built)} (cu explicație: {with_expl})")
    print(f"11246: {str(built[0].get('text', ''))[:70]}...")
    print(f"11445: {str(built[-1].get('text', ''))[:70]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
