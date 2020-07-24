import discord
from discord.ext import commands
from util.db import getMIDforGIDEmo

client = commands.Bot("a!")

players = {}
queues = {}

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

    await client.process_commands(message)



@client.event
async def on_raw_reaction_add(pload):
    if(getMIDforGIDEmo(pload.guild_id)==str(pload.message_id)):
        print("Trued")

@client.command(name="PP",description="Ping Pong")
async def ping(ctx,*arg):
    if ctx.guild == None:
        return
    await ctx.channel.send("Pong!"+str(len(arg)))

@client.command(name="join",description="Join the Voice Channel")
async def join(ctx):
    if ctx.guild == None:
        return
    if ctx.author.voice==None or  ctx.author.voice.channel==None:
        await ctx.channel.send("Please join a voice channel before calling me!")
        return
    if ctx.guild not in players or players[ctx.guild]==None:    
        players[ctx.guild] = await ctx.author.voice.channel.connect()
        return
    else:
        await ctx.channel.send("Already Connected to "+str(players[ctx.guild].channel))
        return


@client.command(name="leave",description="Leave the Voice Channel")
async def leave(ctx):
    if ctx.guild == None:
        return
    if ctx.author.voice==None or  ctx.author.voice.channel==None:
        await ctx.channel.send("Please join a voice channel before commanding me to leave!")
        return
    if ctx.guild not in players or players[ctx.guild]==None:
        await ctx.channel.send("I'm not connected, so, cannot leave.")
        return
    if players[ctx.guild].channel == ctx.author.voice.channel:
        await players[ctx.guild].disconnect()
        players.pop(ctx.guild)
        await ctx.channel.send("Left the channel, remember me soon!")
        return


client.run(token)