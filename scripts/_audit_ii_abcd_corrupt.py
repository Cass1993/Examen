"""Repară itemi Psihologia dezvoltării II cu correct='abcd' corupt de rebalansare."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.psihologia_dezvoltarii_ii_bank_data import PSIHOLOGIA_DEZOLTARII_II_ITEMS  # noqa: E402
from scripts.psihologia_dezvoltarii_ii_exam_items import build_items  # noqa: E402

# Enunțuri care cer UN singur răspuns — abcd e aproape sigur corupt
_SINGLE_STEM = re.compile(
    r"(se numește\s*:|"
    r"cel mai potrivit|"
    r"cel mai clar|"
    r"Răspunsul pedagogic corect|"
    r"Care metodă este cea mai potrivită|"
    r"rezumă cel mai bine|"
    r"indică cel mai clar)",
    re.IGNORECASE,
)

# Enunțuri „Care patru …” — abcd poate fi legitim
_FOUR_STEM = re.compile(
    r"care (patru|4|toate patru)",
    re.IGNORECASE,
)


def main() -> int:
    built = {int(q["id"]): q for q in build_items()}
    suspicious: list[str] = []

    for i, row in enumerate(PSIHOLOGIA_DEZOLTARII_II_ITEMS):
        qid = 10001 + i
        correct = str(row.get("correct") or "").lower()
        if correct != "abcd":
            continue
        stem = str(row.get("stem") or "")
        if _FOUR_STEM.search(stem):
            continue
        if _SINGLE_STEM.search(stem):
            suspicious.append(f"{qid}: SINGLE? stem={stem[:70]}...")
            continue
        # Alte abcd fără „patru” în enunț — de verificat manual
        if not _FOUR_STEM.search(stem):
            suspicious.append(f"{qid}: REVIEW stem={stem[:70]}...")

    print(f"Itemi cu correct=abcd suspect (fără «care patru»): {len(suspicious)}")
    for line in suspicious:
        print(f"  {line}")

    # Verifică itemi construiți cu 4 răspunsuri corecte dar explicație contrazice
    for qid, q in sorted(built.items()):
        correct = q.get("correct") or []
        if len(correct) != 4:
            continue
        expl = str(q.get("explanation") or "").lower()
        opts = q.get("options") or {}
        if "nu descriu" in expl or "nu explică" in expl or "e fals" in expl or "e greșit" in expl:
            suspicious.append(f"{qid}: 4 corecte dar explicația exclude variante")
            print(f"  CONFLICT {qid}: {q.get('text','')[:60]}...")

    return 1 if suspicious else 0


if __name__ == "__main__":
    raise SystemExit(main())
