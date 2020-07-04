import os
import random
import discord
import string

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

    def staff(mod):
        mod_read = open(f"{mod}.txt", "r")
        text = mod_read.read()
        words = str(text.split())
        final = words.replace(target, "")
        seembled = " ".join(final)
        print(seembled)
        mod_read.close()
        mod_write = open(f"{mod}.txt", "w")
        mod_write.writelines(final)
        mod_write.close()

    if message.content.lower() == ".help":
        if message.author.name in admins:
            await message.channel.send('''``` 
Este bot basicamente serve as pessoas sem cargos de administrador nao conseguirem 
colocar links para outros discords. Ao primeiro  link de invite que alguem (sem cargos) meter 
em qualquer chat-textrecebe um "warn", que podem verificar usando o comando <.warn list>, 
so pessoas com cargos têm acesso a estes comandos. E tambem podes remover warn se achares 
que a pessoa merece ou foi um bug(Coisa que nao vai acontecer pois je programar muito bem).
Se o mesmo voltar a por um invite é automaticamente kickado e é colocado numa lista 
que tambem podem acessar com o comando <.kicker list>, e se voltar ao servidor e voltar a 
por um link vai ser automaticamente banido(é claro que todos os invites sao automaticamente 
apagados no mesmo instante que é publicado). Em baixo tem os comandos e como os deves executar :)
\n
\n
------------------------------Comandos------------------------------
.kicker list --> mostra todas as pessoas que estao na lista kicker (Depois de pustar 2 invites)
.unkicker <NAME_LIST> --> retira alguem da lista Kicker
.warn list --> mesma coisa que o kicker list (Depois de pustar 1 invite)
.unwarn <USER_LIST> --> remove uma pessoa da warn list
--------------------------------------------------------------------```''')
        else:
            await message.channel.send("""```
Este bot é destinado aos moderadores do servidor, so tens que saber que nao podes pustar qualquer tipo de link que é destinado a publicitar outro servidor, só mesmo com a permissão de um administrador ou Boss(Ou de mim claro //Fury^^). Continuação de um bom dia e stay safe :)```""")

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
                    print(
                        f"{message.author} Levou ban pois ja levou kick uma vez e voltou a publicar um invite")
                    await member_invite.ban(reason="Levou kick e voltou a publicar um invite")

                else:
                    print(
                        f"Detectou na lista o nome {message.author.name} e foi kickado")
                    kicked_write = open("kicked.txt", "a")
                    kicked_write.write(f"\n{message.author.name}")
                    kicked_write.close()
                    await member_invite.kick(reason="Publicou um invite")

            else:
                warn_read.close()
                print(
                    f"Nao foi detectado na lista o nome {message.author.name}")
                warn_write = open("warn.txt", "a")
                warn_write.write(f"\n{message.author.name}")
                warn_write.close()
                await message.channel.send(f"{message.author.mention} Se voltares a postar um invite seras kickado.")

    if message.content == ".warn list":
        if message.author.name in admins:
            warn_read = open("warn.txt", "r")
            await message.channel.send(warn_read.read())
            warn_read.close()

        else:
            await message.channel.send(f"{message.author.mention} Não tens premissões para esse comando.")

    if message.content == ".kicked list":
        if message.author.name in admins:
            kicked_read = open("kicked.txt", "r")
            await message.channel.send(kicked_read.read())
            kicked_read.close()

        else:
            await message.channel.send(f"{message.author.mention} Não tens premissões para esse comando.")

    for i in range(0, 300):
        user = random.choice(message.channel.guild.members)
        target = user.name

        try:
            if message.content == ".unkicked {}".format(target):

                if message.author.name in admins:
                    staff(mod="kicked")
                    break

                else:
                    await message.channel.send(f"{message.author.mention} Não tens premissões para esse comando.")
                    break

            if message.content == ".unwarn {}".format(target):

                if message.author.name in admins:        	
                    staff(mod="warn")
                    break

                else:
                    await message.channel.send(f"{message.author.mention} Não tens premissões para esse comando.")
                    break

        except EnvironmentError:
            print("Algo correu mal")

client.run(token)
