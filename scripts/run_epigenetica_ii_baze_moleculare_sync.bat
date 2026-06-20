@echo off
cd /d "%~dp0.."
python scripts\sync_epigenetica_ii_baze_moleculare_lot.py
python scripts\_validate_epigenetica_ii_baze_moleculare_items.py
pause
