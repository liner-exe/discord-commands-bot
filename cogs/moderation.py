import discord
import asyncio
from typing import Optional
from discord.ext import commands
from discord import Member

client = commands.Bot(command_prefix = '.')

class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	# Закрытие канала

	@commands.command(name="Блокировка канала", aliases=["lock", "заблокировать", "залочь"])
	@commands.has_permissions(manage_channels=True)
	async def lockdown(self, ctx):
		await ctx.message.delete()
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
		await ctx.send( ctx.channel.mention + " - **Канал заблокирован.**")
	
	# Открытие канала

	@commands.command(name="Разблокировка канала", aliases=["разблокировать", "разлочь"])
	@commands.has_permissions(manage_channels=True)
	async def unlock(self, ctx):
		await ctx.message.delete()
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
		await ctx.send( ctx.channel.mention + " - **Канал разблокирован.**")

	# Бан

	@commands.command(name="Бан", aliases=["ban"])
	@commands.has_permissions(ban_members = True)
	async def бан(self, ctx, member: Member, *, reason : Optional[str] = "Причина не указана."):
		await ctx.message.delete()
		await ctx.channel.trigger_typing()
		embed = discord.Embed(description=f"🚫 Пользователь **{member.name}** забанен!", colour=0xff0000)
		# embed.set_author(name=member, icon_url=member.avatar_url)
		# embed.add_field(name='Бан!', value=f'Пользователь {member.mention} забанен по причине:\n{reason}')
		embed.add_field(name="Пользователь", value=f"{member.mention}")
		embed.add_field(name="Причина", value=f"{reason}")
		embed.set_footer(text=f'Администратор - {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)
		await member.ban(reason=reason)

	# Разбан

	@commands.command(name="Разбан", aliases=["unban"])
	@commands.has_permissions(administrator = True)
	async def разбан(self, ctx, *, member, reason : Optional[str] = "Причина не указана."):
		await ctx.message.delete()
		await ctx.channel.trigger_typing()
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split("#")

		for ban_entry in banned_users:
			user = ban_entry.user

			if(user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.channel.trigger_typing()
				await ctx.guild.unban(user)
				embed = discord.Embed(description=f"✅ Пользователь **{user.name}** разбанен!", colour=0x33ff00)
				embed.add_field(name="Пользователь", value=f"{user.mention}")
				embed.add_field(name="Причина", value=f"{reason}")
				embed.set_footer(text=f'Администратор - {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
				await ctx.send(embed=embed)
				return
      
def setup(client):
	client.add_cog(Moderation(client))
