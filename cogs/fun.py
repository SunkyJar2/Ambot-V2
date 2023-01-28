import random
import discord
from discord.ext import commands
from random import choice


class Fun(commands.Cog):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(description="ship")
    async def ship(self, ctx, person1: str, person2: str):
        shiprandom = random.randrange(45, 100)
        await ctx.respond(f"{person1} and {person2} are a {str(shiprandom)}% match")

    @discord.slash_command(description="dice")
    async def dice(self, ctx):
        dice1 = random.randrange(1, 6)
        dice2 = random.randrange(1, 6)
        await ctx.respond(str(dice1) + ", " + str(dice2))

    @discord.slash_command()
    async def ambo(self, ctx):
        await ctx.respond("ambotukam!!!!!!! :drooling_face: :flushed:")
        await ctx.send(
            "https://cdn.discordapp.com/attachments/798374033674338364/1022434470428680202/ambotukamzzz.png?size=4096")


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Fun(bot))  # add the cog to the bot
