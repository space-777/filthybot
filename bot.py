import os
import sys

import discord
from discord.ext import commands

import requests
from functions import *
from osuapi import OsuApi, ReqConnector

Token_read = open("Token.txt")
api_read = open("osuapikey.txt")


TOKEN = Token_read.readline()
apicode = api_read.readline()

api = OsuApi(apicode, connector=ReqConnector())

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
async def shutdown():
    await client.logout()


@client.command()
async def restart():
    restart_program()
    await client.close()


@client.command(pass_context=True)
async def osu(context, param):

    em = display(param)
    await client.send_message(context.message.channel, embed=em)


@client.command(pass_context=True)
async def top(context, user, amt=50):
    scores = ret50(user, val=amt)
    em = scoredisp(user, scores, amt)
    await client.send_message(context.message.channel, embed=em)

client.run(TOKEN)
