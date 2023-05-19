import nextcord
from nextcord.ext import commands
import random

class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def dice(self, ctx):
		player_dice, bot_dice = [random.randint(2, 12) for i in range (2)]

		emb = nextcord.Embed(
			description="\n".join([f"**Ваше число**: {player_dice} 🎲",
								   f"Число **{self.client.user.display_name}**: {bot_dice} 🎲"]),
			colour=0xfc0362
		)
		if player_dice > bot_dice:
			emb.add_field(name = "Результат", value = "Вы победили!")
		elif bot_dice > player_dice:
			emb.add_field(name="Результат", value="Вы проиграли..")
		await ctx.send(embed=emb)

	@commands.command()
	async def roll(self, ctx):
		emojis = "🍎🍊🍐🍋🍉🍇🍓🍒🔔💎🅱️7️⃣"

		a = random.choice(emojis)
		b = random.choice(emojis)
		c = random.choice(emojis)

		if (a == b == c):
			slotmachine = nextcord.Embed(title="Slot machine", description=f"🎰 ({a}|{b}|{c})", colour=0x33ff00)
			slotmachine.add_field(name="Вы победили!", value="Все 3 совпали.")
			await ctx.send(embed=slotmachine)

		if (a == b) or (a == c) or (b == c):
			slotmachine = nextcord.Embed(title="Slot machine", description=f"🎰 ({a}|{b}|{c})", colour=0xffff00)
			slotmachine.add_field(name="Вы победили!", value="2 символа совпали.")
			await ctx.send(embed=slotmachine)

		else:
			slotmachine = nextcord.Embed(title="Slot machine", description=f"🎰 ({a}|{b}|{c})", colour=0xff0000)
			slotmachine.add_field(name="Вы проиграли..", value="Ничего не совпало.")
			await ctx.send(embed=slotmachine)

	@commands.command()
	async def password(self, ctx, *, lenght : int = None):
		lower = 'abcdefghijklmnopqrstuvwxyz'
		upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		digits = '0123456789'
		punct = ';;<,>.?!@#$%'

		symb = lower + upper + digits + punct

		if lenght >= 8 and lenght <= 74:
			pass
		elif lenght > 74:
			return await ctx.send("Пароль может быть не более 74 символов.")
		else:
			return await ctx.send("Пароль должен быть не менее 8 символов.")

		ps = ''.join(random.sample(symb, lenght))
		embed = nextcord.Embed(
			title='Password generator',
			description=f'Ваш рандомный пароль: ``{ps}``',
			timestamp=ctx.message.created_at,
			colour = 0x45fc03
			)
		embed.add_field(name='Внимание ⚠️', value='Генератор паролей не рекомендуется использовать на серверах.')
		await ctx.send(embed=embed)

	@commands.command()
	async def coin(self, ctx):
		arr_monetka = ['Орёл', 'Решка']
		x_moneta = random.choice(arr_monetka)
		if x_moneta == 'Орёл':
			emb1=nextcord.Embed(
				description=f"Монетка подкинута и выпал **{x_moneta}**.",
				colour=0xdf03fc
				)
			await ctx.send(embed=emb1)
		else:
			emb2=nextcord.Embed(
				description=f"Монетка подкинута и выпала **{x_moneta}**.",
				colour=0xdf03fc
				)
			await ctx.send(embed=emb2)

	@commands.command()
	async def say(self, ctx, *, word):
		embed=nextcord.Embed(
			description=f'{word}',
			)
		await ctx.send(embed=embed)
		await ctx.message.delete()

	@commands.command()
	async def eval(self, ctx, *, content):
		try:
			embed = nextcord.Embed(description=content)
			embed.add_field(name="Результат", value=eval(content))
			await ctx.send(embed=embed)

		except SyntaxError:
			await ctx.send("Недопустимое выражение")

		except ZeroDivisionError:
			await ctx.send("Нельзя делить на ноль!")

		except Exception as error:
			await ctx.send(error)

def setup(client):
	client.add_cog(Fun(client))
