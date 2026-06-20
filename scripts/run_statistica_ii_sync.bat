@echo off
cd /d "%~dp0.."
echo === Statistica II: validare + sync ===
python -u scripts\_validate_statistica_ii_items.py
if errorlevel 1 goto err
python -u scripts\sync_statistica_ii_lot.py
if errorlevel 1 goto err
echo.
echo Gata. Reporneste aplicatia si alege lotul „Statistica II”.
pause
exit /b 0
:err
pause
exit /b 1
