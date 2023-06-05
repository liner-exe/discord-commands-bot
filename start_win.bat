@echo off
chcp 65001
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
echo Вы должны установить Python версии 3.8 и выше!
echo Установите Python и попробуйте снова.
echo.
echo Если Python установлен, то переустановите и добавьте его в PATH через "Add Python to PATH" при установке
start https://www.python.org/downloads/
echo.

pause
exit

:run
py setup.py

pause
exit