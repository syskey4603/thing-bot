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
    guild = ctx.guild
    while stoping == False:
        await guild.create_text_channel("abhijosh kinda qt")

@bot.event
async def on_guild_channel_create(channel):
    global stoping
    if(channel.name != ("test")):
        while stoping == False:
            await channel.send("@everyone")


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
    await ctx.send("https://cdn.discordapp.com/attachments/931452152059154462/1005396614850023434/Screenshot_2022-08-06_at_2.17.00_PM.png")
    await ctx.send ("hottie abhijay about to rape us")

    
bot.run(token, bot=True)
