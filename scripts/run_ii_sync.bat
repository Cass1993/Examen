@echo off
cd /d "%~dp0.."
echo === Patch distractori sursa + resync loturi II ===
python -u scripts\patch_ii_bank_distractors.py
if errorlevel 1 (
  echo Eroare la patch. Incerc doar resync prin supplemental...
  python -c "import json; from pathlib import Path; from scripts.supplemental_lots import ensure_all_supplemental_lots; p=Path('data/questions.json'); d=json.loads(p.read_text(encoding='utf-8')); ensure_all_supplemental_lots(d,p); print('OK')"
)
echo.
echo Reporneste aplicatia Streamlit pentru a vedea modificarile.
pause
