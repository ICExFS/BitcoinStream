import discord
from discord.ext import tasks
import discord.ext.commands
from discord.ext import commands
import asyncio

import requests 
import json

import sys 
import os
os.system('cls')

self = True #If it's a selfbot
video_url = "The YouTube video URL here"
bot_token = "Your/The bot token"
prefix = "bitcoin?"
text = "Bitcoin Value: %valueInEURO%€" #The text, you can use %valueInEURO%, %valueInUSD% & %valueInGBP%
refresh = 60 #Everytime the bot will refresh

bot = commands.Bot(command_prefix=prefix, self_bot=self)
        

@tasks.loop(seconds=refresh)
async def bitcoin():
    r = requests.get(f'https://api.coindesk.com/v1/bpi/currentprice.json')
    js = r.json()
    value_usd = f'{js["bpi"]["USD"]["rate"].split(".")[0]}K'
    value_euro = f'{js["bpi"]["EUR"]["rate"].split(".")[0]}K'
    value_gbp = f'{js["bpi"]["GBP"]["rate"].split(".")[0]}K'
    text_r = text.replace("%valueInUSD%", value_usd).replace("%valueInEURO%", value_euro).replace("%valueInGBP%", value_gbp)
    bitcoin_stream = discord.Streaming(
        name=text_r,
        url=video_url
    )
    await bot.change_presence(activity=bitcoin_stream)
    
@bot.command()
async def exit(ctx):
    os.system('exit')
    

@bot.event 
async def on_connect():
    print('Connected') 
    bitcoin.start()    

if self is True:
    bot.run(bot_token, bot=False)
if self is False:
    bot.run(bot_token, bot=True)