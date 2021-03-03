import discord
from discord.ext import tasks
import discord.ext.commands
from discord.ext.commands import bot
from discord import Game
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import errors
import discord.utils
from discord.utils import find, get
import asyncio
import aiohttp

import requests 
import json

import sys 
import os
os.system('cls')

self = True
video_url = "https://www.youtube.com/watch?v=bKtFYnrDXFk"
bot_token = "mfa.zEWnU8MWjywHdmlxNqFVj9iNA-0gO8JAu5RtpRkAq9eODL0gCHzkWaeVTYP5xgUeAZ3aEhWQf97ZIYxZN3EK"
prefix = "bitcoin?"
text = "Bitcoin Value: %valueInEURO%€"
refrsh = 60

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