import discord
from discord.ext import commands
from osuapi import OsuApi, AHConnector
import aiohttp
import asyncio


TOKEN = 'NDg4NzMxMDE2NTY0MDQ3ODgz.DngeQQ.egVl3OgvvifBWBaNZeN9nR8QP1I'


client = commands.Bot(command_prefix = '!f')



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
    

client.run(TOKEN)
