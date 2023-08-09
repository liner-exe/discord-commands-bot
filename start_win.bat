@echo off
title discord-bot-ru

cls

>nul 2>nul assoc .py
if errorlevel 1 (
  goto install_python
) else (
  goto run
)

:install_python
cls
echo You must download Python ver 3.8 or newer!
echo Install Python and try again.
echo.
echo If Python has installed, reinstall and add it to PATH via "Add Python to PATH" during installation
start https://www.python.org/downloads/
echo.

pause
exit

:run
py main.py

pause
exit
