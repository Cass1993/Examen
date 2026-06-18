"""Audit distractori ușor de eliminat în loturile examen II."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.exam_ii_plausible_distractors import _is_easy_wrong  # noqa: E402
from scripts.exam_item_utils import LETTERS, normalize_correct  # noqa: E402
from scripts.patch_ii_bank_distractors import II_BANK_SOURCES  # noqa: E402

REPORT = ROOT / "data" / "audit_ii_absolutes.txt"


def audit() -> List[str]:
    lines: List[str] = []
    total = 0
    for mod_name, list_name in II_BANK_SOURCES:
        try:
            mod = importlib.import_module(mod_name)
            items: List[Dict[str, Any]] = getattr(mod, list_name, [])
        except Exception as exc:
            lines.append(f"ERR {mod_name}: {exc}")
            continue
        for row in items:
            if row.get("tf") or not row.get("options"):
                continue
            stem = str(row.get("stem", ""))
            correct = set(normalize_correct(str(row.get("correct", ""))))
            for i, opt in enumerate(row["options"]):
                letter = LETTERS[i]
                if letter in correct:
                    continue
                text = str(opt)
                if _is_easy_wrong(text, stem):
                    total += 1
                    lines.append(
                        f"[{mod_name}] {letter}) {text[:90]}"
                        f"{'…' if len(text) > 90 else ''}\n"
                        f"    stem: {stem[:100]}{'…' if len(stem) > 100 else ''}"
                    )
    lines.insert(0, f"Total distractori ușori în sursă: {total}\n{'=' * 60}")
    return lines


def main() -> int:
    report = audit()
    text = "\n".join(report)
    REPORT.write_text(text, encoding="utf-8")
    print(text)
    print(f"\nRaport salvat: {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
