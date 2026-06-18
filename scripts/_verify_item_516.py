"""Verify item 516: polish simulation + genetics checks."""
from __future__ import annotations

import json
import sys
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.label_definition_index import build_label_definition_index
from scripts.polish_text import polish_question_item
from scripts.upgrade_tf_items import build_label_definition_map

QUESTIONS = ROOT / "data" / "questions.json"
ITEM_ID = 516
REPEAT_PHRASE = "Modelul personalității"
FORBIDDEN = "validitate de criteriu"
POLISH_PASSES = 2


def load_bank() -> dict:
    return json.loads(QUESTIONS.read_text(encoding="utf-8"))


def find_item(data: dict, item_id: int) -> tuple[str, dict] | None:
    for lot, block in (data.get("lots") or {}).items():
        for item in block.get("questions") or block.get("items") or []:
            if item.get("id") == item_id:
                return lot, item
    return None


def format_item(item: dict) -> str:
    lines = [f"Question: {item.get('text') or item.get('intrebare') or ''}"]
    opts = item.get("options") or {}
    for k in sorted(opts.keys()):
        mark = "*" if k in (item.get("correct") or []) else " "
        lines.append(f"  ({k}){mark} {opts[k]}")
    return "\n".join(lines)


def main() -> int:
    data = load_bank()
    found = find_item(data, ITEM_ID)
    if not found:
        print(f"FAIL: item id {ITEM_ID} not found in {QUESTIONS}")
        return 1

    lot, raw = found
    label_map = build_label_definition_map(data)
    label_index = build_label_definition_index(data)

    row = deepcopy(raw)
    row["domeniu"] = lot
    row["lot"] = lot
    for _ in range(POLISH_PASSES):
        row = polish_question_item(
            row,
            index=ITEM_ID,
            label_map=label_map,
            label_index=label_index,
        )

    print(f"Lot: {lot}")
    print()
    print("=== BEFORE polish ===")
    print(format_item(raw))
    print()
    print("=== AFTER polish ===")
    print(format_item(row))
    print()

    opt_a = (row.get("options") or {}).get("a", "")
    repeat_count = opt_a.count(REPEAT_PHRASE)
    all_text = " ".join(
        [str(row.get("text") or "")]
        + [str(v) for v in (row.get("options") or {}).values()]
    ).lower()

    checks = [
        (
            f'Option (a) does NOT repeat "{REPEAT_PHRASE}"',
            repeat_count <= 1,
            f"appears {repeat_count} time(s): {opt_a!r}",
        ),
        (
            f'No "{FORBIDDEN}" in question/options',
            FORBIDDEN not in all_text,
            "forbidden phrase present",
        ),
    ]

    print("=== CHECKS ===")
    ok = True
    for name, passed, detail in checks:
        status = "PASS" if passed else "FAIL"
        print(f"{status}: {name}" + (f" — {detail}" if not passed else ""))
        ok = ok and passed

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
