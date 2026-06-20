"""Verifică consistența itemilor Psihologia învățării II (10501–10960)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.psihologia_invatarii_ii_exam_items import LOT_NAME, START_ID, build_items  # noqa: E402
from scripts.psihologia_invatarii_ii_explanations import explanation_for_exam_id  # noqa: E402

LETTER_MARKERS = re.compile(
    r"✅|❌|Varianta [abcd]|varianta [abcd]|Corect:\s*[abcd]|Greșit",
    re.IGNORECASE,
)


def main() -> int:
    built = build_items()
    data = json.loads((ROOT / "data" / "questions.json").read_text(encoding="utf-8"))
    json_lot = data.get("lots", {}).get(LOT_NAME, {}).get("questions") or []
    issues: list[str] = []

    expected_n = 460
    if len(built) != expected_n:
        issues.append(f"build_items: așteptat {expected_n}, primit {len(built)}")
    if len(json_lot) != expected_n:
        issues.append(f"questions.json: așteptat {expected_n}, primit {len(json_lot)}")

    for q in built:
        qid = int(q["id"])
        if not (10501 <= qid <= 10960):
            issues.append(f"{qid}: ID în afara intervalului 10501–10960")
        if not str(q.get("text") or "").strip():
            issues.append(f"{qid}: enunț gol")
        if not q.get("options"):
            issues.append(f"{qid}: fără opțiuni")
        if not q.get("correct"):
            issues.append(f"{qid}: fără barem")
        expl = str(q.get("explanation") or "").strip()
        if not expl:
            issues.append(f"{qid}: fără explicație în build_items")
        if LETTER_MARKERS.search(expl):
            issues.append(f"{qid}: explicație cu marcaje a/b/c/d")
        if not explanation_for_exam_id(qid).strip():
            issues.append(f"{qid}: explanation_for_exam_id gol")

    json_ids = sorted(int(q["id"]) for q in json_lot)
    expected_ids = list(range(START_ID, START_ID + expected_n))
    if json_ids != expected_ids:
        missing = set(expected_ids) - set(json_ids)
        extra = set(json_ids) - set(expected_ids)
        if missing:
            issues.append(f"JSON lipsesc ID-uri: {sorted(missing)[:10]}")
        if extra:
            issues.append(f"JSON ID-uri în plus: {sorted(extra)[:10]}")

    if not issues:
        with_expl = sum(1 for q in built if str(q.get("explanation") or "").strip())
        print(f"OK: {len(built)} itemi ({START_ID}–{START_ID + len(built) - 1})")
        print(f"JSON sincronizat: {len(json_lot)} itemi, explicații: {with_expl}/{expected_n}")
        return 0

    print(f"Probleme ({len(issues)}):")
    for line in issues[:80]:
        print(f"  - {line}")
    if len(issues) > 80:
        print(f"  ... și încă {len(issues) - 80}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
