token = "NzI2NDg2OTU2NDQzNDM1MDg5.Xvd_yw.-VjxkBQmyh7XbR3TiUurcfuMxN4"

import discord


client = discord.Client()

@client.event
async def on_ready():
    print("Up and Running!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel == None:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

client.run(token)