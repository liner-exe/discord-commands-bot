from logging import Logger

import disnake
from disnake.ext import commands

import os, platform, sys, logging
import json

from cogs.utils import dependecies, github, version

PATH = os.path.dirname(os.path.realpath(__file__))

extensions = [
    "cogs.useful",
    "cogs.fun"
]

with open(f"{PATH}/config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

OWNER_IDS = config["bot"]["owners"]
ADMIN_GUILDS = config["bot"]["admin_guilds"]


class LoggingFormatter(logging.Formatter):
    black = "\x1b[30b"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    gray = "\x1b[38m"
    reset = "\x1b[0m"
    bold = "\x1b[1m"

    COLORS = {
        logging.DEBUG: gray + bold,
        logging.INFO: blue + bold,
        logging.WARNING: yellow + bold,
        logging.ERROR: red + bold,
        logging.CRITICAL: red + bold
    }

    def format(self, record):
        log_color = self.COLORS[record.levelno]
        format = "(black){asctime}(reset) (levelcolor){levelname:<8}(reset) (gray)[{filename}](reset) (green){name}(reset) {message}"
        format = format.replace("(black)", self.black + self.bold)
        format = format.replace("(reset)", self.reset)
        format = format.replace("(levelcolor)", log_color)
        format = format.replace("(green)", self.green + self.green)
        format = format.replace("(gray)", self.gray)
        formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S", style="{")
        return formatter.format(record)


def init_logger(logger_name: str) -> Logger:
    _logger = logging.getLogger(logger_name)
    _logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(LoggingFormatter())

    _logger.addHandler(console_handler)

    print(f"Logger {logger_name} was initialized sucessfully.")
    return _logger


logger = init_logger("bot")
dependecies.check_installed()

if github.check_for_updates(version=version.get(path_to_version=PATH)):
    latest = github.get_latest()
    logger.info(f"[GITHUB]: New update available: v{latest}")
    logger.info(f"\nCHANGELOG:\n-----------\n{github.changelog()}-----------")


class DiscordBot(commands.InteractionBot):
    def __init__(self) -> None:
        super().__init__(
            owner_ids=OWNER_IDS,
            intents=disnake.Intents.all(),
            reload=True
        )

        for extension in extensions:
            logger.info(extension + ' has been loaded')
            self.load_extension(extension)

    async def on_ready(self):
        await self.change_presence(
            status=disnake.Status.do_not_disturb,
            activity=disnake.Game("Status")
        )
        logger.info("")

    @commands.slash_command(name='cogs', guild_ids=ADMIN_GUILDS)
    async def _cogs(self, interaction: disnake.AppCommandInteraction):
        pass

    @_cogs.sub_command()
    async def load(self,
                   interaction: disnake.AppCommandInteraction,
                   extension=commands.Param(
                       choices=extensions
                   )):
        """
        Loads selected extension
        """
        bot.load_extensions(f"{PATH}/cogs/{extension}")
        embed = disnake.Embed(
            description="Extension has been loaded.",
            color=disnake.Color.green()
        )

        await interaction.send(embed=embed)

    @_cogs.sub_command()
    async def unload(self,
                     interaction: disnake.AppCommandInteraction,
                     extension=commands.Param(
                         choices=extensions
                     )):
        """
        Unloads selected extension
        """
        bot.unload_extension(f"{PATH}/cogs/{extensions}")
        embed = disnake.Embed(
            description="Extension has been unloaded.",
            color=disnake.Color.red()
        )

        await interaction.send(embed=embed)


if __name__ == "__main__":
    bot = DiscordBot()

    try:
        bot.run(config["bot"]["token"])

    except disnake.LoginFailure:
        ...

    except disnake.PrivilegedIntentsRequired:
        ...

    except Exception as e:
        print(f"{type(e).__name__}: {e}")