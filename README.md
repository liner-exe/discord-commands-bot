# Discord Commands Bot [![Code Factor](https://www.codefactor.io/repository/github/r-liner/discord-commands-bot/badge)](https://www.codefactor.io/repository/github/r-liner/discord-commands-bot)
![GitHub Release](https://img.shields.io/badge/release-v0.8.3-blue.svg?logo=github&logoColor=ffffff&style=for-the-badge&color=efa94a)
![GitHub issues](https://img.shields.io/github/issues-raw/r-liner/discord-commands-bot?style=for-the-badge)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg?logo=python&logoColor=ffffff&style=for-the-badge)](https://www.python.org/downloads/)
[![Nextcord Version](https://img.shields.io/badge/nextcord-2.4.2+-blue.svg?logo=pypi&logoColor=ffffff&style=for-the-badge)](https://pypi.org/project/nextcord/)
![GitHub License](https://img.shields.io/github/license/r-liner/discord-commands-bot?style=for-the-badge&color=blue)

# Description
An another yet Discord multipurposal bot written in Python.

## Table of Contents
- [Discord Commands Bot](#discord-commands-bot-code-factor)
- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Key Features](#key-features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
    - [API Keys](#api-keys)
    - [Requirements](#requirements)
  - [Installing - Self Hosting](#installing---self-hosting)
- [Launch](#launch)
- [Roadmap](#roadmap)
- [Changelog](#changelog)
- [Support](#support)
- [Contribution](#contribution)
- [Contact](#contact)
- [License](#license)

## Key Features
- Async-await syntax
- Slash commands partial-ready
- Easy installation, setup
- Use the same bot instance on multiple guilds
- Regurarly updates

## Installation
### Prerequisites
#### API Keys
- Discord - https://discord.com/developers
- Openweather (Optional) - https://openweathermap.org/api

##### How to get discord token?
1. Go to [Discord Developer Portal](https://discord.com/developers).
2. Press **New Application**.

    <details>
        <summary>Hint</summary>
        <img src='./assets/discord developer portal/setup_01.png' alt='setup_01.png'>
    </details>
3. Enter application name and press **Create**.
    <details>
        <summary>Hint</summary>
        <img src='./assets/discord developer portal/setup_02.png' alt='setup_02.png'>
    </details>
4. Go to tab **Bot**.
5. Reset and **Copy** bot token.
    <details>
        <summary>Hint</summary>
        <img src='./assets/discord developer portal/setup_03.png' alt='setup_03.png'>
    </details>

Obtained keys must be entered while setup the bot through `setup.py`.

#### Requirements
- Installation of Python 3.8+ - https://www.python.org/downloads/

##### Install nextcord:
```sh
# Linux/macOS
python3 -m pip install -U nextcord

# Windows
pip install -U nextcord
```
##### Install dependencies:
```
pip install -r requirements.txt
```

### Installing - Self Hosting

**Manual Installation**
1. Complete [prerequisites](#prerequisites).
2. [Download latest release](https://github.com/r-liner/discord-bot-ru/releases).
3. Launch `setup.py` and complete setup process.
4. Done. Now you can launch the bot.

**Installation via Git**
1. Complete [prerequisites](#prerequisites).
2. Clone repository using:
```sh
git clone https://github.com/r-liner/discord-commands-bot
```
3. Launch `setup.py` and complete setup process.
4. Done. Now you can launch the bot.

## Launch
You can run the bot through the `start_win.bat` for Windows
or directly through the `main.py`. <br>
During run the bot you must see:
* Bot username (format: name#discrim).
* Count of bot servers.

## Roadmap
**Q2:**
- Code simplify.
- Add i18n

## Changelog
You can find it [here](https://github.com/r-liner/discord-commands-bot/blob/master/CHANGELOG.md).

## Support
❓ If you have a **question** ask it [here](https://github.com/r-liner/discord-commands-bot/issues).

🐛 If you found a **bug** have a look at the [issue list](https://github.com/r-liner/discord-commands-bot/issues/) before you [create a new issue](https://github.com/r-liner/discord-commands-bot/issues/new/choose). Please provide as much information as possible to help us understand and reproduce your issue.

✨ If you want to request new **feature** have a look at the [issue list](https://github.com/r-liner/discord-commands-bot/issues/) before you [create it](https://github.com/r-liner/discord-commands-bot/issues/new/choose).

## Contribution
If you would like to contribute to this project, fork repository, add your changes and then create pull request.
Please ensure that you have thoroughly tested all your changes.

Even if you`re not the programmer, you can contribute to this project by reporting bugs, requesting new features, fixing typos, etc.

## Contact
If you have a question regarding the project, [open new issue](https://github.com/r-liner/discord-commands-bot/issues/new/choose).

If your request would contain confidentional information, [please send me an email](mailto:contact.liner999@gmail.com).

## License
[MIT](https://opensource.org/license/mit/)

<br>

Copyright &copy; 2022-2024 [liner](https://github.com/r-liner)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[(Back to top)](#table-of-contents)