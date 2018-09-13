import os
import sys
import Location
import discord
from discord.ext import commands

import requests
from functions import *
from osuapi import OsuApi, ReqConnector

api_read = open("osuapikey.txt")
Token_read = open("Token.txt")

TOKEN = Token_read.readline()
apicode = api_read.readline()


client = commands.Bot(command_prefix='!f')


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


@client.event
async def on_ready():
    ready_message = "Logged in as" + client.user.name + "\n ID:" + client.user.id
    print(ready_message)


@client.command()
async def ping():
    await client.say('pong')


@client.command()
async def sd():
    await client.logout()


@client.command()
async def restart():
    restart_program()
    await client.close()


@client.command(pass_context=True)
async def osu(context, *param):
    if len(param) == 0:
        await client.say("**Provide a Username(s)**")
    elif len(param) == 1:
        embed = display_profile(context, param)
        await client.send_message(context.message.channel, embed=embed)
    else:
        for var in param:
            embed = display_profile(context, var)
            await client.send_message(context.message.channel, embed=embed)


@client.command(pass_context=True)
async def top(context, user, amt=50):
    scores = ret50(user, val=amt)
    em = scoredisp(user, scores, amt)
    await client.send_message(context.message.channel, embed=em)

client.run(TOKEN)
