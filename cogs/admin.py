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
    async def change_nickname(self, interaction, name: str = nextcord.SlashOption(default=None)):
        """
        Change nickname of certain user.
        """
        await interaction.guild.me.edit(nick=name)

        if name:
            return await interaction.send(f"Display name of bot has changed on **{name}**")

        elif name is None:
            return await interaction.send(f"Nickname has cleared")

    @application_checks.is_owner()
    @nextcord.slash_command(guild_ids=(admin_guilds,))
    async def change_username(self, interaction, name: str = nextcord.SlashOption(default=None)):
        """
        Change bot nickname.
        """
        await self.client.user.edit(username=name)
        await interaction.send(f"Username of bot has changed on **{name}**")

    @application_checks.is_owner()
    @nextcord.slash_command()
    async def direct_message(self, interaction, user: nextcord.User, message: str):
        """
        Send direct message to selected user.
        """
        try:
            await user.send(message)
            await interaction.send("Message has sent")

        except nextcord.Forbidden:
            await interaction.send("User`s dm unreacheable.")

    @application_checks.is_owner()
    @nextcord.slash_command(guild_ids=(admin_guilds,))
    async def shutdown(self, interaction):
        print("Bot is shutting down")
        await interaction.send("Bot is shutting down")
        await self.client.close()

    @application_checks.is_owner()
    @nextcord.slash_command(guild_ids=(admin_guilds,))
    async def eval(self, interaction, content):
        try:
            embed = nextcord.Embed(description=content)
            embed.add_field(name="Result", value=eval(content))
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
