import nextcord
from nextcord.ext import commands, application_checks
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
admin_guilds = config["settings"]["admin_guild"]


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @application_checks.is_owner()
    @nextcord.slash_command()
    async def change_nickname(self, interaction, nickname: str = nextcord.SlashOption(default=None, required=False)):
        """
        [ADMIN] Change bot nickname.

        Parameters
        ----------
        interaction: Interaction
        nickname: str
            Enter a new bot nickname.
        """
        await interaction.guild.me.edit(nick=nickname)

        if nickname:
            return await interaction.send(f"Display name of bot has changed on **{nickname}**")

        elif nickname is None:
            return await interaction.send(f"Nickname has cleared")

    @application_checks.is_owner()
    @nextcord.slash_command(guild_ids=(admin_guilds,))
    async def change_username(self, interaction, username: str = nextcord.SlashOption(default=None, required=False)):
        """
        [ADMIN] Change bot username.

        Parameters
        ----------
        interaction: Interaction
        username: str
            Enter a new bot username.
        """
        await self.client.user.edit(username=username)
        await interaction.send(f"Username of bot has changed on **{username}**")

    @application_checks.is_owner()
    @nextcord.slash_command()
    async def direct_message(self, interaction, user: nextcord.User, message: str):
        """
        [ADMIN] Send direct message to selected user.

        Parameters
        ----------
        interaction: Interaction
        user: nextcord.User
            Choose an user to dm.
        message: str
            Enter a message to send.
        """
        try:
            await user.send(message)
            await interaction.send("Message has sent")

        except nextcord.Forbidden:
            await interaction.send("User`s dm unreacheable.")

    @application_checks.is_owner()
    @nextcord.slash_command(guild_ids=(admin_guilds,))
    async def shutdown(self, interaction):
        """
        [ADMIN] Turns off the bot.
        """
        print("Bot is shutting down")
        await interaction.send("Bot is shutting down")
        await self.client.close()

    @application_checks.is_owner()
    @nextcord.slash_command(guild_ids=(admin_guilds,))
    async def eval(self, interaction, expression: str):
        """
        [ADMIN] Evaluates a Python expression.

        Parameters
        ----------
        interaction: Interaction
        expression: str
            Enter an expression to evaluate.
        """
        try:
            embed = nextcord.Embed(description=expression)
            embed.add_field(name="Result", value=eval(expression))
            await interaction.send(embed=embed)

        except SyntaxError:
            await interaction.send("Incorrect expression")

        except ZeroDivisionError:
            await interaction.send("Cannot be divided by zero!")

        except Exception as error:
            print(error)
            await interaction.send(f"Error message:\n```{error}```")


def setup(client):
    client.add_cog(Admin(client))
