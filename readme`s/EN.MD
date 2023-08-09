# discord-bot-ru [![CodeFactor](https://www.codefactor.io/repository/github/r-liner/discord-bot-ru/badge)](https://www.codefactor.io/repository/github/r-liner/discord-bot-ru)

## Installation
### Install Python 3.8 or newer
[Install](https://www.python.org/downloads/)
### Install module nextcord


```sh
# Linux/macOS
python3 -m pip install -U nextcord

# Windows
py -3 -m pip install -U nextcord
```

### Download the code of bot
Download the zip archive of version marked as `latest` <br>
and unpack it on any place of your PC. <br>
[Download latest release](https://github.com/r-liner/discord-bot-ru/releases)

### Next must setup it for you
Rename the file `config.ini.sample` to `config.ini`<br>
You can remove comments of it.<br><br>
In the file `config.ini` you must add:
- token to `token`
- id of your discord account to `owner_id`
- prefix of your bot to `prefix` (. by default)
- openweather token to `openweather_token`<br>
```diff
@@ Annotation @@
+ The command `weather` in cog `cogs/fun.py` will not work without token.
+ The code will work without the openweather token.
```

## Launch
You can run the bot through the `start_win.bat` for Windows<br>
or through the `start_linux.sh` for Linux (don`t works now)<br>
During run the bot you must see:
* Bot`s username (format: name#discrim)
* Count of bot`s servers
<br>
<center>
    <a href="https://www.python.org/downloads/">
        <img src="https://img.shields.io/badge/PYTHON-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue?style=for-the-badge&logo=python"  alt="Python Versions" >
    </a>
    <a href="https://github.com/nextcord/nextcord/blob/5ed02d06386ba7b0ac009e9e8833c5f9f2cadb44/docs/index.rst/">
        <img src="https://img.shields.io/badge/NEXTCORD-2.4.2-blue?style=for-the-badge" alt="nextcord">
    </a>
</center>

