import discord
from discord.ext import commands, tasks
import os
from itertools import cycle

# интенты

intents = discord.Intents.all()
intents.members = True
intents.presences = True
discord.member = True

# всякое важное

prefix = '.'
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help') 

token = os.getenv("token")
owner_id = # добавь сам

# статус

status = cycle(['.help', 'use .help for help', 'created by liner#9544'])

@tasks.loop(seconds=10)
async def change_status():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))
		# await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='.help'))
		# await client.change_presence(activity=discord.Streaming(name='.help', url=''))
		# await client.change_presence(status=discord.Status.Online, activity=discord.game('.help'))

# ивенты

@client.event
async def on_ready():
	change_status.start()
	print("Logged in as {0.user}.".format(client))
	print("Bot is using on " + str(len(client.guilds)) + ' servers!')

# загрузка когов

@client.command()
async def load(ctx, extension):
	if ctx.author.id == owner_id:
		client.load_extension(f"cogs.{extension}")
		print("Cogs is loaded.")
		await ctx.send("Cog is loaded.")
	else:
		await ctx.send("Недостаточно прав.")

@client.command()
async def unload(ctx, extension):
	if ctx.author.id == owner_id:
		client.unload_extension(f"cogs.{extension}")
		print("Cogs is unloaded.")
		await ctx.send("Cog is unloaded.")
	else:
		await ctx.send("Недостаточно прав.")

@client.command()
async def reload(ctx, extension):
	if ctx.author.id == owner_id:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}")
		print("Cogs is re-loaded.")
		await ctx.send("Cog is reloaded.")
	else:
		await ctx.send("Недостаточно прав.")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
