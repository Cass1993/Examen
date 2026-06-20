"""Verifică consistența itemilor Epigenetica II: BAZE MOLECULARE (11726–11935)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.epigenetica_ii_baze_moleculare_bank_data import (
    BAZE_MOLECULARE_ITEMS,
    _count_dist,
)
from scripts.epigenetica_ii_baze_moleculare_explanations import (
    BAZE_MOLECULARE_EXPLANATIONS,
)
from scripts.epigenetica_ii_baze_moleculare_exam_items import (
    LOT_NAME,
    START_ID,
    build_items,
)
from scripts.epigenetica_ii_epigenetica_bank_data import (
    EPIGENETICA_ITEMS,
    SEG_DIST_50 as SEG_DIST_EPIG,
)
from scripts.epigenetica_ii_epigenetica_explanations import EPIGENETICA_EXPLANATIONS
from scripts.epigenetica_ii_genetica_comportamentala_bank_data import (
    GENETICA_COMPORTAMENTALA_ITEMS,
    SEG_DIST_50 as SEG_DIST_GC,
)
from scripts.epigenetica_ii_genetica_comportamentala_explanations import (
    GENETICA_COMPORTAMENTALA_EXPLANATIONS,
)
from scripts.epigenetica_ii_patologii_genetice_bank_data import (
    PATOLOGII_GENETICE_ITEMS,
    SEG_DIST_30,
)
from scripts.epigenetica_ii_patologii_genetice_explanations import (
    PATOLOGII_GENETICE_EXPLANATIONS,
)
from scripts.epigenetica_ii_psihologie_legatura_bank_data import (
    PSIHOLOGIE_LEGATURA_ITEMS,
    SEG_DIST_30 as SEG_DIST_PSYCH,
)
from scripts.epigenetica_ii_psihologie_legatura_explanations import (
    PSIHOLOGIE_LEGATURA_EXPLANATIONS,
)

OBVIOUS_WRONG = re.compile(
    r"\b(doar de|exclusiv de|absența oricărei|eliminarea oricărei|"
    r"în grilă|pentru grilă|la grilă)\b",
    re.IGNORECASE,
)

SEG_DIST_50 = {"1": 18, "2": 12, "3": 10, "4": 5, "TF": 5}
TOTAL_ITEMS = 210


def main() -> int:
    built = build_items()
    issues: list[str] = []

    if len(built) != TOTAL_ITEMS:
        issues.append(f"număr itemi: {len(built)}, așteptat {TOTAL_ITEMS}")

    segments = [
        (
            "Baze moleculare",
            BAZE_MOLECULARE_ITEMS,
            BAZE_MOLECULARE_EXPLANATIONS,
            SEG_DIST_50,
        ),
        (
            "Patologii genetice",
            PATOLOGII_GENETICE_ITEMS,
            PATOLOGII_GENETICE_EXPLANATIONS,
            SEG_DIST_30,
        ),
        (
            "Genetică comportamentală",
            GENETICA_COMPORTAMENTALA_ITEMS,
            GENETICA_COMPORTAMENTALA_EXPLANATIONS,
            SEG_DIST_GC,
        ),
        (
            "Epigenetică",
            EPIGENETICA_ITEMS,
            EPIGENETICA_EXPLANATIONS,
            SEG_DIST_EPIG,
        ),
        (
            "Legătură psihologie",
            PSIHOLOGIE_LEGATURA_ITEMS,
            PSIHOLOGIE_LEGATURA_EXPLANATIONS,
            SEG_DIST_PSYCH,
        ),
    ]
    for name, items, explanations, expected_dist in segments:
        if len(items) != len(explanations):
            issues.append(
                f"{name}: itemi ({len(items)}) ≠ explicații ({len(explanations)})"
            )
        for i, row in enumerate(items):
            if not row.get("tf"):
                opts = row.get("options") or []
                if len(opts) != 4:
                    issues.append(
                        f"{name} #{i + 1}: {len(opts)} opțiuni (așteptat 4)"
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
        expl = str(q.get("explanation") or "").strip()
        if not expl:
            issues.append(f"{qid}: fără explicație")
        opts = q.get("options") or {}
        for letter, text in opts.items():
            if OBVIOUS_WRONG.search(str(text)):
                issues.append(f"{qid}: distractor suspect ({letter}): {text[:60]}")
        if str(q.get("domeniu") or "") != LOT_NAME:
            issues.append(f"{qid}: domeniu greșit ({q.get('domeniu')})")

    if issues:
        print(f"EȘEC — {len(issues)} probleme:")
        for issue in issues:
            print(f"  - {issue}")
        return 1

    print(f"OK — {LOT_NAME}: {TOTAL_ITEMS} itemi")
    print(f"  Baze: 50 | Patologii: 30 | Gen. comp.: 50 | Epigenetică: 50 | Psihologie: 30")
    print(f"  ID {START_ID}–{START_ID + TOTAL_ITEMS - 1}, toate cu explicație")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
