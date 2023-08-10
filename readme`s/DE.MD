# <img src="https://flagpedia.net/data/flags/w580/de.webp" width=30> Deutsch
# discord-commands-bot [![CodeFactor](https://www.codefactor.io/repository/github/r-liner/discord-commands-bot/badge)](https://www.codefactor.io/repository/github/r-liner/discord-commands-bot)

## Installation
### Installieren Sie Python 3.8 oder neuer
[Installieren](https://www.python.org/downloads/)
### Installieren Sie das nächste Kabelmodul


```sh
# Linux/macOS
python3 -m pip install -U nextcord

# Windows
py -3 -m pip install -U nextcord
```

### Laden Sie den Bot-Code herunter
Laden Sie das Zip-Archiv der als `neueste` gekennzeichneten Version herunter <br>
und entpacken Sie es an einer beliebigen Stelle Ihres Pcs. <br>
[Neueste Version herunterladen](https://github.com/r-liner/discord-bot-ru/releases)

### Als nächstes muss es für Sie einrichten
Benennen Sie die Datei um `config.ini.sample` zu `config.ini`<br>
Sie können Kommentare davon entfernen.<br><br>
In der Datei `config.ini` sie müssen hinzufügen:
- token in `token`
- id deines Discord Kontos in `owner_id`
- präfix Ihres Bots in `prefix` (. standardmäßig)
- openweather token in `openweather_token`<br>
```diff
@@ Annotation @@
+ Befehl `weather` in cog `cogs/fun.py` funktioniert nicht ohne Token.
+ Der Code funktioniert ohne das Openweather Token.
```

## Start
Sie können den Bot über die ausführen `start_win.bat` für Windows<br>
oder durch die `start_linux.sh` für Linux (don`t works now)<br>
Während des Laufs des Bots müssen Sie sehen:
* Benutzername des Bots (Formatierung: name#discriminator)
* Anzahl Servers des Bot
<br>
<center>
    <a href="https://www.python.org/downloads/">
        <img src="https://img.shields.io/badge/PYTHON-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue?style=for-the-badge&logo=python"  alt="Python Versions" >
    </a>
    <a href="https://github.com/nextcord/nextcord/blob/5ed02d06386ba7b0ac009e9e8833c5f9f2cadb44/docs/index.rst/">
        <img src="https://img.shields.io/badge/NEXTCORD-2.5.0-blue?style=for-the-badge" alt="nextcord">
    </a>
</center>

