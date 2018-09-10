import discord

TOKEN = "NDg4NzMxMDE2NTY0MDQ3ODgz.DngeQQ.egVl3OgvvifBWBaNZeN9nR8QP1I"

client = discord.Client()

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content.startswith('!heck'):
		msg = 'Heck Off {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)