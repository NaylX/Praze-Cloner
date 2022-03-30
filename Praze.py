mytitle = "Praze - Developed by !Nayl#0001"
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
print(f"""{Fore.RED}
                         d8888b. d8888b.  .d8b.  d88888D d88888b 
                         88  `8D 88  `8D d8' `8b YP  d8' 88'     
                         88oodD' 88oobY' 88ooo88    d8'  88ooooo 
                         88~~~   88`8b   88~~~88   d8'   88~~~~~ 
                         88      88 `88. 88   88  d8' db 88.     
                         88      88   YD YP   YP d88888P Y88888P 
                                        
                                        
{Style.RESET_ALL}
                              {Fore.RED}Developed by: !"Nayl#0001.{Style.RESET_ALL}
        """)
token = input(f'Entre le token:\n >')
guild_s = input('Mais lidentifiant du serveur que tu veux copier:\n >')
guild = input('Mais lidentifiant du serveur que tu veux coller:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Connecté sur le compte : {client.user}")
    print("Clone le serveur...")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}
                               ::::::::  :::        ::::::::  ::::    ::: :::::::::: :::::::::  
                               :+:    :+: :+:       :+:    :+: :+:+:   :+: :+:        :+:    :+: 
                               +:+        +:+       +:+    +:+ :+:+:+  +:+ +:+        +:+    +:+ 
                               +#+        +#+       +#+    +:+ +#+ +:+ +#+ +#++:++#   +#+    +:+ 
                               +#+        +#+       +#+    +#+ +#+  +#+#+# +#+        +#+    +#+ 
                               #+#    #+# #+#       #+#    #+# #+#   #+#+# #+#        #+#    #+# 
                               ########  ########## ########  ###    #### ########## #########  
{Style.RESET_ALL}""")

client.run(token, bot=False)
