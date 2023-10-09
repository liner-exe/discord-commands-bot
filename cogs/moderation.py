import nextcord
from typing import Optional
from nextcord.ext import commands
from nextcord import Member


class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	# Closing channel

	@commands.command(aliases=["lock"])
	@commands.has_permissions(manage_channels=True)
	async def lockdown(self, ctx):
		await ctx.message.delete()
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
		await ctx.send(ctx.channel.mention + " - **Channel locked.**")
	
	# Opening channel

	@commands.command()
	@commands.has_permissions(manage_channels=True)
	async def unlock(self, ctx):
		await ctx.message.delete()
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
		await ctx.send( ctx.channel.mention + " - **Channel unclocked.**")

	# Ban

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: Member, *, reason: Optional[str] = "No reason."):
		await ctx.message.delete()
		await ctx.channel.trigger_typing()
		embed = nextcord.Embed(description=f"🚫 User **{member.name}** banned!", colour=0xff0000)
		embed.add_field(name="User", value=f"{member.mention}")
		embed.add_field(name="Reason", value=f"{reason}")
		embed.set_footer(text=f'Administrator - {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar.url)
		await ctx.send(embed=embed)
		await member.ban(reason=reason)

	# Unban

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def unban(self, ctx, *, member, reason: Optional[str] = "No reason."):
		await ctx.message.delete()
		await ctx.channel.trigger_typing()
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split("#")

		for ban_entry in banned_users:
			user = ban_entry.user

			if(user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.channel.trigger_typing()
				await ctx.guild.unban(user)
				embed = nextcord.Embed(description=f"✅ User **{user.name}** unbanned!", colour=0x33ff00)
				embed.add_field(name="User", value=f"{user.mention}")
				embed.add_field(name="Reason", value=f"{reason}")
				embed.set_footer(text=f'Administrator - {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar.url)
				await ctx.send(embed=embed)
				return

	# Kick

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: nextcord.Member, *, reason: Optional[str] = "No reason."):
		await ctx.message.delete()
		await ctx.channel.trigger_typing()
		await member.kick(reason=reason)

		embed = nextcord.Embed(description=f"❌ User **{member.name}** kicked!", colour=0xff0000)
		embed.add_field(name="User", value=f"{member.mention}", inline=True)
		embed.add_field(name="Reason", value=f"{reason}", inline=True)
		embed.set_footer(text=f'Administrator - {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar.url)
		await ctx.send(embed=embed)

	# Clear / Purge

	@commands.command(aliases=["purge"])
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, *, amount: int = None):
		try:
			await ctx.channel.purge(limit=amount+1)
			await ctx.send(f'{amount} messages deleted.')

		except Exception as error:
			await ctx.send(error)

		except PermissionError:
			await ctx.send("You haven`t permissions.")


def setup(client):
	client.add_cog(Moderation(client))
