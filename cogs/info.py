import os
from datetime import timedelta
from time import time
import nextcord
from nextcord.ext import commands
import psutil
from platform import python_version
from nextcord import __version__ as nextcord_version


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.process = psutil.Process(os.getpid())

    @commands.command()
    async def ping(self, ctx):
        latency = int(round(self.client.latency * 1000, 1))
        embed = nextcord.Embed(title="Ping",
                               description=f"Latency is **{latency} ms**",
                               colour=nextcord.Color.teal())
        await ctx.send(embed=embed)

    @commands.command(aliases=['dev'])
    async def developer(self, ctx):
        embed = nextcord.Embed(title="Developer: **liner#9544**",
                               description=f"[GitHub](https://github.com/r-liner)",
                               colour=nextcord.Color.teal())
        await ctx.send(embed=embed)

    @commands.command()
    async def source(self, ctx):
        embed = nextcord.Embed(title=f"Source **{self.client.user}**",
                               description=f"[GitHub](https://github.com/r-liner/discord-bot-ru/tree/master)",
                               colour=nextcord.Color.teal())
        await ctx.send(embed=embed)

    @commands.command()
    async def servers(self, ctx):
        embed = nextcord.Embed(title=f"Guilds",
                               description=f"Bot works on **{str(len(self.client.guilds))}** guilds",
                               colour=nextcord.Color.teal())
        await ctx.send(embed=embed)

    @commands.command()
    async def stats(self, ctx):
        ram_usage = round(self.process.memory_full_info().rss / 1024**2, 1)
        ram_perc_usage = round(self.process.memory_percent(), 1)
        cpu_usage = round(psutil.cpu_percent(), 1)

        with self.process.oneshot():
            uptime = timedelta(seconds=time()-self.process.create_time())
            uptime = str(uptime).split('.')[0]

        with open('version.txt', 'r') as file:
            version = file.read()

        embed = nextcord.Embed(colour=nextcord.Color.teal())

        embed.add_field(name="Python Version", value=python_version(), inline=True)
        embed.add_field(name="Nextcord version", value=nextcord_version, inline=True)
        embed.add_field(name="Bot Version", value=version, inline=True)
        embed.add_field(name="Uptime", value=uptime)
        embed.add_field(name="RAM Usage", value=f"{ram_usage} MiB | {ram_perc_usage} %")
        embed.add_field(name="CPU Usage", value=f"{cpu_usage} %")
        embed.add_field(name="Servers", value=len(ctx.bot.guilds))
        embed.add_field(name="Ping", value=int(round(self.client.latency * 1000, 1)))
        embed.add_field(name="Commands", value=len([x.name for x in self.client.commands]))

        await ctx.send("📊 **Stats**", embed=embed)


def setup(client):
    client.add_cog(Info(client))
