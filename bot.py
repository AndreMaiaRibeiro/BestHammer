import os
import random
import discord

token_txt = open('token.txt', 'r')
token = token_txt.read()

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

admins = [
"BestHammer",
"Fury^^",
".Fastio",
"Bifão",
"Ricardo21",
"nocasxd",
"Saldanha",
"martimm",
"Badum Badero",
"zara",
"ernestu",
"GATONÁCIO",
]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(""))
    print(f'{client.user.name} is online')

@client.event
async def on_message(message):
	if "https://discord.gg/" in message.content or "discord.gg/" in message.content:
		member_invite = message.author
		print(f"{message.author} postou um invite")

		if message.author.name in admins:
			await message.channel.send(f"{message.author.mention} Tu podes :laughing:")

		else:
			await message.channel.purge(limit=1)
			warn_read = open("warn.txt", "r")

			if message.author.name in warn_read.read():
				warn_read.close()
				kicked_read = open("kicked.txt", "r")
				if message.author.name in kicked_read.read():
					kicked_read.close()
					print(f"{message.author} Levou ban pois ja levou kick uma vez e voltou a publicar um invite")
					await member_invite.ban(reason="Levou kick e voltou a publicar um invite")

				else:
					print(f"Detectou na lista o nome {message.author.name} e foi kickado")
					kicked_write = open("kicked.txt", "a")
					kicked_write.write(f"\n{message.author.name}")
					kicked_write.close()
					await member_invite.kick(reason="Publicou um invite")

			else:
				warn_read.close()
				print(f"Nao foi detectado na lista o nome {message.author.name}")
				warn_write = open("warn.txt", "a")
				warn_write.write(f"\n{message.author.name}")
				warn_write.close()
				await message.channel.send(f"{message.author.mention} Se voltares a postar um invite seras kickado.")

client.run(token)
