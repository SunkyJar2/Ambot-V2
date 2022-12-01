import discord
from discord.ext import commands
snipe_message_content = {}
snipe_message_content2 = {}
snipe_message_content3 = {}
snipe_message_content4 = {}
snipe_message_content5 = {}
snipe_message_author = {}
snipe_message_author2 = {}
snipe_message_author3 = {}
snipe_message_author4 = {}
snipe_message_author5 = {}


class Snipe(commands.Cog):  # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot):  # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot and len(message.content) > 2:
            print(len(snipe_message_author))
            if len(snipe_message_content) == 0:
                channel = message.channel
                snipe_message_author[message.channel.id] = message.author.display_name
                snipe_message_content[message.channel.id] = message.content
                print(snipe_message_content, snipe_message_author)
            elif len(snipe_message_content2) == 0:
                channel2 = message.channel
                snipe_message_author2[message.channel.id] = message.author.display_name
                snipe_message_content2[message.channel.id] = message.content
                print(snipe_message_content2, snipe_message_author2)
            elif len(snipe_message_content3) == 0:
                channel2 = message.channel
                snipe_message_author3[message.channel.id] = message.author.display_name
                snipe_message_content3[message.channel.id] = message.content
                print(snipe_message_content3, snipe_message_author3)
            elif len(snipe_message_content4) == 0:
                channel2 = message.channel
                snipe_message_author4[message.channel.id] = message.author.display_name
                snipe_message_content4[message.channel.id] = message.content
                print(snipe_message_content4, snipe_message_author4)
            elif len(snipe_message_content5) == 0:
                channel2 = message.channel
                snipe_message_author5[message.channel.id] = message.author.display_name
                snipe_message_content5[message.channel.id] = message.content
                print(snipe_message_content5, snipe_message_author5)
            else:
                snipe_message_author5.update(snipe_message_author4)
                snipe_message_author4.update(snipe_message_author3)
                snipe_message_author3.update(snipe_message_author2)
                snipe_message_author2.update(snipe_message_author)
                snipe_message_author.clear()
            if not message.author.bot and len(message.content) > 2:
                print(len(snipe_message_author), "Method B")
                if len(snipe_message_content) == 0:
                    channel = message.channel
                    snipe_message_author[message.channel.id] = message.author
                    snipe_message_content[message.channel.id] = message.content
                    print(snipe_message_content)
                elif len(snipe_message_content2) == 0:
                    channel2 = message.channel
                    snipe_message_author2[message.channel.id] = message.author
                    snipe_message_content2[message.channel.id] = message.content
                    print("snipe 2" + str(snipe_message_content2))
                elif len(snipe_message_content3) == 0:
                    channel2 = message.channel
                    snipe_message_author3[message.channel.id] = message.author
                    snipe_message_content3[message.channel.id] = message.content
                    print(snipe_message_content3)
                elif len(snipe_message_content4) == 0:
                    channel2 = message.channel
                    snipe_message_author4[message.channel.id] = message.author
                    snipe_message_content4[message.channel.id] = message.content
                    print(snipe_message_content4)
                elif len(snipe_message_content4) == 0:
                    channel2 = message.channel
                    snipe_message_author5[message.channel.id] = message.author
                    snipe_message_content5[message.channel.id] = message.content
                    print(snipe_message_content5)

    @discord.slash_command()
    async def clearsnip(self, ctx):
        if len(snipe_message_content5) != 0:
            snipe_message_author5.clear()
            snipe_message_author4.clear()
            snipe_message_author3.clear()
            snipe_message_author2.clear()
            snipe_message_author.clear()
            snipe_message_content5.clear()
            snipe_message_content4.clear()
            snipe_message_content3.clear()
            snipe_message_content2.clear()
            snipe_message_content.clear()
            await ctx.reply("https://cdn.discordapp.com/emojis/1004203844479242271.png?size=4096&quality=lossless")

    @discord.slash_command()
    async def snip(self, ctx):
        channel = ctx.channel
        embed = discord.Embed(
            title="Snipes", description="(Gtw)")  # ,color=Hex code
        embed.add_field(name=str(snipe_message_author),
                        value=str(snipe_message_content))
        embed.add_field(name=str(snipe_message_author2),
                        value=str(snipe_message_content2))
        embed.add_field(name=str(snipe_message_author3),
                        value=str(snipe_message_content3))
        embed.add_field(name=str(snipe_message_author4),
                        value=str(snipe_message_content4))
        embed.add_field(name=str(snipe_message_author5),
                        value=str(snipe_message_content5))
        # if you like to
        embed.set_footer(text="(this version of the bot is a preview/beta)")
        await ctx.reply(embed=embed)


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Snipe(bot))  # add the cog to the bot
