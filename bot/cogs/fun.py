import nextcord
from nextcord.ext import commands

import random
import string
import requests
import datetime
from datetime import timezone, timedelta
import math
import configparser

from .utils import (
    is_weather_active,
    generate_random_color,
    rgb_to_hex, rgb_to_hex_color,
    url_encode
)

config = configparser.ConfigParser()
config.read("config.ini")


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command()
    async def dice(self, interaction):
        """
        Just a dice.
        """
        player_dice, bot_dice = [random.randint(1, 6) for _ in range(2)]

        if player_dice > bot_dice:
            result = "You won!"
            color = nextcord.Color.green()

        elif player_dice < bot_dice:
            result = "You lost.."
            color = nextcord.Color.red()

        else:
            result = "Draw.."
            color = nextcord.Color.teal()

        embed = nextcord.Embed(title="Dice", description="\n".join([f"You: {player_dice} 🎲",
                                                                     f"{self.client.user.display_name}: {bot_dice} 🎲\n",
                                                                     f"**Result**",
                                                                     f"{result}"]),
                                colour=color)

        await interaction.send(embed=embed)

    @nextcord.slash_command()
    async def roll(self, interaction):
        """
        Slots.
        """
        emojis = ["🍎", "🍊", "🍐", "🍋", "🍉", "🍇", "🍓", "🍒", "🔔", "💎", ":seven:"]

        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        if a == b == c:
            color = 0x33ff00
            name, value = "Absolute win!", f"All 3 symbols matched."

        elif (a == b) or (a == c) or (b == c):
            color = 0xffff00
            name, value = "You won!", "All 2 symbols matched."

        else:
            color = 0xff0000
            name, value = "You lost..", "Nothing matched."

        slotmachine = nextcord.Embed(title="Slots", description=f"🎰 ({a}|{b}|{c})", colour=color)
        slotmachine.add_field(name=name, value=value)
        await interaction.send(embed=slotmachine)

    @nextcord.slash_command()
    async def password(self, interaction, length: int = nextcord.SlashOption(min_value=8, 
                                                                             max_value=74,
                                                                             default=8)):
        """
        Random password generator.

        Parameters
        ----------
        interaction: Interaction
        length: int
            Enter password length.
        """
        password = ''.join(
            random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation,
                          length))
        embed = nextcord.Embed(
            title='Password generator',
            description=f'Your random generated password: ``{password}``',
            timestamp=interaction.created_at,
            colour=0x45fc03
        )
        await interaction.send(embed=embed, ephemeral=True)

    @nextcord.slash_command()
    async def coin(self, interaction):
        """
        Heads or tails.
        """
        array_coins = ['heads', 'tails']
        coin_flip = random.choice(array_coins)

        embed = nextcord.Embed(description=f"Coin tossed and **{coin_flip}** falls out.", colour=0xdf03fc)
        await interaction.send(embed=embed)

    @nextcord.slash_command()
    async def say(self, interaction, text: str):
        """
        Say message as the bot.

        Parameters
        ----------
        interaction: Interaction
        text: str
            Enter a text to say.
        """
        embed = nextcord.Embed(
            description=f'{text}',
        )
        await interaction.send(embed=embed)

    @nextcord.slash_command()
    async def reverse(self, interaction, text: str):
        """
        Reverse entered message.

        Parameters
        ----------
        interaction: Interaction
        text: str
            Enter a text to reverse.
        """
        await interaction.send(f"{text[::-1]}")

    @nextcord.slash_command()
    async def random(self, interaction):
        ...

    @random.subcommand()
    async def number(self, interaction,
                 first_num: int = nextcord.SlashOption(name="minimum",
                                                       description="Minimum number of the range "
                                                                   "(0 if not specified)",
                                                       min_value=0, default=0),
                 second_num: int = nextcord.SlashOption(name="maximum",
                                                        description="Maximum number of the range "
                                                                    "(100 if not specified)",
                                                        min_value=0, default=100)):
        """
        Random number within the specified range.
        """
        embed = nextcord.Embed(description=f"Random number in the range **from {first_num} to {second_num}**")
        embed.add_field(name="Result", value=f"{random.randint(first_num, second_num)}")
        await interaction.send(embed=embed)

    @random.subcommand()
    async def color(self, interaction):
        """
        Random color (hex & rgb).
        """
        color = generate_random_color()
        response = requests.get(f"https://some-random-api.com/canvas/colorviewer?"
                                f"{url_encode({'hex': rgb_to_hex(color)})}")
        embed = nextcord.Embed(title="Random color", colour=rgb_to_hex_color(color))
        embed.set_thumbnail(response.url)
        embed.add_field(name="HEX", value=f"#{rgb_to_hex(color)}")
        embed.add_field(name="RGB", value=f"{color[0]}, {color[1]}, {color[2]}")

        await interaction.send(embed=embed)

    @is_weather_active
    @nextcord.slash_command()
    async def weather(self, interaction, _city = nextcord.SlashOption(name="city")):
        """
        Get a weather forecast in certain city.

        Parameters
        ----------
        interaction: Interaction
        _city: str
            Enter a city to get weather forecast.
        """
        try:
            ow_token = config["bot"]["openweather_token"]
            response = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={_city}&lang=ru&units=metric&appid={ow_token}')
            data = response.json()

            city = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]
            time_zone = data["timezone"]

            sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M %d/%m/%Y')
            sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M %d/%m/%Y')

            emoji = {
                "Clear": "Clear \U00002600",
                "Clouds": "Clouds \U00002601",
                "Rain": "Rain \U00002614",
                "Drizzle": "Drizzle \U00002614",
                "Thunderstorm": "Thunder \U000026A1",
                "Snow": "Snow \U0001F328",
                "Mist": "Mist \U0001F32B"
            }

            weather_description = data["weather"][0]["main"]

            if weather_description in emoji:
                wd = emoji[weather_description]
            else:
                wd = "X"

            tz = timezone(timedelta(seconds=time_zone))

            embed = nextcord.Embed(description=f"Weather forecast in **{city} city**")
            embed.add_field(name="Date", value=f"{datetime.datetime.now(tz).strftime('%d/%m/%Y')}")
            embed.add_field(name="Time", value=f"{datetime.datetime.now(tz).strftime('%H:%M')}")
            embed.add_field(name="Weather", value=f"{wd}")
            embed.add_field(name="Temperature", value=f"{temperature}°C")
            embed.add_field(name="Humidity", value=f"{humidity}%")
            embed.add_field(name="Pressure", value=f"{math.ceil(pressure / 1.333)} mmHg.")
            embed.add_field(name="Wind", value=f"{wind} meters/second")
            embed.add_field(name="Sunrise", value=f"{sunrise_timestamp}")
            embed.add_field(name="Sunset", value=f"{sunset_timestamp}")

            await interaction.send(embed=embed)

        except Exception as err:
            print(err)
            await interaction.send("Incorrect city.")


def setup(client):
    client.add_cog(Fun(client))
