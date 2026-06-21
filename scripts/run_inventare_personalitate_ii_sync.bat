@echo off



cd /d "%~dp0.."



echo === Inventare de personalitate II: validare + sync ===



python -u scripts\_validate_inventare_personalitate_ii_items.py



if errorlevel 1 goto err



python -u scripts\sync_inventare_personalitate_ii_lot.py



if errorlevel 1 goto err



echo.



echo Gata. Reporneste aplicatia si alege lotul „Inventare de personalitate II”.



pause



exit /b 0



:err



pause



exit /b 1


