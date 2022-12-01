import os
import discord
import random
import dotenv
from dotenv import load_dotenv
bot = discord.Bot()
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

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))


@bot.event
async def on_message_delete(message):
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


@bot.slash_command(description="ship")
async def ship(ctx, person1: str, person2: str):
    shiprandom = random.randrange(45, 100)
    await ctx.respond(f"{person1} and {person2} are a {str(shiprandom)}% match")


@bot.command()
async def clearsnip(ctx):
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


@bot.command()
async def snip(ctx):
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
    await ctx.send(embed=embed)


@bot.command()
async def ambo(ctx):
    await ctx.reply("ambotukam!!!!!!! :drooling_face: :flushed:")
    await ctx.send(
        "https://cdn.discordapp.com/attachments/798374033674338364/1022434470428680202/ambotukamzzz.png?size=4096")


@bot.slash_command(description="dice")
async def dice(ctx):
    dice1 = random.randrange(1, 6)
    dice2 = random.randrange(1, 6)
    await ctx.respond(str(dice1) + ", " + str(dice2))


@bot.slash_command()
async def amongas(ctx):
    await ctx.respond("fortnite")
bot.run(token)
