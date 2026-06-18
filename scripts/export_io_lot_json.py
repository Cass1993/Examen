"""Exportă lotul I/O ca JSON pentru merge manual."""
from __future__ import annotations

import json
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.i_o_exam_items import LOT_NAME, build_items

out = APP_DIR / "data" / "_io_lot_export.json"
payload = {"lot_name": LOT_NAME, "questions": build_items()}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(build_items())} items to {out}")
