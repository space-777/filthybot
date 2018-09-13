import discord
from discord.ext import commands
from osuapi import OsuApi, ReqConnector
import requests
import os
import sys
from functions import *

TOKEN = 'NDg4NzMxMDE2NTY0MDQ3ODgz.DngeQQ.egVl3OgvvifBWBaNZeN9nR8QP1I'
apicode="92a4871f7a42d7015d58a9acf3dda2f662ba28db"
api = OsuApi(apicode, connector=ReqConnector())

client = commands.Bot(command_prefix = 'f!')

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

@client.command(pass_context=True)
async def osu(context,param):

    em=display(param)
    await client.send_message(context.message.channel, embed=em)


@client.command(pass_context=True)
async def top(context,user,amt=50):
    scores=ret50(user,val=amt)
    em=scoredisp(user,scores,amt)
    await client.send_message(context.message.channel, embed=em)


@client.command(pass_context=True)
async def set(ctx,param):
    ''' Sets a username.
    many usernames can be set to one discord iD and every time this command is
    called, number of days of filthy farmer gets reset
    '''
    try:
        user_id=api.get_user(param)[0].user_id
        discord_id=ctx.message.author.id   # Discord iD
        new_data = {
            'discord_id': discord_id,
            'days': 0,   # Days of filthy farmer left
            'total': 0  # Total days of filthy farmer earned
        }

        with open('records.json') as f:
            data = json.load(f)
        data[str(user_id)] = new_data
        with open('records.json', 'w') as f:
            json.dump(data, f, indent=2)
        tit = 'succesfully set {} IGN as {}'.format(ctx.message.author, param)
        em = discord.Embed(title= tit, colour=0xDEADBF)
        await client.say(embed=em)

    except IndexError:
        await client.say('invalid username')


client.run(TOKEN)
