@echo off
title DISCORD BOT

cls

if not exist config.ini (
  goto setup
)

>nul 2>nul assoc .py
if errorlevel 1 (
  goto install_python
) else (
  goto run
)

:install_python
cls
echo You must install Python 3.8 or above!
echo Install Python and try again.
echo.
echo If python already installed, reinstall and add it to PATH via "Add Python to PATH" during installation
start https://www.python.org/downloads/
echo.

pause
exit

:run
py main.py

pause
exit

:setup
cls

echo You must setup the bot firstly
echo.

py setup.py

pause
exit