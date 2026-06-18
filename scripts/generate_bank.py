"""Generează banca combinată 3400 + data/questions.json pentru aplicație."""
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))

from scripts.bank_merge import merge_banks  # noqa: E402
from scripts.bank_parser import write_questions_json  # noqa: E402

BANK_1400 = APP_DIR / "1400 x3" / "questions_1400_v6_fara_prescurtari.json"
BANK_2000 = APP_DIR / "2000 itemi raw" / "questions_2000_all.json"
MERGED = APP_DIR / "questions_3400_merged.json"
REPORT = APP_DIR / "2000 itemi raw" / "raport_validare_merge_3400.txt"
RESEARCH = APP_DIR / "2000 itemi raw" / "raport_cercetare_metodologica_2000.txt"
OUT = APP_DIR / "data" / "questions.json"


def main() -> None:
    if not BANK_1400.exists():
        raise FileNotFoundError(BANK_1400)
    if not BANK_2000.exists():
        raise FileNotFoundError(BANK_2000)

    stats = merge_banks(BANK_1400, BANK_2000, MERGED, REPORT, RESEARCH)
    data = write_questions_json(MERGED, OUT)
    print(f"Merged: {stats['merged']} items -> {MERGED}")
    print(f"Report: {REPORT}")
    print(f"Research: {RESEARCH}")
    print(f"App data: {OUT} ({data['total_questions']} questions, {len(data['lots'])} domains)")
    print(
        f"Duplicates skipped: {stats['duplicates_skipped']}, "
        f"Overlap 1400: {stats.get('overlap_1400_skipped', 0)}, "
        f"Errors excluded: {stats['errors_excluded']}"
    )


if __name__ == "__main__":
    main()
