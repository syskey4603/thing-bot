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
from discord import Webhook, RequestsWebhookAdapter # Importing discord.Webhook and discord.RequestsWebhookAdapter


token = "MTAwNTE1MjgwNjUzOTM2NjQxMA.GTsuPv.-Ot3Jh8wUg19y7XtXaZkgtOkbiHn0OMAeq69sE"

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix= ".", intents=intents)
stoping = False
trolling = False
trolling1 = False

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="test"))
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
    await user.message.delete()
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
    for x in range(1, 15):
        await ctx.send(random.choice(str1))
@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")


@bot.command()
async def config(ctx, args):
    if(args == "on"):
        global trolling
        trolling = True
        await ctx.send("test is on")
    elif(args == "off"):
        trolling = False
        await ctx.send("test is off")
    else:
        await ctx.send("invalid argument")

@bot.command()
async def troll(ctx, args):
    if(args == "on"):
        global trolling1
        trolling1 = True
        await ctx.send("test is on")
    elif(args == "off"):
        trolling1 = False
        await ctx.send("test is off")
    else:
        await ctx.send("invalid argument")

@bot.event
async def on_message(message):
    if(trolling == True):
        if(message.author.bot):
            return
        await message.delete()
        test = message.author
        webhook = Webhook.from_url('https://discord.com/api/webhooks/1005815714545934397/KLuiNvQDHyBwRXx9U12sD9kTuVNoXl8B8A10qMEOJIMQeyWOivEXrM8yL9UERrIZ1olt', adapter=RequestsWebhookAdapter()) # Initializing webhook
        webhook.send(username= test.name, avatar_url=test.avatar_url, content= message.content)
    
    if(trolling1 == True):
        if(message.author.bot):
            return
        test1 = message.content
        await message.edit(content=test1 + 'i hope this works')

    await bot.process_commands(message)
            
    
bot.run(token, bot=True)
