# Discord Commands Bot - Changelog

## [v0.8.2](https://github.com/r-liner/discord-commands-bot/releases/tag/v0.8.2) (2024-02-18)

[Full Changelog](https://github.com/r-liner/discord-commands-bot/compare/v0.8.1...v0.8.2)

### GitHub
- **bug.yml:** Labels updated
- **feature.yml:** Labels updated
- **README.md:** Adjusted

## [v0.8.1](https://github.com/r-liner/discord-commands-bot/releases/tag/v0.8.1) (2024-02-17)

[Full Changelog](https://github.com/r-liner/discord-commands-bot/compare/v0.8.0...v0.8.1)

### Features
- Added `/cogs list` command

### Documentation
- **cogs/discord.py:** Added docstring to `/avatar` command
- **README.md:** Roadmap updated

### GitHub
- **bug.yml:** Fixed indent, added `Discord Commands Bot` version input
- **feature.yml:** Added feature request template

## [v0.8.0](https://github.com/r-liner/discord-commands-bot/releases/tag/v0.8.0) (2024-02-14)

[Full Changelog](https://github.com/r-liner/discord-commands-bot/compare/v0.7.8...v0.8.0)

### Features
- Slash commands migration!
- **main.py:** added dependency checker, added update notifier
- **cogs/fun.py@Fun:weather:** command is inactive if no openweather token

### New Files
- cogs/utils/
    - __init\__.py
    - decorators.py
    - dependecies.py
    - github.py
    - version.py
- .gitignore

### Documentation
- **cogs/\*.py:** added docstrings to all functions
- **version.txt:** version bumped to 0.8.0
- **README.md:** fixed typo

### Chore
- **main.py:** fixed typo
- **requirements.txt:** updated dependencies

## [v0.7.8](https://github.com/r-liner/discord-commands-bot/releases/tag/v0.7.8) (2024-02-13)

[Full Changelog](https://github.com/r-liner/discord-commands-bot/compare/v0.7.7...v0.7.8)

### Documentation
- **README.md:** fixed typos. Added link to changelog
- **config.yml:** added emoji to `name`
- **version.txt:** version bumber to 0.7.8
- **CHANGELOG.md:** added v0.7.7 release notes, changelog adjusted

### Tweak
- **start_win.bat:** compatibility with new Python version. Minor correction

### Chore
- **config.ini.sample:** removed useless info

### Bugfix
- **main.py:** moved universal exception handling to the end of the try-except block




## [v0.7.7](https://github.com/r-liner/discord-commands-bot/releases/tag/v0.7.7) (2024-02-12)

[Full Changelog](https://github.com/r-liner/discord-commands-bot/compare/v0.7.6...v0.7.7)

### Documentaion
- **pull_request_template.md:** new pr template
- **CHANGELOG.md:** added changelog file
- **LICENSE:** 2022-2023 -> 2022-2024
- **.version:** version bumped to 0.7.7
- **bug.yml:** added bug template
- **config.yml:** added question template
- **README.md:** readme 2.0 (re-built)

### Misc
- **misc(file):** added new screenshots
- **misc(file):** deleted old READMEs

## [v0.7.6](https://github.com/r-liner/discord-commands-bot/releases/tag/v0.7.6) (2024-01-19)

[Full Changelog](https://github.com/r-liner/discord-commands-bot/compare/v0.7.5...v0.7.6)

### Tweaks
- **change:** comments translated in `moderation.py`

## [v0.7.5](https://github.com/r-liner/discord-commands-bot/releases/tag/v0.7.5) (2023-10-01)

[Full Changelog](https://github.com/r-liner/discord-commands-bot/compare/v0.7.4...v0.7.5)

### Features
- **main.py:** Added `if name main` construction

### Chores
**newfile:** `setup.py` for better setup the bot

### Tweaks
- **main.py:** switched to slash commands
- **main.py:** translated one comment
- **tweak:** `start_win.bat` for better setup the bot
- **tweak:** changed `config.ini.sample`