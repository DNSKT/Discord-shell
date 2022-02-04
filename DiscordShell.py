#i have no idea if this will work tho
# i hope so



import os
import pprint
import sys
import time
from discord import message
#from Shell_Engine import *
from discord.ext import commands
import discord
import base64
import ctypes
import getpass
import os
import platform
import re
import socket
import subprocess
import urllib.request
import sys


bot = discord.Client()

token = 'OTM4OTY1NTg3MTEwMDE0OTk2.Yfx92Q.iOmWP7WZ_zvaw5naTsOwN6MP1Vc'

description = '''Discord bot built in discord.py and made by Skultz.#2059'''

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Inside the shell"))
    print("-----------------------------------------------")
    print("[!] Starting seccion: ", bot.user.name)
    print("[!] ID: ", bot.user.id)
    print("-----------------------------------------------")

#te odio tesseract

def whoami():
    return getpass.getuser()

@bot.command()
async def whoami(ctx):
    """eeee"""
    await ctx.send(whoami())


bot.run(token)