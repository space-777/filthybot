import discord
from discord.ext import commands
from osuapi import OsuApi, ReqConnector
import requests
import os
import sys

apicode="92a4871f7a42d7015d58a9acf3dda2f662ba28db"
api = OsuApi(apicode, connector=ReqConnector())



def display(param):
	profile=api.get_user(param)
	print(profile)
	tit="Osu Profile for "+param
	desc="Username: "+profile[0].username+"\n"+"PP: "+str(profile[0].pp_raw)+"\n"+"Rank: "+str(profile[0].pp_rank)+"\n"+"Playcount: "+str(profile[0].playcount)
	em = discord.Embed(title= tit, description=desc, colour=0xDEADBF)
	return em
	
def scoredisp(user,scores,amt):
	tit = "Top "+str(amt)+" scores for "+user
	desc=""
	count = 1
	for i in scores:
		bmp = api.get_beatmaps(beatmap_id=i.beatmap_id)
		desc = desc + str(count) + ".) " + bmp[0].title + "[" + bmp[0].version + "] " + str(i.enabled_mods) + " -- PP : " + str(i.pp) +  " Played on " + str(i.date) + "\n"   
		count+=1

	em = discord.Embed(title= tit, description=desc, colour=0xDEADBF)
	return em

def recentdisp(user,scores,amt):
	tit = "Recent "+str(amt)+" scores for "+user
	desc=""
	count = 1
	for i in scores:
		bmp = api.get_beatmaps(beatmap_id=i.beatmap_id)
		desc = desc + str(count) + ".) " + bmp[0].title + "[" + bmp[0].version + "] " + str(i.enabled_mods) + " Played on " + str(i.date) + "\n" 
		count+=1

	em = discord.Embed(title= tit, description=desc, colour=0xDEADBF)
	return em

