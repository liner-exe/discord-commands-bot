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
                return await ctx.send(f"Отображаемое имя бота изменено на **{name}**")

            elif name is None:
                return await ctx.send(f"Имя очищено")

        except Exception as error:
            await ctx.send(error)

    @commands.command(aliases=["cu"])
    @commands.is_owner()
    async def change_username(self, ctx, *, name: str):
        try:
            await self.client.user.edit(username=name)
            await ctx.send(f"Имя бота изменено на **{name}**")
            
        except Exception as error:
            await ctx.send(error)

    @commands.command(aliases=["dm"])
    @commands.is_owner()
    async def direct_message(self, ctx, user: nextcord.User, *, message: str):
        try:
            await user.send(message)
            await ctx.send("Сообщение отправлено")

        except nextcord.Forbidden:
            await ctx.send("У пользователя заблокированы ЛС. Или этот пользователь - бот.")

    @commands.command(aliases=["shut"], pass_context=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        print("Bot is shutting down")
        await ctx.send("Бот выключается")
        await self.client.close()


def setup(client):
    client.add_cog(Admin(client))
