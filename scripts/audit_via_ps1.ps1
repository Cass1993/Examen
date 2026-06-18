$ErrorActionPreference = 'Stop'
$AppDir = Split-Path (Split-Path $MyInvocation.MyCommand.Path -Parent) -Parent
$py = Join-Path $AppDir '.venv\Scripts\python.exe'
$script = Join-Path $AppDir 'scripts\audit_item_quality.py'
$questions = Join-Path $AppDir 'data\questions.json'
$jsonOut = Join-Path $AppDir 'data\audit_item_quality_report.json'
$txtOut = Join-Path $AppDir 'data\audit_stdout.txt'
& $py $script $questions --json-out $jsonOut 2>&1 | Tee-Object -FilePath $txtOut
exit $LASTEXITCODE
