@echo off
echo Running as administrator...

:: Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Already running as administrator
) else (
    echo Restarting as administrator...
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\runas.vbs"
    echo UAC.ShellExecute "cmd.exe", "/c ""%~0""", "", "runas", 1 >> "%temp%\runas.vbs"
    "%temp%\runas.vbs"
    exit /b
)

:: Install customtkinter and pytube using pip
echo Installing required libraries...
pip install customtkinter plyer requests winshell Pillow openai pytube pyttsx3 watchdog

echo Installation complete.
pause
