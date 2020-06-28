import discord

client = discord.Client()

with open(".token") as file:
    token=file.read()

@client.event
async def on_ready():
    print("Up and Running!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.guild == False:
        return

    if message.content=="checkchannel":
        await message.channel.send('{.channel}'.format(message))

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

client.run(token)