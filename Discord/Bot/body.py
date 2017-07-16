# -*- coding: utf-8 -*-

import discord, asyncio, re, codecs, requests, json, threading, os, sys, locale
from time import strftime, time, localtime, gmtime

# Local Script Inclusion
import kkutu
from settings import settings

timestr = strftime("-%Y%m%d")
client = discord.Client()
nowdir = os.getcwd()

# Token here
token = "MzE4MTg4NTgxMzYzMzg0MzMx.DAuw5g.546jvNdwYiLCVLGnO9P0-zCAv2Q"

# Bot ready
@client.event
async def on_ready():
    print(" Started Daemon | ", end='')
    print(client.user.name, end=' | ')
    print(client.user.id)
    print(" ===========")
    await client.change_presence(game=discord.Game(name="문의는 이은학#9299"))

os.chdir("./logs")

# Bot event trigger
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    with codecs.open("%s-%s(#%s)-%s.log"%(message.server.name, message.channel.name,message.channel.id,strftime("%Y%m%d")), "a", encoding="UTF-8") as f:
        f.write(strftime("%Y.%m.%d %H:%M:%S")+ "─"+ str(message.server.id)+ "─"+ str(message.channel.id)+ "─"+ str(message.author)+ "─"+message.content+"\n")
    print(".",end="")

client.run(token)