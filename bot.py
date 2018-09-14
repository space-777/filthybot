import os
import sys
import discord
from discord.ext import commands

import requests
from functions import *

from osuapi import OsuApi, ReqConnector

Token_read = open("token.txt")
api_read = open("osuapikey.txt")


TOKEN = Token_read.readline().strip()
apicode = api_read.readline().strip()

import json


api = OsuApi(apicode, connector=ReqConnector())

client = commands.Bot(command_prefix='f!')


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


@client.event
async def on_ready():
    ready_message = "Logged in as " + client.user.name + "\n ID:" + client.user.id
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


@client.command(pass_context=True) #Completed with Rich embed. Todo: Add Local Search -- Arulson will take care of that.
async def osu(context, *param):
    if len(param) == 0:
        #await client.say("**Provide a Username(s)**")
        with open('records.json') as f:
            data = json.load(f)
        id = data[context.message.author.id]["user_id"]
        embed = display_profile(id)
        await client.send_message(context.message.channel, embed=embed)
    elif len(param) == 1:
        embed = display_profile(param)
        await client.send_message(context.message.channel, embed=embed)
    else:
        for var in param:
            embed = display_profile(var)
            await client.send_message(context.message.channel, embed=embed)

@client.command(pass_context=True)
async def top(context, *params):
    #Default user AND default amount
    if len(params) == 0:
        with open('records.json') as f:
            data = json.load(f)
        user = api.get_user(data[context.message.author.id]["user_id"])[0].username
        amt=5
    #Only default amount
    elif len(params) == 1:
        user = params[0]
        amt=5
    #No defaults
    else:
        user = params[0]
        amt = params[1]
    embed = Top_Scores(user, amt)
    await client.send_message(context.message.channel, embed=embed)


@client.command(pass_context=True) #Completed With Rich Embed.
async def recent(context, *params):
    #Default user AND default amount
    if len(params) == 0:
        with open('records.json') as f:
            data = json.load(f)
        user = api.get_user(data[context.message.author.id]["user_id"])[0].username
        amt=5
    #Only default amount
    elif len(params) == 1:
        user = params[0]
        amt=5
    #No defaults
    else:
        user = params[0]
        amt = params[1]
    embed = recent_Scores(user, amt)
    await client.send_message(context.message.channel, embed=embed)


@client.command(pass_context=True)
async def set(ctx, param):
    ''' Sets a username.
    many usernames can be set to one discord iD and every time this command is
    called, number of days of filthy farmer gets reset
    '''
    try:
        user_id = api.get_user(param)[0].user_id
        discord_id = ctx.message.author.id   # Discord iD
        new_data = {
            'user_id': user_id,
            'days': 0,   # Days of filthy farmer left
            'total': 0  # Total days of filthy farmer earned
        }

        with open('records.json') as f:
            data = json.load(f)
        data[str(discord_id)] = new_data
        with open('records.json', 'w') as f:
            json.dump(data, f, indent=2)
        tit = 'succesfully set {} IGN as {}'.format(ctx.message.author, param)
        em = discord.Embed(title=tit, colour=0xDEADBF)
        await client.say(embed=em)

    except IndexError:
        await client.say('invalid username')


@client.command(pass_context = True)
async def compare(ctx, user1, user2):
	em = check(user1, user2)
	await client.send_message(ctx.message.channel, embed=em)
	
@client.command(pass_context = True)
async def topr(context, *params):
    #Default user AND default amount
    if len(params) == 0:
        with open('records.json') as f:
            data = json.load(f)
        user = api.get_user(data[context.message.author.id]["user_id"])[0].username
        amt= 5
    #Only default amount
    elif len(params) == 1:
        user = params[0]
        amt= 5
    #No defaults
    else:
        user = params[0]
        amt = int(params[1])
    em=recent_top(user, amt)
    await client.send_message(context.message.channel, embed=em)




client.run(TOKEN)
