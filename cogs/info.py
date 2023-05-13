import nextcord
from nextcord.ext import commands
import random

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        latency = int(round(self.client.latency * 1000, 1))
        await ctx.send(f"ping is {latency} ms")

    @commands.command()
    async def developer(self, ctx):
        await ctx.send(f"**liner#9544**\nGitHub: https://github.com/r-liner")

    @commands.command()
    async def source(self, ctx):
        await ctx.send(f"**{self.client.user}** работает с помощью исходного кода: https://github.com/r-liner")

    @commands.command()
    async def servers(self, ctx):
        await ctx.send(f"Бот работает на **{str(len(self.client.guilds))}** серверах")

def setup(client):
    client.add_cog(Info(client))