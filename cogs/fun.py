import asyncio

import nextcord
from nextcord.ext import commands
import random

import requests
import datetime
from datetime import timezone, timedelta
import math
import configparser

from embed.colors import Colors

config = configparser.ConfigParser()
config.read("config.ini")


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dice(self, ctx):
        try:
            player_dice, bot_dice = [random.randint(2, 12) for _ in range(2)]

            if player_dice > bot_dice:
                result = "Вы победили!"
                color = Colors.light_green

            elif bot_dice > player_dice:
                result = "Вы проиграли.."
                color = Colors.light_red

            elif bot_dice == player_dice:
                result = "Ничья.."
                color = Colors.teal

            embed = nextcord.Embed(title="Кости", description="\n".join([f"Вы: {player_dice} 🎲",
                                                                         f"{self.client.user.display_name}: {bot_dice} 🎲\n",
                                                                         f"**Результат**",
                                                                         f"{result}"]),
                                   colour=color
                                   )

            await ctx.send(embed=embed)

        except Exception as error:
            print(error)

    @commands.command(aliases=["slots"])
    async def roll(self, ctx):
        emojis = ["🍎", "🍊", "🍐", "🍋", "🍉", "🍇", "🍓", "🍒", "🔔", "💎", ":seven:"]

        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        if a == b == c:
            color = 0x33ff00
            name, value = "Абсолютная победа!", f"Все 3 символа совпали."

        elif (a == b) or (a == c) or (b == c):
            color = 0xffff00
            name, value = "Вы победили!", "2 символа совпали."

        else:
            color = 0xff0000
            name, value = "Вы проиграли..", "Ничего не совпало."

        slotmachine = nextcord.Embed(title="Слоты", description=f"🎰 ({a}|{b}|{c})", colour=color)
        slotmachine.add_field(name=name, value=value)
        await ctx.send(embed=slotmachine)

    @commands.command(aliases=["pass", "пароль"])
    async def password(self, ctx, *, lenght: int = None):
        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        punct = ';;<,>.?!@#$%'

        symbols = lower + upper + digits + punct

        if 8 <= lenght <= 74:
            pass
        elif lenght > 74:
            return await ctx.send("Пароль может быть не более 74 символов.")
        else:
            return await ctx.send("Пароль должен быть не менее 8 символов.")

        password = ''.join(random.sample(symbols, lenght))
        embed = nextcord.Embed(
            title='Password generator',
            description=f'Ваш рандомный пароль: ``{password}``',
            timestamp=ctx.message.created_at,
            colour=0x45fc03
        )
        embed.add_field(name='Внимание ⚠️', value='Генератор паролей не рекомендуется использовать на серверах.')
        await ctx.send(embed=embed)

    @commands.command()
    async def coin(self, ctx):
        array_coins = ['Орёл', 'Решка']
        coin_flip = random.choice(array_coins)

        if coin_flip == 'Орёл':
            description = f"Монетка подкинута и выпал **{coin_flip}**."
        else:
            description = f"Монетка подкинута и выпала **{coin_flip}**."

        embed = nextcord.Embed(description=description, colour=0xdf03fc)
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

    @commands.command(name="Рандомное число")
    async def random(self, ctx, first_num: int = 0, *, second_num: int = 10):
        try:
            embed = nextcord.Embed(description=f"Число в диапозоне **от {first_num} до {second_num}**")
            embed.add_field(name="Результат", value=f"{random.randint(first_num, second_num)}")
            await ctx.send(embed=embed)

        except Exception as error:
            print(error)

    @commands.command()
    async def guess(self, ctx):

        await ctx.reply("Напиши число от 1 до 5")

        try:
            number = await self.client.wait_for('message', check=lambda message: message.author == ctx.author,
                                                timeout=7)
            h_number = random.randint(1, 5)

        except asyncio.TimeoutError:
            await ctx.send("Время вышло... Попробуйте снова.")

        else:
            try:
                if int(number.content) == h_number and 1 <= int(number.content) <= 5:
                    color = Colors.light_green
                    result = f"**ВЫ УГАДАЛИ!**\n\nВаше число: {number.content}\nЗагаданное число: {h_number}"

                elif int(number.content) != h_number and 1 <= int(number.content) <= 5:
                    color = Colors.light_red
                    result = f"**ВЫ НЕ УГАДАЛИ..**\n\n**Ваше число:** {number.content}\n**Загаданное число:** {h_number}"

                else:
                    color = Colors.yellow
                    result = "Ой! Ошибочка вышла..."

                embed = nextcord.Embed(title="Угадай число", description=result, colour=color)
                await ctx.send(embed=embed)

            except ValueError:
                await ctx.send("Я не понял, что вы написали...")

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
            print(error)

    @commands.command()
    async def weather(self, ctx, a_city):
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

            sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

            emoji = {
                "Clear": "Ясно \U00002600",
                "Clouds": "Облачно \U00002601",
                "Rain": "Дождь \U00002614",
                "Drizzle": "Дождь \U00002614",
                "Thunderstorm": "Гроза \U000026A1",
                "Snow": "Снег \U0001F328",
                "Mist": "Туман \U0001F32B"
            }

            weather_description = data["weather"][0]["main"]

            if weather_description in emoji:
                wd = emoji[weather_description]
            else:
                wd = "X"

            tz = timezone(timedelta(seconds=time_zone))

            embed = nextcord.Embed(description=f"Погода в городе **{city}**")
            embed.add_field(name="Дата", value=f"{datetime.datetime.now(tz).strftime('%d/%m/%Y')}")
            embed.add_field(name="Время", value=f"{datetime.datetime.now(tz).strftime('%H:%M')}")
            embed.add_field(name="Погода", value=f"{wd}")
            embed.add_field(name="Температура", value=f"{temperature}°C")
            embed.add_field(name="Влажность", value=f"{humidity}%")
            embed.add_field(name="Давление", value=f"{math.ceil(pressure / 1.333)} мм.рт.ст")
            embed.add_field(name="Ветер", value=f"{wind} м/с")
            embed.add_field(name="Восход", value=f"{sunrise_timestamp}")
            embed.add_field(name="Закат", value=f"{sunset_timestamp}")

            await ctx.send(embed=embed)

        except Exception as err:
            print(err)
            await ctx.send("Указанного города не существует.")


def setup(client):
    client.add_cog(Fun(client))
