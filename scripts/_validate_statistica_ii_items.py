"""Verifică consistența itemilor Statistică II (10961–11050)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.ii_grila_meta_audit import audit_grila_meta_stem  # noqa: E402
from scripts.statistica_ii_exam_items import build_items  # noqa: E402
from scripts.statistica_ii_explanations import STATISTICA_II_EXPLANATIONS  # noqa: E402
from scripts.statistica_ii_bank_data import STATISTICA_II_ITEMS  # noqa: E402
from scripts.statistica_ii_scales_sampling_bank_data import SCALES_SAMPLING_ITEMS  # noqa: E402

LETTER_MARKERS = re.compile(
    r"✅|❌|Varianta [abcd]|varianta [abcd]|Corect:\s*[abcd]|Greșit",
    re.IGNORECASE,
)
OBVIOUS_WRONG = re.compile(
    r"\b(doar de|exclusiv de|absența oricărei|eliminarea oricărei|"
    r"în grilă|pentru grilă|la grilă)\b",
    re.IGNORECASE,
)


def _count_dist(rows: list) -> dict[str, int]:
    counts = {"1": 0, "2": 0, "3": 0, "4": 0, "TF": 0}
    for row in rows:
        if row.get("tf"):
            counts["TF"] += 1
            continue
        letters = "".join(sorted(set(str(row.get("correct") or "").lower())))
        n = len(letters)
        if 1 <= n <= 4:
            counts[str(n)] += 1
    return counts


def main() -> int:
    built = build_items()
    issues: list[str] = []

    if len(built) != 90:
        issues.append(f"număr itemi: {len(built)}, așteptat 90")

    if len(STATISTICA_II_ITEMS) != 90:
        issues.append(f"STATISTICA_II_ITEMS: {len(STATISTICA_II_ITEMS)}, așteptat 90")

    if len(STATISTICA_II_EXPLANATIONS) != 90:
        issues.append(
            f"STATISTICA_II_EXPLANATIONS: {len(STATISTICA_II_EXPLANATIONS)}, așteptat 90"
        )

    counts = _count_dist(STATISTICA_II_ITEMS)
    seg2 = _count_dist(SCALES_SAMPLING_ITEMS)

    if counts["TF"] != 9:
        issues.append(f"TF total: {counts['TF']} (așteptat 9 ≈10%)")
    if seg2["TF"] != 5:
        issues.append(f"TF segment 2: {seg2['TF']} (așteptat 5)")
    if not (seg2["1"] > seg2["2"] > seg2["3"] > seg2["4"]):
        issues.append(f"distribuție segment 2: {seg2}")

    for q in built:
        qid = int(q["id"])
        if not (10961 <= qid <= 11050):
            issues.append(f"{qid}: ID în afara intervalului 10961–11050")
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
        if len(opts) == 4 and q.get("kind") != "single":
            pass
        elif opts and len(opts) not in (2, 4):
            issues.append(f"{qid}: număr opțiuni neobișnuit: {len(opts)}")

    if issues:
        print("PROBLEME:")
        for i in issues:
            print(i)
        return 1
    print("OK: 90 itemi Statistică II.")
    print(f"Distribuție totală: {counts}")
    print(f"Distribuție segment 2 (11001–11050): {seg2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
