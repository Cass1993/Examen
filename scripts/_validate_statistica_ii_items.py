"""Verifică consistența itemilor Statistică II (10961–11245)."""

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
from scripts.statistica_ii_anova_bank_data import ANOVA_ITEMS  # noqa: E402

LETTER_MARKERS = re.compile(
    r"✅|❌|Varianta [abcd]|varianta [abcd]|Corect:\s*[abcd]|Greșit",
    re.IGNORECASE,
)
OBVIOUS_WRONG = re.compile(
    r"\b(doar de|exclusiv de|absența oricărei|eliminarea oricărei|"
    r"în grilă|pentru grilă|la grilă)\b",
    re.IGNORECASE,
)

SEG_DIST_20 = {"1": 7, "2": 5, "3": 4, "4": 2, "TF": 2}


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

    if len(built) != 285:
        issues.append(f"număr itemi: {len(built)}, așteptat 285")

    if len(STATISTICA_II_ITEMS) != 285:
        issues.append(f"STATISTICA_II_ITEMS: {len(STATISTICA_II_ITEMS)}, așteptat 285")

    if len(STATISTICA_II_EXPLANATIONS) != 285:
        issues.append(
            f"STATISTICA_II_EXPLANATIONS: {len(STATISTICA_II_EXPLANATIONS)}, așteptat 285"
        )

    counts = _count_dist(STATISTICA_II_ITEMS)
    seg12 = _count_dist(ANOVA_ITEMS)

    if counts["TF"] != 28:
        issues.append(f"TF total: {counts['TF']} (așteptat 28 ≈10%)")
    if seg12 != SEG_DIST_20:
        issues.append(f"distribuție segment 12 (ANOVA): {seg12}, așteptat {SEG_DIST_20}")

    for q in built:
        qid = int(q["id"])
        if not (10961 <= qid <= 11245):
            issues.append(f"{qid}: ID în afara intervalului 10961–11245")
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
    print("OK: 285 itemi Statistică II.")
    print(f"Distribuție totală: {counts}")
    print(f"Segment 12 (11226–11245): {seg12}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
