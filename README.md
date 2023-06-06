# discord-bot-ru

## Установка
### Установите Python 3.8 или новее
[Установить](https://www.python.org/downloads/)
### Установить модуль nextcord


```sh
# Linux/macOS
python3 -m pip install -U nextcord

# Windows
py -3 -m pip install -U nextcord
```

### Установите код бота
Скачайте zip архив версии с пометкой `latest` <br>
и распакуйте в любое место на своём ПК. <br>
[Установить последний релиз](https://github.com/r-liner/discord-bot-ru/releases)

### Далее необходимо настроить под себя
Переименуйте файл `config.ini.sample` в `config.ini`<br>
Также можно удалить комментарии из того же файла<br><br>
В файле `config.ini` необходимо добавить:
- токен в `token`
- id учётной записи Discord в `owner_id`
- префикс бота в `prefix`
- токен openweather в `openweather_token`<br>
```diff
@@ Примечание @@
+ Команда `weather` в коге `cogs/fun.py` работать без него не будет.
+ Код в целом без него будет работать как обычно.
```

## Запуск
Бота можно запустить через файл `start_win.bat` для Windows<br>
Или через `start_linux.sh` для Linux<br>
При запуске вы должны увидеть:
* Имя бота
* На скольки серверах он работает
<br>
<center>
    <a href="https://www.python.org/downloads/">
        <img src="https://img.shields.io/badge/PYTHON-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue?style=for-the-badge&logo=python"  alt="Python Versions" >
    </a>
    <a href="https://github.com/nextcord/nextcord/blob/5ed02d06386ba7b0ac009e9e8833c5f9f2cadb44/docs/index.rst/">
        <img src="https://img.shields.io/badge/NEXTCORD-2.4.2-blue?style=for-the-badge" alt="nextcord">
    </a>
</center>
