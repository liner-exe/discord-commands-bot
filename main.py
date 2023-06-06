import nextcord
from nextcord.ext import commands, tasks
import os
from itertools import cycle

# интенты

intents = nextcord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
nextcord.member = True

# всякое важное

prefix = '.'
owner_id = 923915325668487190 # замени на свой айди учётной записи дискорд здесь
client = commands.Bot(command_prefix=prefix, owner_id=owner_id, intents=intents)
client.remove_command('help') 

# token = os.getenv("token") для replit
token = open ("token.txt", "r").readline()

# статус

status = cycle(['.help', 'use .help for help', 'created by liner#9544'])

@tasks.loop(seconds=10)
async def change_status():
	await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=next(status)))
		# await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name='.help'))
		# await client.change_presence(activity=nextcord.Streaming(name='.help', url=''))
		# await client.change_presence(status=nextcord.Status.Online, activity=nextcord.game('.help'))

# ивенты

@client.event
async def on_ready():
	change_status.start()
	print("Logged in as {0.user}.".format(client))
	print("Bot is using on " + str(len(client.guilds)) + ' servers!')

# загрузка когов

@client.command()
@commands.is_owner()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")
	print("Cogs is loaded.")
	await ctx.send("Cog is loaded.")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	print("Cog is unloaded.")
	await ctx.send("Cog is unloaded.")

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	client.load_extension(f"cogs.{extension}")
	print("Cog is re-loaded.")
	await ctx.send("Cog is reloaded.")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
