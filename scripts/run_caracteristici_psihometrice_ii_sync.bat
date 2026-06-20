@echo off
cd /d "%~dp0.."
echo === Caracteristici psihometrice II: validare + sync ===
python -u scripts\_validate_caracteristici_psihometrice_ii_items.py
if errorlevel 1 goto err
python -u scripts\sync_caracteristici_psihometrice_ii_lot.py
if errorlevel 1 goto err
echo.
echo Gata. Reporneste aplicatia si alege lotul „Caracteristici psihometrice II”.
pause
exit /b 0
:err
pause
exit /b 1
