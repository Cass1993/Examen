import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.psihologia_dezvoltarii_ii_exam_items import LOT_NAME, build_items

out = ROOT / "_sync_batranete_log.txt"
try:
    built = build_items()
    qpath = ROOT / "data" / "questions.json"
    data = json.loads(qpath.read_text(encoding="utf-8"))
    old = len(data.get("lots", {}).get(LOT_NAME, {}).get("questions") or [])
    data.setdefault("lots", {})[LOT_NAME] = {"questions": built}
    data["total_questions"] = sum(
        len(b.get("questions") or []) for b in data.get("lots", {}).values()
    )
    qpath.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    out.write_text(
        f"ok items={len(built)} old={old} last_id={built[-1]['id']}\n",
        encoding="utf-8",
    )
except Exception as e:
    out.write_text(f"error: {e}\n", encoding="utf-8")
    raise
