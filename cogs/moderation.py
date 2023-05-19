import discord
import nextcord
from typing import Optional
from nextcord.ext import commands
from nextcord import Member

class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	# Закрытие канала

	@commands.command(name="Блокировка канала", aliases=["lockdown", "lock", "заблокировать"])
	@commands.has_permissions(manage_channels=True)
	async def lockdown(self, ctx):
		await ctx.message.delete()
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
		await ctx.send( ctx.channel.mention + " - **Канал заблокирован.**")
	
	# Открытие канала

	@commands.command(name="Разблокировка канала", aliases=["разблокировать", "unlock"])
	@commands.has_permissions(manage_channels=True)
	async def unlock(self, ctx):
		await ctx.message.delete()
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
		await ctx.send( ctx.channel.mention + " - **Канал разблокирован.**")

	# Бан

	@commands.command(name="Бан", aliases=["ban", "бан"])
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx, member: Member, *, reason : Optional[str] = "Причина не указана."):
		await ctx.message.delete()
		await ctx.channel.trigger_typing()
		embed = nextcord.Embed(description=f"🚫 Пользователь **{member.name}** забанен!", colour=0xff0000)
		embed.add_field(name="Пользователь", value=f"{member.mention}")
		embed.add_field(name="Причина", value=f"{reason}")
		embed.set_footer(text=f'Администратор - {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar.url)
		await ctx.send(embed=embed)
		await member.ban(reason=reason)

	# Разбан

	@commands.command(name="Разбан", aliases=["unban", "разбан"])
	@commands.has_permissions(administrator = True)
	async def unban(self, ctx, *, member, reason : Optional[str] = "Причина не указана."):
		await ctx.message.delete()
		await ctx.channel.trigger_typing()
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split("#")

		for ban_entry in banned_users:
			user = ban_entry.user

			if(user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.channel.trigger_typing()
				await ctx.guild.unban(user)
				embed = nextcord.Embed(description=f"✅ Пользователь **{user.name}** разбанен!", colour=0x33ff00)
				embed.add_field(name="Пользователь", value=f"{user.mention}")
				embed.add_field(name="Причина", value=f"{reason}")
				embed.set_footer(text=f'Администратор - {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar.url)
				await ctx.send(embed=embed)
				return

	@commands.command(name="Кик", aliases=["kick", "кик"])
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member : discord.Member, *, reason : Optional[str] = "Не указана."):
		await ctx.message.delete()
		await ctx.channel.trigger_typing()
		await member.kick(reason=reason)

		embed = nextcord.Embed(description=f"❌ Пользователь **{member.name}** кикнут!", colour=0xff0000)
		embed.add_field(name="Пользователь", value=f"{member.mention}", inline=True)
		embed.add_field(name="Причина", value=f"{reason}", inline=True)
		embed.set_footer(text=f'Администратор - {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar.url)
		await ctx.send(embed=embed)

	@commands.command(name="1", aliases=["очистить", "clear"])
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, *, amount : int = None):
		try:
			await ctx.channel.purge(limit=amount+1)
			if amount == 1:
				await ctx.send(f'Удалено {amount} сообщение.')
			elif amount == 2 or amount == 3 or amount == 4:
				await ctx.send(f'Удалено {amount} сообщения.')
			else:
				await ctx.send(f'Удалено {amount} сообщений.')

		except Exception as error:
			await ctx.send(error)
def setup(client):
	client.add_cog(Moderation(client))
