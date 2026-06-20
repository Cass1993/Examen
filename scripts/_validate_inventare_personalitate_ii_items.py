"""Verifică consistența itemilor Inventare de personalitate II (11446–11725)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.inventare_personalitate_ii_comparatii_bank_data import COMPARATII_ITEMS
from scripts.inventare_personalitate_ii_comparatii_explanations import COMPARATII_EXPLANATIONS
from scripts.inventare_personalitate_ii_cpi_bank_data import CPI_ITEMS, _count_dist
from scripts.inventare_personalitate_ii_cpi_explanations import CPI_EXPLANATIONS
from scripts.inventare_personalitate_ii_epq_bank_data import EPQ_IVE_ITEMS
from scripts.inventare_personalitate_ii_epq_explanations import EPQ_IVE_EXPLANATIONS
from scripts.inventare_personalitate_ii_exam_items import LOT_NAME, START_ID, build_items
from scripts.inventare_personalitate_ii_fpi_bank_data import FPI_ITEMS
from scripts.inventare_personalitate_ii_fpi_explanations import FPI_EXPLANATIONS
from scripts.inventare_personalitate_ii_neo_bank_data import NEO_PI_R_ITEMS
from scripts.inventare_personalitate_ii_neo_explanations import NEO_PI_R_EXPLANATIONS
from scripts.ii_grila_meta_audit import audit_grila_meta_stem

LETTER_MARKERS = re.compile(
    r"✅|❌|Varianta [abcd]|varianta [abcd]|Corect:\s*[abcd]|Greșit",
    re.IGNORECASE,
)
OBVIOUS_WRONG = re.compile(
    r"\b(doar de|exclusiv de|absența oricărei|eliminarea oricărei|"
    r"în grilă|pentru grilă|la grilă)\b",
    re.IGNORECASE,
)

SEG_DIST_60 = {"1": 22, "2": 14, "3": 12, "4": 6, "TF": 6}
SEG_DIST_50 = {"1": 18, "2": 12, "3": 10, "4": 5, "TF": 5}
SEG_DIST_80 = {"1": 29, "2": 19, "3": 16, "4": 8, "TF": 8}
SEG_DIST_30 = {"1": 11, "2": 7, "3": 6, "4": 3, "TF": 3}
TOTAL_ITEMS = 280


def main() -> int:
    built = build_items()
    issues: list[str] = []

    if len(built) != TOTAL_ITEMS:
        issues.append(f"număr itemi: {len(built)}, așteptat {TOTAL_ITEMS}")

    segments = [
        ("CPI", CPI_ITEMS, CPI_EXPLANATIONS, SEG_DIST_60),
        ("EPQ/IVE", EPQ_IVE_ITEMS, EPQ_IVE_EXPLANATIONS, SEG_DIST_60),
        ("FPI", FPI_ITEMS, FPI_EXPLANATIONS, SEG_DIST_50),
        ("NEO PI-R", NEO_PI_R_ITEMS, NEO_PI_R_EXPLANATIONS, SEG_DIST_80),
        ("Comparații", COMPARATII_ITEMS, COMPARATII_EXPLANATIONS, SEG_DIST_30),
    ]
    for name, items, explanations, expected_dist in segments:
        if len(items) != len(explanations):
            issues.append(
                f"{name}: itemi ({len(items)}) ≠ explicații ({len(explanations)})"
            )
        dist = _count_dist(items)
        if dist != expected_dist:
            issues.append(f"{name} distribuție: {dist}, așteptat {expected_dist}")

    for q in built:
        qid = int(q["id"])
        if not (START_ID <= qid <= START_ID + TOTAL_ITEMS - 1):
            issues.append(
                f"{qid}: ID în afara intervalului "
                f"{START_ID}–{START_ID + TOTAL_ITEMS - 1}"
            )
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
    print(f"OK: {TOTAL_ITEMS} itemi {LOT_NAME}.")
    print(f"CPI: {_count_dist(CPI_ITEMS)}")
    print(f"EPQ/IVE: {_count_dist(EPQ_IVE_ITEMS)}")
    print(f"FPI: {_count_dist(FPI_ITEMS)}")
    print(f"NEO PI-R: {_count_dist(NEO_PI_R_ITEMS)}")
    print(f"Comparații: {_count_dist(COMPARATII_ITEMS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
