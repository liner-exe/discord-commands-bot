import nextcord
from nextcord.ext import commands, application_checks
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
    async def on_application_command_error(self, interaction, error: Exception):
        embed = nextcord.Embed(title="Error", colour=nextcord.Color.red)

        if isinstance(error, application_checks.errors.ApplicationMissingPermissions):
            embed.description = "You do not have permissions to perform this action."
            embed.add_field(name="Hint", value="Permissions needed, for example: \"BAN MEMBERS\".")

        if isinstance(error, nextcord.errors.ApplicationInvokeError):
            embed.description = "Bot does not have sufficient permissions."
            embed.add_field(name="Hint", value="Give the bot administrator permissions and make its role higher than others (except admins).")
            embed.add_field(name="Hint 2", value="The error could be on the developer's side. Please report this to the developer.")

        if isinstance(error, application_checks.errors.ApplicationNSFWChannelRequired):
            embed.description = "Channel is not NSFW."
            embed.add_field(name="Hint", value="Send the command in an NSFW channel.")

    @commands.Cog.listener()
    async def on_message(self, message):
        print("{0.guild} - {0.author}: {0.content}".format(message))

        if message.author.bot:
            return
        elif message.author == self.client.user:
            return

def setup(client):
    client.add_cog(Events(client))
