"""Repară itemii de domeniu transformați parțial (enunț tautologic, încă multi-select)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.distractor_fix import build_index  # noqa: E402
from scripts.label_definition_index import build_label_definition_index  # noqa: E402
from scripts.upgrade_tf_items import build_label_definition_map  # noqa: E402
from scripts.domain_item_utils import is_orphan_domain_item  # noqa: E402
from scripts.reformulate_domain import reformulate_domain_batch  # noqa: E402

TARGETS = [
    APP_DIR / "1400 x3" / "questions_1400_v6_fara_prescurtari.json",
    APP_DIR / "2000 itemi raw" / "questions_2000_all.json",
    APP_DIR / "questions_3400_merged.json",
    APP_DIR / "data" / "questions.json",
]


def _flatten_lots(data: dict) -> list[dict]:
    rows: list[dict] = []
    for lot_name, lot_data in (data.get("lots") or {}).items():
        for q in lot_data.get("questions", []):
            rows.append(
                {
                    "id": q.get("id"),
                    "text": q.get("text"),
                    "options": q.get("options"),
                    "correct": q.get("correct"),
                    "explanation": q.get("explanation"),
                    "kind": q.get("kind"),
                    "domeniu": lot_name,
                }
            )
    return rows


def patch_list(items: list[dict]) -> tuple[list[dict], int]:
    index = build_index(items)
    label_map = build_label_definition_map(items)
    label_index = build_label_definition_index(items)

    orphans_before = sum(1 for it in items if is_orphan_domain_item(it))
    fixed, domain_count = reformulate_domain_batch(
        items, index, label_map, label_index
    )
    orphans_after = sum(1 for it in fixed if is_orphan_domain_item(it))
    print(
        f"  reformulate_domain: {domain_count} itemi | "
        f"orfani: {orphans_before} -> {orphans_after}"
    )
    return fixed, domain_count


def patch_bank(path: Path) -> int:
    if not path.exists():
        print(f"SKIP: {path}")
        return 0

    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        fixed, count = patch_list(data)
        path.write_text(
            json.dumps(fixed, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"{path.name}: salvat")
        return count

    if isinstance(data, dict) and "lots" in data:
        rows = _flatten_lots(data)
        fixed_rows, count = patch_list(rows)
        by_id = {r["id"]: r for r in fixed_rows}
        for lot_name, lot_data in data["lots"].items():
            for q in lot_data.get("questions", []):
                row = by_id.get(q.get("id"))
                if not row:
                    continue
                q["text"] = row.get("text", q.get("text"))
                q["options"] = row.get("options", q.get("options"))
                q["correct"] = row.get("correct", q.get("correct"))
                if row.get("explanation"):
                    q["explanation"] = row["explanation"]
                q["kind"] = row.get("kind", q.get("kind"))
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"{path.name}: salvat (lots)")
        return count

    print(f"SKIP (format necunoscut): {path}")
    return 0


def main() -> None:
    total = 0
    for path in TARGETS:
        print(f"\n{path.name}:")
        total += patch_bank(path)
    print(f"\nTotal reformulări: {total}")


if __name__ == "__main__":
    main()
