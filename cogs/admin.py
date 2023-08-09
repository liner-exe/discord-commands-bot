import nextcord
from nextcord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["cn"])
    @commands.is_owner()
    async def change_nickname(self, ctx, *, name: str = None):
        try:
            await ctx.guild.me.edit(nick=name)

            if name:
                return await ctx.send(f"Display name of bot has changed on **{name}**")

            elif name is None:
                return await ctx.send(f"Nickname has cleared")

        except Exception as error:
            await ctx.send(error)

    @commands.command(aliases=["cu"])
    @commands.is_owner()
    async def change_username(self, ctx, *, name: str):
        try:
            await self.client.user.edit(username=name)
            await ctx.send(f"Username of bot has changed on **{name}**")
            
        except Exception as error:
            await ctx.send(error)

    @commands.command(aliases=["dm"])
    @commands.is_owner()
    async def direct_message(self, ctx, user: nextcord.User, *, message: str):
        try:
            await user.send(message)
            await ctx.send("Message has sent")

        except nextcord.Forbidden:
            await ctx.send("User`s dm unreacheable.")

    @commands.command(aliases=["shut"], pass_context=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        print("Bot is shutting down")
        await ctx.send("Bot is shutting down")
        await self.client.close()

    @commands.is_owner()
    @commands.command()
    async def eval(self, ctx, *, content):
        try:
            embed = nextcord.Embed(description=content)
            embed.add_field(name="Result", value=eval(content))
            await ctx.send(embed=embed)

        except SyntaxError:
            await ctx.send("Incorrect expression")

        except ZeroDivisionError:
            await ctx.send("Cannot be divided by zero!")

        except Exception as error:
            print(error)


def setup(client):
    client.add_cog(Admin(client))
