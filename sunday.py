import asyncio
import data
import discord
from discord.ext import commands

TOKEN = data.grab_parent("tokens")["bot"]
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def dove(ctx):
    # add this to a new text.json or something
    copypasta = "One day, after dinner, while my younger sister and I were lounging about in Mr. Gopher Wood's yard, we spotted a fledgling Charmony Dove all on its own. That baby bird was tiny, it didn't even have all of its feathers, and it couldn't sing. When we found it, it was already on its last breath, having fallen into a shrub — probably abandoned by its parents. We decided to build a nest for it right there and then. However, thinking back, that winter was unusually cold, with fierce winds at night in the yard, not to mention the many poisonous bugs and wild beasts in the vicinity... It was clear that if we left the fledgling in the yard, it stood no chance of surviving until spring. So, I suggested we take it inside, place it on the shelf by the window, and asked the adults to fashion a cage for it. We decided that when it regained its strength enough to spread its wings, we would release it back into the wild. The tragic part — something that we'd never considered — was that this bird's fate had already been determined long before this moment... Its destiny was determined by our momentary whim. Now, I pass the power of choice to you all. Faced with this situation, what choice would you make? Stick to the original plan, and build a nest with soft net where the Charmony Dove fell? Or build a cage for it, and feed it, giving it the utmost care from within the warmth of a home? I eagerly await your answer."
    copypasta_split = copypasta.split(" ")
    first = copypasta_split.pop(0)
    message = await ctx.send(first)
    await message.add_reaction("⬆️")
    for word in copypasta_split:
        first = first + " " + word
        message = await message.channel.fetch_message(message.id)
        if not message.reactions[0].count > 1:
            print(message.reactions)
            await message.edit(content=first)
            await asyncio.sleep(1)
        else:
            await message.edit(content=copypasta)
            return

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    return

bot.run(TOKEN)
