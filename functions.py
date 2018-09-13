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


def display_profile(param):
        # Obtaining Profile from Paramerter.
    profile = api.get_user(param)

    # Local Stuff
    Usertitle = "Osu Profile for " + profile[0].username
    thum = "https://a.ppy.sh/"+str(profile[0].user_id)+"?1528809158.jpeg"
    user_url = "https://osu.ppy.sh/users/"+str(profile[0].user_id)

    # Embed Creation.
    embed = discord.Embed(title=Usertitle, timestamp=datetime.datetime.utcnow(),
                          url=user_url,
                          color=0xFF0418,
                          footer="Osu India bot v.1.0"
                          )

    # thumbnails
    embed.set_thumbnail(url=thum)
    # PP
    embed.add_field(name="PP", value=str(profile[0].pp_raw), inline=True)
    # Rank
    embed.add_field(name="Rank", value='#' +
                    str(profile[0].pp_rank), inline=True)
    # Playcount
    embed.add_field(name="Playcount", value=str(
        profile[0].playcount), inline=True)
    # Accuracy
    embed.add_field(name="Accuracy", value=str(
        profile[0].accuracy)[:6], inline=True)
    # Country Indentification.
    embed.add_field(name="Country", value=str(profile[0].country), inline=True)
    # Country Rank.
    embed.add_field(name="Country Rank", value='#'+str(
        profile[0].pp_country_rank), inline=True)
    return embed


def Top_Scores(context, user, amt):
	#Api Call
    Scores = api.get_user_best(user, limit=amt)
	#Local Stuff.
    Usertitle = "Top {} Scores for {}".format(amt, user)
    count = 1
	#Embed
    embed = discord.Embed(title=Usertitle, timestamp=datetime.datetime.utcnow(),
                          color=0xFF0418,
                          footer="Osu India bot v.1.0"
                          )
	#Feilds.
    for var in Scores:
        beatmap = api.get_beatmaps(beatmap_id=var.beatmap_id)
        Title = "{}. {}[{}] +**{}**".format(count, beatmap[0].title,
                                       beatmap[0].version, var.enabled_mods)
        Value = "PP:{}\n Played on:{}".format(var.pp, var.date)
        embed.add_field(name=Title, value=Value, inline=False)
        count += 1
    return embed


def recent_Scores(param, amt):
    scores = api.get_user_recent(param, limit=amt)
    Usertitle = "Recent {} scores for {}".format(amt, param)
    count = 1
    # Discord Embed Creation.
    embed = discord.Embed(title=Usertitle, timestamp=datetime.datetime.utcnow(),
                          color=0xFF0418,
                          footer="Osu India bot v.1.0"
                          )
    # Looping over All Scores and adding feilds.
    for var in scores:
        beatmap = api.get_beatmaps(beatmap_id=var.beatmap_id)
        Title = "{}. {}[{}] +**{}**".format(count, beatmap[0].title,
                                           beatmap[0].version, var.enabled_mods)

        Time_del = var.date
        Value = "*Played on*: {}\n SR: {}".format(
            Time_del, str(beatmap[0].difficultyrating)[:5])
        embed.add_field(name=Title, value=Value, inline=False)
        count += 1
    return embed
