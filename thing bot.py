import discord
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import requests
from discord.ext import commands
import time
import random
import string
import pyjokes


token = "MTAwNTE1MjgwNjUzOTM2NjQxMA.GTsuPv.-Ot3Jh8wUg19y7XtXaZkgtOkbiHn0OMAeq69sE"

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix= ".", intents=intents)
stoping = False

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="abhijosh kinda qt"))
    print(Fore.GREEN + f"{bot.user.name} has logged in successfully." + Fore.RESET)


@bot.command()
async def startping(ctx):
    await ctx.send("Hello @everyone This your daily dose of abhijosh")
    guild = ctx.guild
    while stoping == False:
        await guild.create_text_channel("abhijosh kinda qt")

@bot.event
async def on_guild_channel_create(channel):
    global stoping
    if(channel.name != ("test")):
        while stoping == False:
            await channel.send("@everyone https://cdn.discordapp.com/attachments/931452152059154462/1005396614850023434/Screenshot_2022-08-06_at_2.17.00_PM.png")


@bot.command()
async def stop(ctx):
    global stoping
    await ctx.send("stopping")
    stoping = True
    

@bot.command()
async def reset(ctx):
    global stoping
    guild = ctx.guild
    for channel in guild.channels:
        if(channel.name != ("test")):
            try:
                await channel.delete()
                print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
            except:
                print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)



@bot.command()
async def whywontitwork(ctx):
    guild = ctx.guild
    for member in guild.members:
        print(random.choice(member))


@bot.command()
async def abhijosh(ctx):
    abhijosh = ["https://cdn.discordapp.com/attachments/931452152059154462/1005396614850023434/Screenshot_2022-08-06_at_2.17.00_PM.png", "https://cdn.discordapp.com/attachments/1005405725964644424/1005406002323148800/Screenshot_2022-08-04_at_8.45.43_AM.png", "https://cdn.discordapp.com/attachments/1005405725964644424/1005405973160149002/unknown.png","https://cdn.discordapp.com/attachments/1005405725964644424/1005405931472965712/Screenshot_2022-08-06_at_2.52.24_PM.png" ]
    await ctx.send("abhijosh found")
    await ctx.send(random.choice(abhijosh))
    
@bot.command()
async def youropinion(ctx):
   await ctx.message.delete()
   youropinion = ["didnt ask", "you gave the opinion", "while u gave the opinion i was doing your mom", "dont care", "ratio"]
   await ctx.send("reason why your opinion doesnt matter")
   await ctx.send(random.choice(youropinion))
    
@bot.command()
async def dm(user: discord.User, message):
    await user.send(message)



@bot.command(pass_context=True, aliases=['purge', 'clear'])
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit+1)
        await ctx.message.delete()

@bot.command()
async def cubescramble(ctx):
    await ctx.send("imagine not even sub 20 pb")
    str1 = ["U", "D", "R", "L", "F", "B", "U2", "D2", "R2", "L2", "F2", "B2", "M", "M2"]
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
    await ctx.send(random.choice(str1))
@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

    
bot.run(token, bot=True)
