import disnake
from disnake.ext import commands

import random
import logging
import string

logger = logging.getLogger("bot")

YES_NO_CHOICES = {
    "yes": "1",
    "no": "0"
}

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="dice")
    async def dice(self, interaction: disnake.AppCommandInteraction):
        logger.debug("DICE used")
        player_score, bot_score = [random.randint(1, 6) for _ in range(2)]

        embed = disnake.Embed(title="Dice")

        if player_score > bot_score:
            embed.color = disnake.Color.green()
            embed.description = "You win!"

        elif player_score == bot_score:
            embed.color = disnake.Color.yellow()
            embed.description = "Tie"

        else:
            embed.color = disnake.Color.red()
            embed.description = "Bot wins."

        embed.add_field(
            name="Bot's score",
            value=bot_score,
            inline=False
            )
        
        embed.add_field(
            name=f"{interaction.user.name}'s score",
            value=player_score,
            inline=False
            )
        
        await interaction.send(embed=embed)

    
    @commands.slash_command()
    async def roll(self, interaction: disnake.AppCommandInteraction):
        """
        Slots
        """
        emojis = ["🍎", "🍊", "🍐", "🍋", "🍉", "🍇", 
                  "🍓", "🍒", "🔔", "💎", ":seven:"]
        
        a, b, c = [random.choice(emojis) for _ in range(3)]

        if a == b == c:
            color = disnake.Color.green()
            name, value = "Epic win!", "All 3 symbols matched."
        
        elif a == b or a == c or b == c:
            color = disnake.Color.yellow()
            name, value = "You win!", "2 symbols matched."

        else:
            color = disnake.Color.red()
            name, value = "You lose!", "Nothing matched..."

        slot_machine = disnake.Embed(title="Slots", description=f"({a}|{b}|{c})",
                                     color=color)
        slot_machine.add_field(name=name, value=value)

        await interaction.send(embed=slot_machine)

    
    @commands.slash_command()
    async def password(self, 
                       interaction: disnake.AppCommandInteraction,
                       use_lower: str = commands.Param(name="use-lowercase", choices=YES_NO_CHOICES),
                       use_upper: str = commands.Param(name="use-uppercase", choices=YES_NO_CHOICES),
                       use_digits: str = commands.Param(name="use-digits", choices=YES_NO_CHOICES),
                       use_punctuation: str = commands.Param(name="use-punctuation", choices=YES_NO_CHOICES),
                       length: int = commands.Param(name="length", min_value=8, max_value=40,)
                       ):
        symbols = str()

        if use_lower:
            symbols += string.ascii_lowercase

        if use_upper:
            symbols += string.ascii_uppercase

        if use_digits:
            symbols += string.digits

        if use_punctuation:
            symbols += string.punctuation

        generated_password = "".join(random.sample(symbols, length))        

        embed = disnake.Embed(
            title="Your generated password:",
            description=generated_password + f" ({length})"
            )
        
        strength = int(use_lower) + int(use_upper) + int(use_digits) + int(use_punctuation)

        if strength == 0:
            return await interaction.send("Password length can't be zero.")

        strength_emojis = {
            "0": "",
            "1": "Too Weak ? ⚫",
            "2": "Weak ? 🔴",
            "3": "Normal ? 🟡",
            "4": "Good ? 🟢"
        }

        strength = strength_emojis[f"{strength}"].replace("?", f"({strength})")
        
        embed.add_field(name="Strength", value=strength)
        
        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))