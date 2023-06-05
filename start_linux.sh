#!/bin/bash

if !command -v python3 &> /dev/null; then
  printf "python3 не найден\n\n"

  echo Установите Python 3.8 или выше
  echo https://www.python.org/downloads/
  echo
  echo Если Python уже установлен проверьте PATH
  echo Переустановите и поставьте галочку \"Add Python to PATH\"
  echo
  read -p "Press Enter to continue . . ."
  exit
fi

python setup.py

exit