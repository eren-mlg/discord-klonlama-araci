mytitle = "Sunucu Kopyalama Aracı"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = 'Your Account ID'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
from colorama import Fore, Style, init
import time
init(autoreset=True)
ascii_art = '''


 /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$  /$$   /$$ /$$$$$$$  /$$$$$$$$ /$$     /$$ /$$$$$$    /$$  
| $$  /$$/ /$$__  $$| $$__  $$|__  $$__//$$__  $$| $$$ | $$| $$__  $$| $$_____/|  $$   /$$//$$$_  $$ /$$$$  
| $$ /$$/ | $$  \ $$| $$  \ $$   | $$  | $$  \ $$| $$$$| $$| $$  \ $$| $$       \  $$ /$$/| $$$$\ $$|_  $$  
| $$$$$/  | $$$$$$$$| $$$$$$$/   | $$  | $$$$$$$$| $$ $$ $$| $$$$$$$ | $$$$$     \  $$$$/ | $$ $$ $$  | $$  
| $$  $$  | $$__  $$| $$____/    | $$  | $$__  $$| $$  $$$$| $$__  $$| $$__/      \  $$/  | $$\ $$$$  | $$  
| $$\  $$ | $$  | $$| $$         | $$  | $$  | $$| $$\  $$$| $$  \ $$| $$          | $$   | $$ \ $$$  | $$  
| $$ \  $$| $$  | $$| $$         | $$  | $$  | $$| $$ \  $$| $$$$$$$/| $$$$$$$$    | $$   |  $$$$$$/ /$$$$$$
|__/  \__/|__/  |__/|__/         |__/  |__/  |__/|__/  \__/|_______/ |________/    |__/    \______/ |______/
                                                                                                            
                                                                                                            
                                                                                                            
'''
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
for i, line in enumerate(ascii_art.split('\n')):
    print(colors[i % len(colors)] + line)
    time.sleep(0.1)
token = input(f'Tokeninizi Giriniz:\n >')
guild_s = input('Kopyalanacak  Sunucu ID:\n >')
guild = input('Aktarılıcak Sunucu ID:\n >')
input_guild_id = guild_s
output_guild_id = guild
token = token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Hesabına Giriş Başarılı : {client.user}")
    print("Aktarımı Başlatıyorum")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}
          Aktarım Bitti
    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()

client.run(token, bot=False)
