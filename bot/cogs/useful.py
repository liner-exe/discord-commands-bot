import disnake
from disnake.ext import commands


class Useful(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="avatar")
    async def discord_avatar(self,
                             interaction: disnake.AppCommandInteraction,
                             selected_user: disnake.Member = commands.Param(
                                 name='user',
                                 default=None
                                 )
                             ):
        user = selected_user or interaction.user

        embed = disnake.Embed(color=disnake.Color.teal())

        if user.avatar or user.guild_avatar:
            user_avatar = user.avatar.url

            embed.title = f"**{user}'s** avatar"
            embed.description = f"[download avatar]({user_avatar})"
            embed.set_image(url=user_avatar)

            await interaction.send(embed=embed)

        elif not user.avatar and not user.guild_avatar:
            embed.color = disnake.Color.red()
            embed.description = "User has no avatar."

            await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(Useful(bot))