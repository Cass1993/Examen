"""Curăță extinderi recursive din fișierele băncii."""

from __future__ import annotations

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.abbreviations import expand_abbreviations  # noqa: E402

TARGETS = [
    APP_DIR / "data" / "questions.json",
    APP_DIR / "questions_3400_merged.json",
    APP_DIR / "2000 itemi raw" / "questions_2000_all.json",
    APP_DIR / "1400 x3" / "questions_1400_v6_fara_prescurtari.json",
]

TEXT_KEYS = ("text", "intrebare", "explicatie", "explanation")
OPT_KEYS = ("options", "variante")


def _fix_value(val: str) -> tuple[str, bool]:
    fixed = expand_abbreviations(val)
    return fixed, fixed != val


def patch_list(data: list) -> int:
    count = 0
    for item in data:
        if not isinstance(item, dict):
            continue
        for key in TEXT_KEYS:
            if key in item and isinstance(item[key], str):
                fixed, changed = _fix_value(item[key])
                if changed:
                    item[key] = fixed
                    count += 1
        for key in OPT_KEYS:
            opts = item.get(key)
            if not isinstance(opts, dict):
                continue
            for letter, opt in list(opts.items()):
                if isinstance(opt, str):
                    fixed, changed = _fix_value(opt)
                    if changed:
                        opts[letter] = fixed
                        count += 1
    return count


def patch_lots(data: dict) -> int:
    count = 0
    for lot in (data.get("lots") or {}).values():
        qs = lot.get("questions") if isinstance(lot, dict) else None
        if isinstance(qs, list):
            count += patch_list(qs)
    return count


def main() -> None:
    total = 0
    for path in TARGETS:
        if not path.exists():
            print(f"SKIP: {path}")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            n = patch_list(data)
        elif isinstance(data, dict):
            n = patch_lots(data)
        else:
            n = 0
        if n:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{path.name}: {n} câmpuri reparate")
        total += n
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
