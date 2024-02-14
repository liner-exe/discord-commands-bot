import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Member

import asyncio


class Moderation(commands.Cog):
	def __init__(self, client):
		self.client = client

	@application_checks.has_permissions(manage_channels=True)
	@nextcord.slash_command()
	async def lockdown(self, interaction):
		"""
		Lock a channel.
		"""
		current_permissions = interaction.channel.overwrites_for(interaction.guild.default_role)
		current_permissions.send_messages = False
		await interaction.channel.set_permissions(interaction.guild.default_role, overwrite=current_permissions)
		embed = nextcord.Embed(description=f"**🔒 Channel locked**\n\n{interaction.channel.mention}")
		embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)

		await interaction.send(embed=embed)

	@application_checks.has_permissions(manage_channels=True)
	@nextcord.slash_command()
	async def unlock(self, interaction):
		"""
		Open a channel.
		"""
		embed = nextcord.Embed(title="Channel Unlocked", description=interaction.channel.mention,
                       colour=nextcord.Color.brand_green())
		embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)

		current_permissions = interaction.channel.overwrites_for(interaction.guild.default_role)

		if current_permissions.send_messages is True:
			return await interaction.send("**You cannot unlock a channel that is not locked!**",
										ephemeral=True)

		current_permissions.send_messages = True
		await interaction.channel.set_permissions(interaction.guild.default_role, overwrite=current_permissions)

		await interaction.send(embed=embed)

	@application_checks.has_permissions(ban_members=True)
	@nextcord.slash_command()
	async def ban(self, interaction, member: Member, reason: str = nextcord.SlashOption(default="No reason.")):
		"""
		Ban a certain user.

		Parameters
		----------
		interaction: Interaction
		member: int
			Choose an user.
		reason: str
			Type a reason.
		"""
		embed = nextcord.Embed(title='Ban', colour=nextcord.Colors.light_red)

		error_embed = nextcord.Embed(title="Error", colour=nextcord.Colors.light_red)

		if member.bot:
			error_embed.description = "**You cannot ban a bot!**"
			return await interaction.send(embed=error_embed, ephemeral=True)

		elif interaction.user.id == member.id:
			error_embed.description = "**You cannot ban yourself!**"
			return await interaction.send(embed=error_embed, ephemeral=True)

		else:
			embed.description = f"🚫 User **{member.name}** has been banned!"
			embed.add_field(name="User", value=member.mention)
			embed.add_field(name="Reason", value=reason)
			embed.set_footer(text=f'Administrator - {interaction.user.name}',
							icon_url=interaction.user.avatar.url)
			await member.ban(reason=reason)
			await interaction.send(embed=embed)

	@application_checks.has_permissions(administrator=True)
	@nextcord.slash_command()
	async def unban(self, interaction, member: nextcord.Member, reason: str = nextcord.SlashOption(default="No reason.")):
		"""
		Ban a certain user.

		Parameters
		----------
		interaction: Interaction
		member: nextcord.Member
			Choose an user.
		reason: str
			Type a reason.
		"""
		banned_users = await interaction.guild.fetch_ban(user=member)

		embed = nextcord.Embed(title='Unban')

		if interaction.user.id == member.id:
			embed.title = 'Error'
			embed.description = "You cannot unban yourself!"
			embed.colour = nextcord.Color.red()
			return await interaction.send(embed=embed, ephemeral=True)

		if member.bot:
			embed.title = 'Error'
			embed.description = "Cannot unban the user. User is a bot."
			embed.colour = nextcord.Color.red()
			return await interaction.send(embed=embed, ephemeral=True)

		if banned_users:
			await interaction.guild.unban(member)

			embed.description = f"✅ User **{member.name}** has been unbanned!"
			embed.colour = nextcord.Color.green()

			embed.add_field(name="User", value=f"{member.mention}")
			embed.add_field(name="Reason", value=f"{reason}")
			embed.set_footer(text=f'Administrator - {interaction.user.name}',
							icon_url=interaction.user.avatar.url)
			await interaction.send(embed=embed)
		else:
			embed.description = "❌ The specified user is not banned."
			embed.colour = nextcord.Color.fuchsia()
			await interaction.send(embed=embed, ephemeral=True)

	@application_checks.has_permissions(kick_members=True)
	@nextcord.slash_command()
	async def kick(self, interaction, member: nextcord.Member, reason: str = nextcord.SlashOption(default="No reason.")):
		"""
		Kick an user.

		Parameters
		----------
		interaction: Interaction
		member: nextcord.Member
			Choose an user.
		reason: str
			Type a reason.
		"""
		embed = nextcord.Embed(title='Kick')

		if interaction.user.id == member.id:
			embed.title = 'Error'
			embed.description = "You cannot kick yourself!"
			embed.colour = nextcord.Color.red()
			return await interaction.send(embed=embed, ephemeral=True)

		if member.bot:
			embed.title = 'Error'
			embed.description = "Cannot kick the user. User is a bot."
			embed.colour = nextcord.Color.red()
			return await interaction.send(embed=embed, ephemeral=True)

		await member.kick(reason=reason)

		embed.description = f"❌ User **{member.name}** has been kicked!"
		embed.colour = nextcord.Color.yellow()

		embed.add_field(name="User", value=f"{member.mention}", inline=True)
		embed.add_field(name="Reason", value="Not specified." if not reason else reason, inline=True)
		embed.set_footer(text=f'Administrator - {interaction.user.name}', icon_url=interaction.user.avatar.url)
		await interaction.send(embed=embed)

	@application_checks.has_permissions(manage_messages=True)
	@nextcord.slash_command()
	async def clear(self, interaction, amount: int = nextcord.SlashOption(min_value=1, max_value=100)):
		"""
		Kick an user.

		Parameters
		----------
		interaction: Interaction
		member: int
			Type a count of messages to delete.
		"""
		deleted = await interaction.channel.purge(limit=amount)

		msg = await interaction.send(f'Messages deleted: **{len(deleted)}**')
		await asyncio.sleep(3)
		await msg.delete()


def setup(client):
	client.add_cog(Moderation(client))
