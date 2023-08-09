import nextcord
from nextcord.ext import commands


class Discord(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Avatar
    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, *, user: nextcord.Member = None):
        user = user or ctx.author
        try:
            if user.avatar or user.guild_avatar:
                user_avatar = user.avatar.url
                embed = nextcord.Embed(title=f"Avatar of user **{user.name}**")
                embed.set_image(url=user_avatar)
                await ctx.send(embed=embed)

            elif not user.avatar and not user.guild_avatar:
                return await ctx.send("User has no avatar.")

        except Exception as err:
            print(err)


def setup(client):
    client.add_cog(Discord(client))
