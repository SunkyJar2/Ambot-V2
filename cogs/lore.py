import random
import discord
from discord.ext import commands


class Lore(commands.Cog):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(description="Past/Current Relationships")
    async def relationships(self, ctx):
        channel = ctx.channel
        embed = discord.Embed(
            title="Ambo's Relationships", description="(Gtw)")  # ,color=Hex code
        embed.add_field(name="Bimo", value='Status : Active')
        embed.add_field(name="Ibi",
                        value='Status : Unknown')
        embed.add_field(name="Ara",
                        value='Status : Friendzoned')

        # if you like to
        embed.set_footer(text="Welcome to Ambot 3.0")
        await ctx.respond(embed=embed)


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Lore(bot))  # add the cog to the bot
