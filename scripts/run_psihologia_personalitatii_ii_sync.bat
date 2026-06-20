@echo off
cd /d "%~dp0.."
python -u scripts\_validate_psihologia_personalitatii_ii_items.py
if errorlevel 1 exit /b 1
python -u scripts\sync_psihologia_personalitatii_ii_lot.py
pause
