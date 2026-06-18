@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
title Pregătire deploy Streamlit Cloud
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Lipseste .venv — ruleaza intai instalarea din README.md
    pause
    exit /b 1
)

".venv\Scripts\python.exe" scripts\prepare_streamlit_deploy.py
echo.
pause
