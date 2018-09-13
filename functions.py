import discord
from discord.ext import commands
from osuapi import OsuApi, ReqConnector
import requests
import os
import sys
import datetime


api_read = open("osuapikey.txt")
apicode = api_read.readline()
api = OsuApi(apicode, connector=ReqConnector())


def display_profile(context, param):
    profile = api.get_user(param)
    Usertitle = "Osu Profile for " + profile[0].username
    thum = "https://a.ppy.sh/"+str(p	rofile[0].user_id)+"?1528809158.jpeg"
    user_url = "https://osu.ppy.sh/users/"+str(profile[0].user_id)
    embed = discord.Embed(title=Usertitle, timestamp=datetime.datetime.utcnow(),
                          url=user_url,
                          color=0xFF0418,
                          footer="Osu India bot v.NO.",
                          )
    embed.set_thumbnail(url=thum)
    embed.add_field(name="PP", value=str(profile[0].pp_raw), inline=True)
    embed.add_field(name="Rank", value='#' +
                    str(profile[0].pp_rank), inline=True)
    embed.add_field(name="Playcount", value=str(
        profile[0].playcount), inline=True)
    embed.add_field(name="Accuracy", value=str(
        profile[0].accuracy)[:6], inline=True)
    embed.add_field(name="Country", value=str(profile[0].country), inline=True)
    embed.add_field(name="Country Rank", value='#'+str(
        profile[0].pp_country_rank), inline=True)
    return embed


def scoredisp(user, scores, amt):
    tit = "Top "+str(amt)+" scores for "+user
    desc = ""
    count = 1
    for i in scores:
        bmp = api.get_beatmaps(beatmap_id=i.beatmap_id)
        desc = desc + str(count) + ".) " + bmp[0].title + "[" + \
            bmp[0].version + "]" + " -- PP : " + str(i.pp) + "\n"
        count += 1

    em = discord.Embed(title=tit, description=desc, colour=0xDEADBF)
    return em


def ret50(user, val=50):
    scores = api.get_user_best(user, limit=val)
    # print(scores)
    return scores
