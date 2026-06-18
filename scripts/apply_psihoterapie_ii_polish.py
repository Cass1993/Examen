"""Aplică polish opțiuni pe psihoterapie_ii_bank_data.py (sursă)."""
from __future__ import annotations

import ast
import json
from pathlib import Path

from scripts.psihoterapie_ii_option_polish import polish_bank_row

BANK_PATH = Path(__file__).resolve().parent / "psihoterapie_ii_bank_data.py"


def _load_items(source: str) -> list:
    module = ast.parse(source)
    for node in module.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "ITEMS":
                    return ast.literal_eval(node.value)
    raise RuntimeError("ITEMS not found")


def main() -> None:
    source = BANK_PATH.read_text(encoding="utf-8")
    items = _load_items(source)
    changed = 0
    polished_items = []
    for row in items:
        new_row = polish_bank_row(row)
        if new_row != row:
            changed += 1
        polished_items.append(new_row)

    start = source.index("ITEMS: List[Item] = [")
    end = source.rindex("]")
    items_block = "ITEMS: List[Item] = " + json.dumps(
        polished_items, ensure_ascii=False, indent=4
    )
    new_source = source[:start] + items_block + source[end + 1 :]
    BANK_PATH.write_text(new_source, encoding="utf-8")
    print(f"polished {changed}/{len(items)} rows")


if __name__ == "__main__":
    main()
