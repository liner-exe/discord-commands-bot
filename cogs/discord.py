import nextcord
from nextcord.ext import commands, application_checks


class Discord(commands.Cog):
    def __init__(self, client):
        self.client = client

    @application_checks.guild_only()
    @nextcord.slash_command()
    async def avatar(self, interaction, user: nextcord.Member = nextcord.SlashOption(default=None)):
        user = user or interaction.user

        if user.avatar or user.guild_avatar:
            user_avatar = user.avatar.url
            embed = nextcord.Embed(title=f"Avatar of user **{user.name}**")
            embed.set_image(url=user_avatar)
            await interaction.send(embed=embed)

        elif not user.avatar and not user.guild_avatar:
            return await interaction.send("User has no avatar.")


def setup(client):
    client.add_cog(Discord(client))
