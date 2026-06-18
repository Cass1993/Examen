"""Injectează explicațiile în data/questions.json pentru lotul evaluare II."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluare_psihologica_ii_exam_items import LOT_NAME, build_items  # noqa: E402

QUESTIONS_JSON = ROOT / "data" / "questions.json"


def main() -> int:
    built = {int(q["id"]): q for q in build_items()}
    id_min, id_max = 9001, 9360
    data = json.loads(QUESTIONS_JSON.read_text(encoding="utf-8"))
    questions = data.get("lots", {}).get(LOT_NAME, {}).get("questions") or []
    patched = 0
    for q in questions:
        qid = int(q.get("id") or 0)
        src = built.get(qid)
        if not src:
            continue
        expl = str(src.get("explanation") or "").strip()
        if expl and q.get("explanation") != expl:
            q["explanation"] = expl
            patched += 1
    QUESTIONS_JSON.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with_expl = sum(1 for q in questions if str(q.get("explanation") or "").strip())
    print(f"Lot: {LOT_NAME}")
    print(f"Întrebări: {len(questions)}, cu explicație: {with_expl}, actualizate acum: {patched}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
