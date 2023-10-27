@echo off
:: Check if we are running with administrative privileges (which we are 99.9% of the time not running with)
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system" && (goto :continue) || (goto :getadmin)

:getadmin
:: Prompt for admin rights
echo Requesting administrative privileges...
if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs"
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
exit /B

:continue
:: The script now has administrator rights but the working directory (cwd) is now C:\Windows\System32
:: So, we need to change that back to the script's directory
cd /d "%~dp0"

:: Now since we got everything rolling, we can start to install the required libraries
echo Installing required libraries...
pip cache remove *
pip install -r requirements.txt
echo Installation complete.
start Management_Panel.pyw


:: NOTES
:: The purpose of this "if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs""
:: is to clean up any previous instances of the getadmin.vbs script
:: that might have been created in the user's temporary directory.
:: This is done to ensure that there are no lingering 
:: or conflicting scripts from previous runs. Not deleting ur system32, alright?
:: and the getadmin.vbs script is a Visual Basic Script (VBS) used in the batch script 
:: to request administrative privileges when running a batch file.
::
:: UAC stands for "User Account Control".
::
:: If you have any more questions, feel free to open a issue on GitHub or a discussion :)