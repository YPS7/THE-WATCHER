@echo off
echo Installing TheWatcher...

:: Create a directory for TheWatcher in Program Files
set "INSTALL_DIR=%LOCALAPPDATA%\TheWatcher"
mkdir "%INSTALL_DIR%" 2>nul

:: Copy the necessary files
copy "terminal_monitor.py" "%INSTALL_DIR%"
copy "requirements.txt" "%INSTALL_DIR%"

:: Create a system-wide batch file
echo @echo off > "%INSTALL_DIR%\thewatcher.bat"
echo python "%INSTALL_DIR%\terminal_monitor.py" %%* >> "%INSTALL_DIR%\thewatcher.bat"

:: Add to PATH
setx PATH "%PATH%;%INSTALL_DIR%"

echo.
echo TheWatcher has been installed successfully!
echo You can now use the 'thewatcher' command from anywhere.
echo.
echo Example usage:
echo   thewatcher "python your_script.py"
echo   thewatcher "node your_script.js"
echo   thewatcher "javac YourFile.java"
echo.
echo Please restart your terminal for the changes to take effect.
pause 