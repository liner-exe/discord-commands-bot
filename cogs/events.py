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
            await ctx.send("Command not found!")
            print(f"Command not found - {ctx.message.author}: {ctx.message.content}")

        elif isinstance(err, errors.MissingPermissions):
            await ctx.send("You haven`t permissions.")

    @commands.Cog.listener()
    async def on_message(self, message):
        print("{0.guild} - {0.author}: {0.content}".format(message))

        if message.author.bot:
            return
        elif message.author == self.client.user:
            return

def setup(client):
    client.add_cog(Events(client))
