from detoxify import Detoxify
import discord
from discord.ext import commands
import tomllib
import os

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.toml"), "rb") as f:
    config = tomllib.load(f)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_message(message):
    results = Detoxify("original").predict(message.content)
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)};

    is_toxic = False
    result = ""

    for dataType in results:
        value = results[dataType]

        if (value > 0.7):
            result += f"{dataType.capitalize().replace('_', ' ')}: {round(value * 100)}%\n"
            is_toxic = True
    
    if is_toxic:
        await message.delete()
        await message.channel.send(f"{message.author.mention} sent an inappropriate message. Classification feedback:\n{result}")

bot.run(config["token"])