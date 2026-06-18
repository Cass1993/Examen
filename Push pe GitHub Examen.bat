@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
title Push GitHub Cass1993/Examen — log
cd /d "%~dp0"
set LOG=%~dp0_push_log.txt
set REPO=https://github.com/Cass1993/Examen.git

echo === Push GitHub %DATE% %TIME% === > "%LOG%"

if not exist ".venv\Scripts\python.exe" (
    echo EROARE: lipseste .venv >> "%LOG%"
    echo Lipseste .venv. Ruleaza instalarea din README.md
    notepad "%LOG%"
    pause
    exit /b 1
)

echo [1] prepare_streamlit_deploy.py >> "%LOG%"
".venv\Scripts\python.exe" scripts\prepare_streamlit_deploy.py >> "%LOG%" 2>&1
if errorlevel 1 (
    echo EROARE la prepare >> "%LOG%"
    notepad "%LOG%"
    pause
    exit /b 1
)

if not exist "data\questions.json" (
    echo EROARE: lipseste data\questions.json >> "%LOG%"
    notepad "%LOG%"
    pause
    exit /b 1
)
if not exist "scripts\bank_parser.py" (
    echo EROARE: lipseste scripts\ >> "%LOG%"
    notepad "%LOG%"
    pause
    exit /b 1
)

where git >nul 2>&1
if errorlevel 1 (
    echo EROARE: git nu e instalat. Instaleaza Git for Windows. >> "%LOG%"
    echo Git nu e instalat: https://git-scm.com/download/win
    notepad "%LOG%"
    pause
    exit /b 1
)

if not exist ".git" git init >> "%LOG%" 2>&1
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    git remote add origin %REPO% >> "%LOG%" 2>&1
) else (
    git remote set-url origin %REPO% >> "%LOG%" 2>&1
)

echo [2] git add >> "%LOG%"
git add app.py requirements.txt .gitignore .streamlit DEPLOY_STREAMLIT.md README.md >> "%LOG%" 2>&1
git add scripts >> "%LOG%" 2>&1
git add data/questions.json >> "%LOG%" 2>&1
git add "Push pe GitHub Examen.bat" "Pregateste Deploy Streamlit.bat" >> "%LOG%" 2>&1

echo [3] git status >> "%LOG%"
git status -sb >> "%LOG%" 2>&1

echo [4] git commit >> "%LOG%"
git commit -m "Streamlit Cloud: app + scripts + data/questions.json" >> "%LOG%" 2>&1

git branch -M main >> "%LOG%" 2>&1

echo [5] git pull --allow-unrelated-histories >> "%LOG%"
git pull origin main --allow-unrelated-histories --no-edit >> "%LOG%" 2>&1

echo [6] git push >> "%LOG%"
git push -u origin main >> "%LOG%" 2>&1
set PUSHERR=%ERRORLEVEL%

echo Push exit code: %PUSHERR% >> "%LOG%"
echo. >> "%LOG%"
echo === Dupa push, pe GitHub trebuie sa vezi folderele data/ si scripts/ === >> "%LOG%"

if %PUSHERR% NEQ 0 (
    echo.
    echo PUSH ESUAT — vezi log: %LOG%
    echo Posibil: login GitHub lipsa sau conflict. Deschide log-ul.
    notepad "%LOG%"
    pause
    exit /b 1
)

echo.
echo OK! Verifica https://github.com/Cass1993/Examen — trebuie data/ si scripts/
echo Apoi Streamlit Cloud: Reboot app sau asteapta redeploy.
notepad "%LOG%"
pause
exit /b 0
