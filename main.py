import nextcord
import nextcord.errors
from nextcord.ext import commands, tasks
import os
from itertools import cycle
import sys
import configparser


intents = nextcord.Intents.all()

config = configparser.ConfigParser()
config.read("config.ini")

if sys.version_info < (3, 8):
	exit("You need Python 3.8+ to run the bot.")

try:
	from nextcord import Intents, Client

except ImportError:
	exit("Nextcord isn`t installed or it`s old, unsupported version.")

client = commands.Bot(command_prefix=config["bot"]["prefix"], owner_id=int(config["bot"]["owner_id"]), intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
	await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="bot status"))
	print("Logged in as {0.user}.".format(client))
	print("Bot is using on {0} servers!".format(len(client.guilds)))

# загрузка когов


@client.command()
@commands.is_owner()
async def load(ctx, extension):
	try:
		client.load_extension(f"cogs.{extension}")
		print(f"Cog {extension} is loaded.")
		await ctx.send(f"Cog **{str.upper(extension)}** is loaded.")

	except Exception as error:
		print(error)
		await ctx.send("Неверное имя или невозможно загрузить")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
	try:
		client.unload_extension(f"cogs.{extension}")
		print(f"Cog {str.upper(extension)} is unloaded.")
		await ctx.send(f"Cog **{str.upper(extension)}** is unloaded.")

	except Exception as error:
		print(error)
		await ctx.send("Неверное имя или невозможно загрузить")


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
	try:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}")
		print(f"Cog {str.upper(extension)} is reloaded.")
		await ctx.send(f"Cog **{str.upper(extension)}** is reloaded.")

	except Exception as error:
		print(error)
		await ctx.send("Неверное имя или невозможно загрузить")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

try:
	client.run(config["bot"]["token"])

except Exception as err:
	print(err)

except nextcord.PrivilegedIntentsRequired:
	exit("Login failure! Privileged Intents not enabled.")

except nextcord.errors.LoginFailure:
	exit("Login failure! Token is required.")
