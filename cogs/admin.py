from nextcord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def change_nickname(self, ctx, *, name: str = None):
        try:
            await ctx.guild.me.edit(nick=name)
            if name:
                return await ctx.send(f"Изменено на {name}")
            elif name == None:
                return await ctx.send(f"Имя очищено")
        except Exception as error:
            await ctx.send(error)

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        print("Bot is shutting down")
        await ctx.send("Бот выключается")
        await self.client.close()

def setup(client):
    client.add_cog(Admin(client))
