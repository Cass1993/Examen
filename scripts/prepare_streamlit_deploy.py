"""Pregătește proiectul pentru deploy pe Streamlit Community Cloud."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

QUESTIONS_JSON = ROOT / "data" / "questions.json"
MIN_SIZE_BYTES = 500_000  # ~0.5 MB — altfel probabil gol / invalid


def _configure_stdio() -> None:
    """Evita UnicodeEncodeError cand stdout e redirectat in .bat (cp1252)."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


def _sync_supplemental_lots() -> int:
    from scripts.supplemental_lots import ensure_all_supplemental_lots

    data = json.loads(QUESTIONS_JSON.read_text(encoding="utf-8"))
    updated = ensure_all_supplemental_lots(data, QUESTIONS_JSON)
    lots = updated.get("lots") or {}
    return sum(len((b.get("questions") or [])) for b in lots.values())


def main() -> int:
    _configure_stdio()
    print("=== Pregatire deploy Streamlit Cloud ===\n")

    if not QUESTIONS_JSON.exists():
        merged = ROOT / "questions_3400_merged.json"
        bank_1400 = ROOT / "1400 x3" / "questions_1400_v6_fara_prescurtari.json"
        if merged.exists():
            print("Generez data/questions.json din questions_3400_merged.json ...")
            from scripts.bank_parser import write_questions_json

            write_questions_json(merged, QUESTIONS_JSON)
        elif bank_1400.exists():
            print("Ruleaza mai intai: python scripts/generate_bank.py")
            return 1
        else:
            print(f"Lipseste {QUESTIONS_JSON}")
            return 1

    try:
        from scripts.sync_psihologia_muncii_ii_lot import main as sync_pm_ii

        print("Actualizez lotul Psihologia muncii II ...")
        sync_pm_ii()
    except Exception as exc:
        print(f"Avertisment sync Psihologia muncii II: {exc}")

    total = _sync_supplemental_lots()
    size_mb = QUESTIONS_JSON.stat().st_size / (1024 * 1024)
    print(f"\nOK: data/questions.json — {total} intrebari, {size_mb:.1f} MB")

    if QUESTIONS_JSON.stat().st_size < MIN_SIZE_BYTES:
        print("EROARE: questions.json pare prea mic.")
        return 1
    if size_mb > 95:
        print(
            "ATENTIE: fisierul e aproape de limita GitHub (100 MB). "
            "Poate fi nevoie de Git LFS."
        )

    print(
        "\nUrmatorii pasi: vezi DEPLOY_STREAMLIT.md "
        "(git add -> commit -> push -> streamlit.io/cloud)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
