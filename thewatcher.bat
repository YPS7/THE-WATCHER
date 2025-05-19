@echo off
setlocal enabledelayedexpansion

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not installed or not in PATH
    exit /b 1
)

REM Check if requirements are installed
python -c "import openai, google.generativeai, groq" >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Installing required packages...
    pip install -r requirements.txt
)

REM Build the command string
set "cmd="
for %%a in (%*) do (
    set "cmd=!cmd! %%a"
)

REM Run TheWatcher
python terminal_monitor.py %cmd%

endlocal
