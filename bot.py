import os
import sys
import Location
import discord
from discord.ext import commands
from osuapi import OsuApi, ReqConnector
import requests


TOKEN = 'NDg5NDU2MTc5MjQ5MDIwOTU5.DntehQ.IlU8WNcpOpO89bYTRnKhPGPsIM0'
apicode = "92a4871f7a42d7015d58a9acf3dda2f662ba28db"
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
    ready_message = "Logged in as" + client.user.name + "\n ID:" +  client.user.id
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
    profile = api.get_user(param)  # fails if more than 1 param.
    tit = "Osu Profile for "+param
    desc = "Username: "+profile[0].username+"\n"+"PP: "+str(profile[0].pp_raw)+"\n"+"Rank: "+str(profile[0].pp_rank)+"\n"+"Playcount: "+str(profile[0].playcount)
    em = discord.Embed(title=tit, description=desc, colour=0xDEADBF)
    await client.send_message(context.message.channel, embed=em)


client.run(TOKEN)
