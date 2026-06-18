"""Run audit silently and write JSON + stdout to data/."""
from __future__ import annotations

import io
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.audit_item_quality import audit_bank, print_pipeline_summary, print_report  # noqa: E402

OUT_JSON = APP_DIR / "data" / "audit_item_quality_report.json"
OUT_TXT = APP_DIR / "data" / "audit_stdout.txt"


def main() -> None:
    buf = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buf
    try:
        result = audit_bank(APP_DIR / "data" / "questions.json")
        print_report(result)
        print_pipeline_summary()
        OUT_JSON.write_text(
            __import__("json").dumps(result, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"JSON report: {OUT_JSON}")
    finally:
        sys.stdout = old_stdout
    OUT_TXT.write_text(buf.getvalue(), encoding="utf-8")
    print(f"Wrote {OUT_JSON} and {OUT_TXT}")


if __name__ == "__main__":
    main()
