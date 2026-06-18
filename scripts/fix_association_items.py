"""Aplică fix asocieri concept–descriere pe banca de itemi."""

from __future__ import annotations

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.association_pair_fix import fix_association_pairs, needs_association_fix  # noqa: E402
from scripts.audit_item_quality import walk_items  # noqa: E402

TARGETS = [
    APP_DIR / "data" / "questions.json",
    APP_DIR / "questions_clean.json",
]


def main() -> None:
    total_changed = 0
    for path in TARGETS:
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        before = sum(1 for _, q in walk_items(data) if needs_association_fix(q))
        changed = 0
        if "lots" in data:
            for lot_data in data["lots"].values():
                qs = lot_data.get("questions", [])
                for i, q in enumerate(qs):
                    fixed, ch = fix_association_pairs(q)
                    if ch:
                        qs[i] = fixed
                        changed += 1
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        after = sum(1 for _, q in walk_items(data) if needs_association_fix(q))
        print(f"{path.name}: {changed} rescrise, probleme {before} → {after}")
        total_changed += changed
    print(f"Total: {total_changed}")


if __name__ == "__main__":
    main()
