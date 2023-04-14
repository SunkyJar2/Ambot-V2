import os
import discord
import dotenv
from dotenv import load_dotenv
import random
from random import choice

class MyView(discord.ui.View):  # Create a class called MyView that subclasses discord.ui.View
    # Create a button with the label "😎 Click me!" with color Blurple
    @discord.ui.button(label="Smash", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        await interaction.response.send_message(f"{interaction.user} Chose Smash")


bot = discord.Bot(intents=discord.Intents.all())
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

cogs_list = [
    'fun',
    'snipe',
    'lore',
    'sci'
]
bot.slash_command(description='help')


async def help(ctx):
    ctx.respond('yout msther')
bot.slash_command(description='help')


async def help(ctx):
    ctx.respond('yout msther')


@bot.slash_command()  # Create a slash command
async def sop(ctx):
    user = random.choice(ctx.guild.members)
    print(user)
    await ctx.respond(f'Smash or Pass: {user.name}', view=MyView())

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')


bot.run(token)
