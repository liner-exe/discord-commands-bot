import nextcord
from nextcord import utils, User
from nextcord.ext import commands
import random
from random import choice

intents = nextcord.Intents.all()
intents.members = True
intents.presences = True
#nextcord.member = True
intents.message_content = True

client = nextcord.Client(intents=intents)

class Events(commands.Cog):
	def __init__ (self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.bot == True:
			return
		elif message.author == client.user:
			return
		else:
			msg = message.content.lower()
		
			if msg.startswith("привет"):
				await message.channel.send(f'Приветствую, {message.author.mention}, чем могу быть полезен?')

			if msg.startswith("пока"):
				await message.channel.send(f'До новых встреч, {message.author.mention}, обращайтесь снова!')

			if msg.startswith('бот инфа'):
				infa_perc = random.randint(0, 101)
				emb1 = nextcord.Embed(
					description=f'{message.author.mention}, вероятность составляет {infa_perc}%',
					colour=0x00ffaa
					)
				await message.channel.send(embed=emb1)

			if msg.startswith('бот кто'):
				answers = ["оказывается это", "я думаю, это", "я предполагаю, это", "по моему мнению, это"]
				result = random.choice(answers)
				emb1 = nextcord.Embed(
					description=f'{message.author.mention}, {result} {choice(message.guild.members).mention}!',
					colour=0x00ffaa
					)
				await message.channel.send(embed=emb1)

			if msg.startswith('бот шип'):
				answers = ["ваша совместимость", "вы подходите друг другу на"]
				an = random.choice(answers)
				ship = random.randint(0, 100)
				embed = nextcord.Embed(
					description=f'{message.author.mention}, {an} {ship}%!',
					colour=0x00ffaa
					)
				await message.channel.send(embed=embed)
				

			if msg.startswith('бот шанс'):
				arr = ["бесспорно", "предрешено", "никаких сомнений", "определённо да", 
				"можешь быть уверен в этом", "мне кажется - да", "вероятнее всего", "хорошие перспективы",
				"знаки говорят - да", "да", "пока не ясно, попробуй снова", "спроси позже",
				"лучше не рассказывать", "сейчас нельзя предсказать", "сконцентрируйся и спроси опять",
				"даже не думай", "мой ответ - нет", "по моим данным - нет", "перспективы не очень хорошие",
				"весьма сомнительно"]
				ball = random.choice(arr)
				emb1 = nextcord.Embed(
					description=f'{message.author.mention}, 🎱 {ball}!',
					colour=0xffffff
					)
				await message.channel.send(embed=emb1)

	@commands.Cog.listener()
	async def on_member_join(self, member):
		guild = client.get_guild(guild_id)
		channel = guild.get_channel(channel_id)
		role = nextcord.utils.get(member.guild.roles, id=role_id)
		await member.add_roles(role)
		await channel.send(f'Добро пожаловать на сервер {guild.name}, {member.mention}!')
		await member.send(f'Добро пожаловать на сервер {guild.name}, {member.mention}! Oзнакомься с правилами.')

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		guild = client.get_guild(guild_id)
		channel = guild.get_channel(channel_id) 
		await channel.send(f'Прощай, {member.mention}!')

def setup(client):
	client.add_cog(Events(client))
