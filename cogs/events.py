import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import errors


class Events(commands.Cog):
    def __init__(self, client):
        self.intents = nextcord.Intents.all()
        self.client = nextcord.Client(intents=self.intents)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err: Exception):
        if isinstance(err, errors.NotOwner):
            pass

        elif isinstance(err, errors.CommandNotFound):
            await ctx.send("Команда не найдена!")
            print(f"Команда не найдена - {ctx.message.author}: {ctx.message.content}")

        elif isinstance(err, errors.MissingPermissions):
            await ctx.send("Недостаточно прав.")

    @commands.Cog.listener()
    async def on_message(self, message):
        print("{0.guild} - {0.author}: {0.content}".format(message))

def setup(client):
    client.add_cog(Events(client))
