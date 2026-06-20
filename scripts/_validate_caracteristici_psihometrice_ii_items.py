"""Verifică consistența itemilor Caracteristici psihometrice II (11246–11445)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.caracteristici_psihometrice_ii_bank_data import (  # noqa: E402
    CARACTERISTICI_PSIHOMETRICE_II_ITEMS,
    _count_dist,
)
from scripts.caracteristici_psihometrice_ii_exam_items import (  # noqa: E402
    LOT_NAME,
    START_ID,
    build_items,
)
from scripts.caracteristici_psihometrice_ii_explanations import (  # noqa: E402
    CARACTERISTICI_PSIHOMETRICE_II_EXPLANATIONS,
)
from scripts.caracteristici_psihometrice_ii_fidelitate_bank_data import (  # noqa: E402
    FIDELITATE_TEST_ITEMS,
)
from scripts.caracteristici_psihometrice_ii_selecie_profesionala_bank_data import (  # noqa: E402
    SELECIE_PROFESIONALA_ITEMS,
)
from scripts.caracteristici_psihometrice_ii_validitate_bank_data import (  # noqa: E402
    VALIDITATE_TEST_ITEMS,
)
from scripts.ii_grila_meta_audit import audit_grila_meta_stem  # noqa: E402

LETTER_MARKERS = re.compile(
    r"✅|❌|Varianta [abcd]|varianta [abcd]|Corect:\s*[abcd]|Greșit",
    re.IGNORECASE,
)
OBVIOUS_WRONG = re.compile(
    r"\b(doar de|exclusiv de|absența oricărei|eliminarea oricărei|"
    r"în grilă|pentru grilă|la grilă)\b",
    re.IGNORECASE,
)

SEG_DIST_50 = {"1": 18, "2": 12, "3": 10, "4": 5, "TF": 5}
SEG_DIST_60 = {"1": 22, "2": 14, "3": 12, "4": 6, "TF": 6}
SEG_DIST_40 = {"1": 14, "2": 10, "3": 8, "4": 4, "TF": 4}
SEG_DIST_200 = {"1": 72, "2": 48, "3": 40, "4": 20, "TF": 20}


def main() -> int:
    built = build_items()
    issues: list[str] = []

    if len(built) != 200:
        issues.append(f"număr itemi: {len(built)}, așteptat 200")

    if len(CARACTERISTICI_PSIHOMETRICE_II_ITEMS) != 200:
        issues.append(f"bank: {len(CARACTERISTICI_PSIHOMETRICE_II_ITEMS)}, așteptat 200")

    if len(CARACTERISTICI_PSIHOMETRICE_II_EXPLANATIONS) != 200:
        issues.append(
            f"explicații: {len(CARACTERISTICI_PSIHOMETRICE_II_EXPLANATIONS)}, așteptat 200"
        )

    total = _count_dist(CARACTERISTICI_PSIHOMETRICE_II_ITEMS)
    seg4 = _count_dist(SELECIE_PROFESIONALA_ITEMS)
    seg3 = _count_dist(VALIDITATE_TEST_ITEMS)
    seg2 = _count_dist(FIDELITATE_TEST_ITEMS)
    seg1 = {k: total[k] - seg2[k] - seg3[k] - seg4[k] for k in total}

    if total != SEG_DIST_200:
        issues.append(f"distribuție totală: {total}, așteptat {SEG_DIST_200}")
    if seg4 != SEG_DIST_40:
        issues.append(f"distribuție segment 4 (selecție): {seg4}, așteptat {SEG_DIST_40}")
    if seg3 != SEG_DIST_60:
        issues.append(f"distribuție segment 3 (validitate): {seg3}, așteptat {SEG_DIST_60}")
    if seg2 != SEG_DIST_50:
        issues.append(f"distribuție segment 2 (fidelitate): {seg2}, așteptat {SEG_DIST_50}")
    if seg1 != SEG_DIST_50:
        issues.append(f"distribuție segment 1 (intro): {seg1}, așteptat {SEG_DIST_50}")

    for q in built:
        qid = int(q["id"])
        if not (START_ID <= qid <= START_ID + 199):
            issues.append(f"{qid}: ID în afara intervalului {START_ID}–{START_ID + 199}")
        stem = str(q.get("text") or "").strip()
        if not stem:
            issues.append(f"{qid}: enunț gol")
        for issue in audit_grila_meta_stem(stem):
            issues.append(f"{qid}: [{issue.rule}] {issue.message}")
        expl = str(q.get("explanation") or "").strip()
        if not expl:
            issues.append(f"{qid}: fără explicație")
        if LETTER_MARKERS.search(expl):
            issues.append(f"{qid}: explicație cu marcaje a/b/c/d")
        opts = q.get("options") or {}
        for letter, text in opts.items():
            if OBVIOUS_WRONG.search(str(text)):
                issues.append(f"{qid}: variantă suspectă ({letter}): {str(text)[:60]}")
        if opts and len(opts) not in (2, 4):
            issues.append(f"{qid}: număr opțiuni neobișnuit: {len(opts)}")

    if issues:
        print("PROBLEME:")
        for i in issues:
            print(i)
        return 1
    print(f"OK: 200 itemi {LOT_NAME}.")
    print(f"Distribuție totală: {total}")
    print(f"Segment 4 (11406–11445): {seg4}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
