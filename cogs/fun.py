import asyncio

import nextcord
from nextcord.ext import commands
import random

import requests
import datetime
from datetime import timezone, timedelta
import math
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dice(self, ctx):
        player_dice, bot_dice = [random.randint(1, 6) for _ in range(2)]
        print(player_dice, bot_dice)
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

        await ctx.send(embed=embed)

    @commands.command(aliases=["slots"])
    async def roll(self, ctx):
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
        await ctx.send(embed=slotmachine)

    @commands.command(aliases=["pass"])
    async def password(self, ctx, *, lenght: int = None):
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        punct = ';;<,>.?!@#$%'

        symbols = lower + upper + digits + punct

        if 8 <= lenght <= 74:
            pass
        elif lenght > 74:
            return await ctx.send("Password must be contain 74 symbols or fewer.")
        else:
            return await ctx.send("Password must be contain 8 symbols or higher.")

        password = ''.join(random.sample(symbols, lenght))
        embed = nextcord.Embed(
            title='Password generator',
            description=f'Your random password: ``{password}``',
            timestamp=ctx.message.created_at,
            colour=0x45fc03
        )
        embed.add_field(name='Warning ⚠️', value='Password generator not recommended for use on guilds.')
        await ctx.send(embed=embed)

    @commands.command()
    async def coin(self, ctx):
        array_coins = ['heads', 'tails']
        coin_flip = random.choice(array_coins)

        embed = nextcord.Embed(description=f"Coin tossed and **{coin_flip}** falls out.", colour=0xdf03fc)
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, sentence):
        embed = nextcord.Embed(
            description=f'{sentence}',
        )
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    async def reverse(self, ctx, *, sentence):
        await ctx.send(f"{sentence[::-1]}")

    @commands.command()
    async def random(self, ctx, first_num: int = 1, *, second_num: int = 10):
        try:
            embed = nextcord.Embed(description=f"Number in range **from {first_num} to {second_num}**")
            embed.add_field(name="Result", value=f"{random.randint(first_num, second_num)}")
            await ctx.send(embed=embed)

        except Exception as error:
            print(error)

    @commands.command()
    async def guess(self, ctx):

        await ctx.reply("Type the number from 1 to 5")

        try:
            number = await self.client.wait_for('message', check=lambda message: message.author == ctx.author,
                                                timeout=7)
            h_number = random.randint(1, 5)

        except asyncio.TimeoutError:
            await ctx.send("Time is out... Try again.")

        else:
            try:
                if int(number.content) == h_number and 1 <= int(number.content) <= 5:
                    color = nextcord.Color.green()
                    result = f"**YOU RIGHT!**\n\nYour number: {number.content}\nHidden number: {h_number}"

                elif int(number.content) != h_number and 1 <= int(number.content) <= 5:
                    color = nextcord.Color.red()
                    result = f"**YOU NOT RIGHT..**\n\n**Your number:** {number.content}\n**Hidden number:** {h_number}"

                else:
                    color = nextcord.Color.yellow()
                    result = "Ooops! Error happens..."

                embed = nextcord.Embed(title="Guees the number", description=result, colour=color)
                await ctx.send(embed=embed)

            except ValueError:
                await ctx.send("I don`t get which you typed...")

    @commands.command()
    async def weather(self, ctx, *, a_city):
        try:
            ow_token = config["bot"]["openweather_token"]
            response = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={a_city}&lang=ru&units=metric&appid={ow_token}')
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

            await ctx.send(embed=embed)

        except Exception as err:
            print(err)
            await ctx.send("Incorrect city.")


def setup(client):
    client.add_cog(Fun(client))
