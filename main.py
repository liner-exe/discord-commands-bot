import nextcord
import nextcord.errors
from nextcord.ext import commands, application_checks
import os
import sys
import configparser

intents = nextcord.Intents.all()

config = configparser.ConfigParser()
config.read("config.ini")
admin_guild = int(config['settings']['admin_guild'])

client = commands.Bot(command_prefix=config["bot"]["prefix"], owner_id=int(config["bot"]["owner_id"]), intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
	await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="bot status"))
	print("Logged in as {0.user}.".format(client))
	print("Bot is using on {0} servers!".format(len(client.guilds)))


@client.event
async def on_disconnect():
	if client.is_closed():
		await client.connect()


# WORKING WITH COGS


@application_checks.is_owner()
@client.slash_command(guild_ids=(admin_guild,))
async def load(interaction, extension):
	"""
	Loading extension

	Parameters
	----------
	interaction: Interaction
	extension: str
		Type name of extension to load.
	"""
	try:
		client.load_extension(f"cogs.{extension}")
		print(f"Cog {extension} is loaded.")
		await interaction.send(f"Cog **{str.upper(extension)}** is loaded.")

	except Exception as error:
		print(error)
		await interaction.send("Incorrect name or not able to load")


@application_checks.is_owner()
@client.slash_command(guild_ids=(admin_guild,))
async def unload(interaction, extension):
	"""
	Unloading extension

	Parameters
	----------
	interaction: Interaction
	extension: str
		Type name of extension to unload.
	"""
	try:
		client.unload_extension(f"cogs.{extension}")
		print(f"Cog {str.upper(extension)} is unloaded.")
		await interaction.send(f"Cog **{str.upper(extension)}** is unloaded.")

	except Exception as error:
		print(error)
		await interaction.send("Incorrect name or not able to unload")


@application_checks.is_owner()
@client.slash_command(guild_ids=(admin_guild,))
async def reload(interaction, extension):
	"""
	Reloading extension

	Parameters
	----------
	interaction: Interaction
	extension: str
		Type name of extension to reload.
	"""
	try:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}")
		print(f"Cog {str.upper(extension)} is reloaded.")
		await interaction.send(f"Cog **{str.upper(extension)}** is reloaded.")

	except Exception as error:
		print(error)
		await interaction.send("Incorrect name or not able to reload")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

if __name__ == '__main__':
	if sys.version_info < (3, 8):
		exit("You need Python 3.8+ to run the bot.")

	try:
		from nextcord import Intents, Client

	except ImportError:
		exit("Nextcord isn`t installed or it`s old, unsupported version.")

	try:
		client.run(config["bot"]["token"])

	except nextcord.PrivilegedIntentsRequired:
		exit("Login failure! Privileged Intents not enabled.")

	except nextcord.errors.LoginFailure:
		exit("Login failure! Token is required.")

	except Exception as err:
		print(err)
