import nextcord
from nextcord.ext import commands
import random
from random import choice

class Fun(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def dice(self, ctx):
		x_dice = random.randint(2, 12)
		emb=nextcord.Embed(
			description=f"Кубики подброшены... И выпало число {x_dice} 🎲",
			colour=0xfc0362
			)
		await ctx.send(embed=emb)

	@commands.command()
	async def roll(self, ctx):
		emojis = ["🍎", "🍊", "🍐", "🍋", "🍉", "🍇", "🍓", "🍒", "🔔", "💎", "🅱️", "7️⃣"]

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
	async def password(self, ctx):
		lower = 'abcdefghijklmnopqrstuvwxyz'
		upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		digits = '0123456789'
		punct = ';;<,>.?!@#$%'

		symb = lower + upper + digits + punct

		lenght = 16
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
	async def say(self, ctx, word):
		embed=nextcord.Embed(
			description=f'{word}',
			)
		await ctx.send(embed=embed)
		await ctx.message.delete()

def setup(client):
	client.add_cog(Fun(client))
