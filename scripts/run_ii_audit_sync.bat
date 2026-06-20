@echo off
cd /d "%~dp0.."
echo === Audit meta-limbaj grila (toate loturile II) ===
python -u scripts\_audit_all_ii_grila_meta.py
if errorlevel 1 goto err

echo.
echo === Validare Psihologia invatarii II ===
python -u scripts\_validate_invatarii_ii_items.py
if errorlevel 1 goto err

echo.
echo === Sync loturi II ===
python -u scripts\sync_psihologia_invatarii_ii_lot.py
if errorlevel 1 goto err
python -u scripts\sync_psihologia_muncii_ii_lot.py
if errorlevel 1 goto err
python -u scripts\sync_psihologia_dezvoltarii_ii_lot.py
if errorlevel 1 goto err
python -u scripts\sync_statistica_ii_lot.py
if errorlevel 1 goto err

echo.
echo Gata. Reporneste aplicatia pentru a vedea modificarile.
pause
exit /b 0

:err
echo.
echo Eroare la rulare. Verifica mesajele de mai sus.
pause
exit /b 1
