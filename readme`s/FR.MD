# <img src="https://flagpedia.net/data/flags/w580/fr.webp" width=30> Français
# discord-commands-bot [![CodeFactor](https://www.codefactor.io/repository/github/r-liner/discord-commands-bot/badge)](https://www.codefactor.io/repository/github/r-liner/discord-commands-bot)
## Installation
### Installez Python 3.8 ou plus récent
[Installer](https://www.python.org/downloads/)
### Installez le module nextcord


```sh
# Linux/macOS
python3 -m pip install -U nextcord

# Windows
py -3 -m pip install -U nextcord
```

### Téléchargez le code du bot
Téléchargez l'archive zip de la version marquée comme `la plus récente` <br>
et décompressez-le sur n'importe quel endroit de votre PC. <br>
[Téléchargez la dernière version](https://github.com/r-liner/discord-bot-ru/releases)

### Vous devez le configurer pour vous ensuite
Renommez le fichier `config.ini.sample` au `config.ini`<br>
Vous pouvez en supprimer les commentaires.<br><br>
Dans le fichier `config.ini` vous devez ajouter:
- jeton au `token`
- identifiant de votre compte discord au `owner_id`
- préfixe de votre bot au `prefix` (. par défaut)
- openweather jeton au `openweather_token`<br>
```diff
@@ Annotation @@
+ La commande `weather` dans cog `cogs/fun.py` ne fonctionnera pas sans jeton.
+ Le code fonctionnera sans le jeton openweather.
```

## Débuter
Vous pouvez exécuter le bot via le `start_win.bat` pour Windows<br>
ou à travers le `start_linux.sh` pour Linux (don`t works now)<br>
Pendant l'exécution du bot, vous devez voir:
* Nom d'utilisateur du bot (format: nom#discriminateur)
* Nombre de serveurs du bot
<br>
<center>
    <a href="https://www.python.org/downloads/">
        <img src="https://img.shields.io/badge/PYTHON-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue?style=for-the-badge&logo=python"  alt="Python Versions" >
    </a>
    <a href="https://github.com/nextcord/nextcord/blob/5ed02d06386ba7b0ac009e9e8833c5f9f2cadb44/docs/index.rst/">
        <img src="https://img.shields.io/badge/NEXTCORD-2.5.0-blue?style=for-the-badge" alt="nextcord">
    </a>
</center>

