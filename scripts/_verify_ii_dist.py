"""Verify MC answer distribution in Psihologia dezvoltarii II bank files."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FILES = [
    ("main (inline)", ROOT / "scripts/psihologia_dezvoltarii_ii_bank_data.py", "PSIHOLOGIA_DEZVOLTARII_II_ITEMS", 50, (17, 13, 11, 4, 5)),
    ("metode", ROOT / "scripts/psihologia_dezvoltarii_ii_metode_bank_data.py", "METODE_CERCETARE_ITEMS", 50, (17, 13, 11, 4, 5)),
    ("teorii", ROOT / "scripts/psihologia_dezvoltarii_ii_teorii_bank_data.py", "TEORII_INVATARII_ITEMS", 40, (14, 11, 8, 3, 4)),
    ("senzorio_motor", ROOT / "scripts/psihologia_dezvoltarii_ii_senzorio_motor_bank_data.py", "SENZORIO_MOTOR_ITEMS", 40, (14, 11, 8, 3, 4)),
    ("limbaj", ROOT / "scripts/psihologia_dezvoltarii_ii_limbaj_bank_data.py", "LIMBAJ_ITEMS", 30, (10, 8, 6, 3, 3)),
    ("atasament", ROOT / "scripts/psihologia_dezvoltarii_ii_atasament_bank_data.py", "ATASAMENT_ITEMS", 30, (10, 8, 6, 3, 3)),
    ("simbol_joc", ROOT / "scripts/psihologia_dezvoltarii_ii_simbol_joc_bank_data.py", "SIMBOL_JOC_ITEMS", 40, (14, 11, 8, 3, 4)),
    ("scolaritate", ROOT / "scripts/psihologia_dezvoltarii_ii_scolaritate_bank_data.py", "SCOLARITATE_ITEMS", 40, (14, 11, 8, 3, 4)),
    ("adolescenta", ROOT / "scripts/psihologia_dezvoltarii_ii_adolescenta_bank_data.py", "ADOLESCENTA_ITEMS", 40, (14, 11, 8, 3, 4)),
    ("tinereete", ROOT / "scripts/psihologia_dezvoltarii_ii_tinereete_bank_data.py", "TINERETE_ITEMS", 40, (14, 11, 8, 3, 4)),
]


def load_items(path: Path, var: str):
    """Încarcă doar lista de itemi, fără importuri din alte module."""
    from typing import Any, Dict, List

    ns: dict = {
        "List": List,
        "Item": Dict[str, Any],
        "Any": Any,
        "__annotations__": {},
    }
    code = path.read_text(encoding="utf-8")
    marker = f"{var}: List[Item] = ["
    if marker not in code:
        raise ValueError(f"{var} not found in {path}")
    start = code.index(marker)
    end = code.index("\n]", start) + 2
    exec(code[start:end], ns)
    return ns[var]


def classify(item: dict) -> str:
    if item.get("tf"):
        return "TF"
    c = (item.get("correct") or "").strip().lower()
    letters = "".join(sorted(set(ch for ch in c if ch in "abcd")))
    n = len(letters)
    if n == 1:
        return "1"
    if n == 2:
        return "2"
    if n == 3:
        return "3"
    if n == 4:
        return "4"
    return f"?({c})"


def main() -> None:
    print(f"{'file':<16} {'tot':>4} {'1':>4} {'2':>4} {'3':>4} {'4':>4} {'TF':>4}  ok?")
    print("-" * 60)
    all_ok = True
    for label, path, var, total, target in FILES:
        items = load_items(path, var)
        counts = {"1": 0, "2": 0, "3": 0, "4": 0, "TF": 0}
        other = {}
        for it in items:
            k = classify(it)
            if k in counts:
                counts[k] += 1
            else:
                other[k] = other.get(k, 0) + 1
        t1, t2, t3, t4, ttf = target
        ok = (
            len(items) == total
            and counts["1"] == t1
            and counts["2"] == t2
            and counts["3"] == t3
            and counts["4"] == t4
            and counts["TF"] == ttf
            and counts["1"] > counts["2"] > counts["3"] > counts["4"]
        )
        if not ok:
            all_ok = False
        extra = f"  other={other}" if other else ""
        print(
            f"{label:<16} {len(items):>4} {counts['1']:>4} {counts['2']:>4} "
            f"{counts['3']:>4} {counts['4']:>4} {counts['TF']:>4}  "
            f"{'OK' if ok else 'NO'} (tgt {t1}/{t2}/{t3}/{t4}/{ttf}){extra}"
        )
    print("-" * 60)
    print("ALL OK" if all_ok else "NEEDS REBALANCE")


if __name__ == "__main__":
    main()
