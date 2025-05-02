import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"{member.name} has joined the server!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - dont use that word or we will timeout or ban!")
            if "fuck" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - dont use that word or we will timeout or ban!")
    if "shut up" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - dont use that word or we will timeout or ban!")
    if "kurva" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - dont use that word or we will timeout or ban!")
    if "debil" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - dont use that word or we will timeout or ban!")

    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
