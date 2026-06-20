"""Verifică consistența itemilor Psihologia personalității II (11936–12225)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.psihologia_personalitatii_ii_ce_este_bank_data import (
    CE_ESTE_PERSONALITATEA_ITEMS,
    SEG_DIST_30,
    _count_dist,
)
from scripts.psihologia_personalitatii_ii_ce_este_explanations import (
    CE_ESTE_PERSONALITATEA_EXPLANATIONS,
)
from scripts.psihologia_personalitatii_ii_dispozitionala_trasaturi_bank_data import (
    DISPOZITIONALA_TRASATURI_ITEMS,
    SEG_DIST_50,
)
from scripts.psihologia_personalitatii_ii_dispozitionala_trasaturi_explanations import (
    DISPOZITIONALA_TRASATURI_EXPLANATIONS,
)
from scripts.psihologia_personalitatii_ii_exam_items import (
    LOT_NAME,
    START_ID,
    build_items,
)
from scripts.psihologia_personalitatii_ii_neo_psihanalitica_bank_data import (
    NEO_PSIHANALITICA_ITEMS,
    SEG_DIST_30 as SEG_DIST_NEO,
)
from scripts.psihologia_personalitatii_ii_neo_psihanalitica_explanations import (
    NEO_PSIHANALITICA_EXPLANATIONS,
)
from scripts.psihologia_personalitatii_ii_psihodinamica_freud_bank_data import (
    PSIHODINAMICA_FREUD_ITEMS,
    SEG_DIST_50 as SEG_DIST_FREUD,
)
from scripts.psihologia_personalitatii_ii_psihodinamica_freud_explanations import (
    PSIHODINAMICA_FREUD_EXPLANATIONS,
)
from scripts.psihologia_personalitatii_ii_fenomenologica_bank_data import (
    FENOMENOLOGICA_ITEMS,
    SEG_DIST_30 as SEG_DIST_FENOM,
)
from scripts.psihologia_personalitatii_ii_fenomenologica_explanations import (
    FENOMENOLOGICA_EXPLANATIONS,
)
from scripts.psihologia_personalitatii_ii_comportamentala_bank_data import (
    COMPORTAMENTALA_ITEMS,
    SEG_DIST_40,
)
from scripts.psihologia_personalitatii_ii_comportamentala_explanations import (
    COMPORTAMENTALA_EXPLANATIONS,
)
from scripts.psihologia_personalitatii_ii_social_cognitiva_bank_data import (
    SOCIAL_COGNITIVA_ITEMS,
    SEG_DIST_20,
)
from scripts.psihologia_personalitatii_ii_social_cognitiva_explanations import (
    SOCIAL_COGNITIVA_EXPLANATIONS,
)
from scripts.psihologia_personalitatii_ii_comparativ_capcane_bank_data import (
    COMPARATIV_CAPCANE_ITEMS,
    SEG_DIST_40 as SEG_DIST_COMP,
)
from scripts.psihologia_personalitatii_ii_comparativ_capcane_explanations import (
    COMPARATIV_CAPCANE_EXPLANATIONS,
)

OBVIOUS_WRONG = re.compile(
    r"\b(doar de|exclusiv de|absența oricărei|eliminarea oricărei|"
    r"în grilă|pentru grilă|la grilă)\b",
    re.IGNORECASE,
)

TOTAL_ITEMS = 290


def main() -> int:
    built = build_items()
    issues: list[str] = []

    if len(built) != TOTAL_ITEMS:
        issues.append(f"număr itemi: {len(built)}, așteptat {TOTAL_ITEMS}")

    segments = [
        (
            "Ce este personalitatea",
            CE_ESTE_PERSONALITATEA_ITEMS,
            CE_ESTE_PERSONALITATEA_EXPLANATIONS,
            SEG_DIST_30,
        ),
        (
            "Psihodinamică — Freud",
            PSIHODINAMICA_FREUD_ITEMS,
            PSIHODINAMICA_FREUD_EXPLANATIONS,
            SEG_DIST_FREUD,
        ),
        (
            "Neo-psihanalitică",
            NEO_PSIHANALITICA_ITEMS,
            NEO_PSIHANALITICA_EXPLANATIONS,
            SEG_DIST_NEO,
        ),
        (
            "Dispozițională — trăsături",
            DISPOZITIONALA_TRASATURI_ITEMS,
            DISPOZITIONALA_TRASATURI_EXPLANATIONS,
            SEG_DIST_50,
        ),
        (
            "Fenomenologică",
            FENOMENOLOGICA_ITEMS,
            FENOMENOLOGICA_EXPLANATIONS,
            SEG_DIST_FENOM,
        ),
        (
            "Comportamentală",
            COMPORTAMENTALA_ITEMS,
            COMPORTAMENTALA_EXPLANATIONS,
            SEG_DIST_40,
        ),
        (
            "Social-cognitivă",
            SOCIAL_COGNITIVA_ITEMS,
            SOCIAL_COGNITIVA_EXPLANATIONS,
            SEG_DIST_20,
        ),
        (
            "Comparativ + capcane",
            COMPARATIV_CAPCANE_ITEMS,
            COMPARATIV_CAPCANE_EXPLANATIONS,
            SEG_DIST_COMP,
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
                    issues.append(f"{name} #{i + 1}: {len(opts)} opțiuni")
        dist = _count_dist(items)
        if dist != expected_dist:
            issues.append(f"{name} distribuție: {dist}, așteptat {expected_dist}")

    for q in built:
        qid = int(q["id"])
        if not (START_ID <= qid <= START_ID + TOTAL_ITEMS - 1):
            issues.append(f"{qid}: ID în afara intervalului")
        if not str(q.get("explanation") or "").strip():
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
    print(
        f"  Ce este: 30 | Freud: 50 | Neo-psih.: 30 | Dispozițională: 50 | "
        f"Fenomenologică: 30 | Comportamentală: 40 | Social-cognitivă: 20 | "
        f"Comparativ: 40"
    )
    print(f"  ID {START_ID}–{START_ID + TOTAL_ITEMS - 1}, toate cu explicație")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
