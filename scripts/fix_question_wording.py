"""Aplică reformulări gramaticale pe fișierele JSON ale băncii."""

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.polish_text import polish_text  # noqa: E402

TARGETS = [
    {
        "path": APP_DIR / "1400 x3" / "questions_1400_v6_fara_prescurtari.json",
        "kind": "bank",
    },
    {
        "path": APP_DIR / "2000 itemi raw" / "questions_2000_all.json",
        "kind": "bank",
    },
    {
        "path": APP_DIR / "2000 itemi raw" / "questions_part_1_500.json",
        "kind": "bank",
    },
    {
        "path": APP_DIR / "2000 itemi raw" / "questions_part_501_1000.json",
        "kind": "bank",
    },
    {
        "path": APP_DIR / "questions_3400_merged.json",
        "kind": "bank",
    },
    {
        "path": APP_DIR / "data" / "questions.json",
        "kind": "lots",
    },
]


def patch_bank(path: Path) -> int:
    if not path.exists():
        print(f"SKIP (lipsă): {path}")
        return 0

    data = json.loads(path.read_text(encoding="utf-8"))
    changed = 0

    for item in data:
        for field in ("intrebare", "explicatie"):
            old = str(item.get(field) or "")
            new = polish_text(old)
            if new != old:
                item[field] = new
                changed += 1
        for k, v in list((item.get("variante") or {}).items()):
            old = str(v)
            new = polish_text(old)
            if new != old:
                item["variante"][k] = new
                changed += 1

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{path.name}: {changed} enunțuri reformulate")
    return changed


def patch_lots_questions(path: Path) -> int:
    if not path.exists():
        print(f"SKIP (lipsă): {path}")
        return 0

    data = json.loads(path.read_text(encoding="utf-8"))
    changed = 0

    for lot_data in (data.get("lots") or {}).values():
        for question in lot_data.get("questions", []):
            old = str(question.get("text") or "")
            new = polish_text(old)
            if new != old:
                question["text"] = new
                changed += 1
            old_e = str(question.get("explanation") or "")
            new_e = polish_text(old_e)
            if new_e != old_e:
                question["explanation"] = new_e
                changed += 1
            for k, v in list((question.get("options") or {}).items()):
                old_o = str(v)
                new_o = polish_text(old_o)
                if new_o != old_o:
                    question["options"][k] = new_o
                    changed += 1

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{path.name}: {changed} enunțuri reformulate")
    return changed


def main() -> None:
    total = 0
    for target in TARGETS:
        path = target["path"]
        kind = target["kind"]
        if kind == "bank":
            total += patch_bank(path)
        elif kind == "lots":
            total += patch_lots_questions(path)
        else:
            print(f"SKIP (tip necunoscut): {path}")

    print(f"Total: {total}")


if __name__ == "__main__":
    main()
