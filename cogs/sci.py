import random
import discord
from scipy import constants
from discord.ext import commands
from random import choice


class Sci(commands.Cog):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(description="Liter to Cubic Meters")
    async def litermeter(self, ctx, liter: float):
        await ctx.respond(constants.liter * liter)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Sci(bot)) # add the cog to the bot
