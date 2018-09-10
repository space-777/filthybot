import discord
from discord.ext import commands
from osuapi import OsuApi, AHConnector
import aiohttp
import asyncio
import os
import sys


TOKEN = 'NDg4NzMxMDE2NTY0MDQ3ODgz.DngeQQ.egVl3OgvvifBWBaNZeN9nR8QP1I'


client = commands.Bot(command_prefix = '!f')

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def ping():
    await client.say('pong')
    
@client.command()
async def shutdown():
    await client.close()
    
@client.command()
async def restart():
    restart_program()
    await client.close()
    

client.run(TOKEN)
