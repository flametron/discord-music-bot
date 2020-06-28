import discord
from discord.ext import commands


client = commands.Bot("!")

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


@client.command(pass_context=True)
async def ping(ctx):
    if ctx.guild == None:
        return
    await ctx.channel.send("{}".format(ctx))

client.run(token)