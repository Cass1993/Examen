"""Rulează upgrade A/F pe fișierele băncii."""

from __future__ import annotations

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.upgrade_tf_items import upgrade_items_batch  # noqa: E402

TARGETS = [
    APP_DIR / "1400 x3" / "questions_1400_v6_fara_prescurtari.json",
    APP_DIR / "2000 itemi raw" / "questions_2000_all.json",
]


def main() -> None:
    total = 0
    for path in TARGETS:
        if not path.exists():
            print(f"SKIP: {path}")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        upgraded, count = upgrade_items_batch(data)
        path.write_text(json.dumps(upgraded, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{path.name}: {count} itemi A/F convertiți")
        total += count
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
