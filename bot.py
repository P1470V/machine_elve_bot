import discord
from discord.ext import commands

help_file = open("help.txt", "r")
bot_token = input("Bot Token: ") #Discord Bot Token

client = commands.Bot(command_prefix="<")
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
@client.command()
async def help(ctx):
    await ctx.send(help_file.read())

client.run(bot_token)
