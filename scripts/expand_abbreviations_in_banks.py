"""Extinde prescurtările în toate fișierele băncii."""

import json

import sys

from pathlib import Path



APP_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(APP_DIR))



from scripts.polish_text import polish_text  # noqa: E402



BANK_FILES = [

    APP_DIR / "1400 x3" / "questions_1400_v6_fara_prescurtari.json",

    APP_DIR / "2000 itemi raw" / "questions_2000_all.json",

    APP_DIR / "questions_3400_merged.json",

]





def patch_bank(path: Path) -> int:

    if not path.exists():

        print(f"SKIP: {path}")

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

        opts = item.get("variante") or {}

        for k, v in list(opts.items()):

            old = str(v)

            new = polish_text(old)

            if new != old:

                opts[k] = new

                changed += 1

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"{path.name}: {changed} câmpuri actualizate")

    return changed





def patch_questions_json(path: Path) -> int:

    if not path.exists():

        print(f"SKIP: {path}")

        return 0

    data = json.loads(path.read_text(encoding="utf-8"))

    changed = 0

    for lot_data in (data.get("lots") or {}).values():

        for q in lot_data.get("questions", []):

            old_t = str(q.get("text") or "")

            new_t = polish_text(old_t)

            if new_t != old_t:

                q["text"] = new_t

                changed += 1

            old_e = str(q.get("explanation") or "")

            new_e = polish_text(old_e)

            if new_e != old_e:

                q["explanation"] = new_e

                changed += 1

            opts = q.get("options") or {}

            for k, v in list(opts.items()):

                old = str(v)

                new = polish_text(old)

                if new != old:

                    opts[k] = new

                    changed += 1

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"{path.name}: {changed} câmpuri actualizate")

    return changed





def main() -> None:

    total = sum(patch_bank(p) for p in BANK_FILES)

    total += patch_questions_json(APP_DIR / "data" / "questions.json")

    print(f"Total: {total}")





if __name__ == "__main__":

    main()


