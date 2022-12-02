import os
import discord
import dotenv
from dotenv import load_dotenv

bot = discord.Bot()
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

cogs_list = [
    'fun',
    'snipe',
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')
bot.run(token)
