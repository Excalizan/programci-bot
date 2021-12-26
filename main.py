from keep_alive import keep_alive
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="p/", intents=intents)

@bot.event
async def on_ready():
    print("Bot çalıştı")
    await bot.change_presence(activity=discord.Game('Programcının Botu | Excalizan#7330 | py.help'))

bot.load_extension("komutlar")
bot.load_extension("yardım")
bot.load_extension("yasa")
bot.load_extension("sosyal_medya")
bot.load_extension("moderasyon")

keep_alive()
bot.run(os.getenv('TOKEN'))