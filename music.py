import discord
from discord.ext import commands


client = commands.Bot("a!")

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


    await client.process_commands(message)


@client.command(name="PP")
async def ping(ctx,*arg):
    if ctx.guild == None:
        return
    await ctx.channel.send("Pong!"+str(len(arg)))

client.run(token)