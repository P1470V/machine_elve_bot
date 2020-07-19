import discord
from discord.ext import commands

bot_token = input("Bot Token: ") #Discord Bot Token

client = commands.Bot(command_prefix="<") #Decides which command prefix to use
client.remove_command('help') #removes default help command

#Bot says that it's ready when it starts up
@client.event
async def on_ready():
    print("Bot is ready")

#First Command, pretty self explanatory
@client.command()
async def hello(ctx):
    await ctx.send("Go Fuck yourself")

#Help command that will list all of the available commands
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help') #List of commands
    embed.add_field(name='<hello', value='Says hi', inline=False)
    embed.add_field(name='<join', value='Joins vc', inline=False)
    embed.add_field(name='<hello', value='Leaves vc', inline=False)

    await author.send(embed=embed)

#Command to join vc
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

#command to leave vc
@client.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        await server.disconnect()

client.run(bot_token)
