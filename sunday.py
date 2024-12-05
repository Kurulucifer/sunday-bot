import asyncio
import data
import discord
from discord.ext import commands

TOKEN = data.grab_json("tokens")["bot"]
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def dove(ctx):
    with open("data/charmony_dove.txt", "r") as charmony:
        copypasta = charmony.read()
    message = await ctx.send(copypasta)
    await message.add_reaction("🕊")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    return

bot.run(TOKEN)
