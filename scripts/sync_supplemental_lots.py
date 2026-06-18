"""Sincronizează loturile examen în data/questions.json (fără Streamlit)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.supplemental_lots import ensure_all_supplemental_lots  # noqa: E402

QUESTIONS_JSON = ROOT / "data" / "questions.json"


def main() -> int:
    data: dict = {"lots": {}}
    if QUESTIONS_JSON.exists():
        data = json.loads(QUESTIONS_JSON.read_text(encoding="utf-8"))

    before = json.dumps(data.get("lots", {}), ensure_ascii=False, sort_keys=True)
    ensure_all_supplemental_lots(data, QUESTIONS_JSON)
    after_data = json.loads(QUESTIONS_JSON.read_text(encoding="utf-8"))
    after = json.dumps(after_data.get("lots", {}), ensure_ascii=False, sort_keys=True)

    lot_name = "Psihoterapie II: Orientări și metode în psihoterapie"
    sample = ""
    for q in after_data.get("lots", {}).get(lot_name, {}).get("questions", []):
        if q.get("id") == 7046:
            sample = q.get("text", "")
            break

    print("questions.json actualizat." if before != after else "questions.json era deja la zi.")
    print(f"Total loturi: {len(after_data.get('lots', {}))}")
    for name in ("Psihopatologie II", "Psihoterapie II: Orientări și metode în psihoterapie"):
        n = len(after_data.get("lots", {}).get(name, {}).get("questions", []))
        if n:
            print(f"  {name}: {n} întrebări")
    if sample:
        print(f"Exemplu id 7046: {sample[:120]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
