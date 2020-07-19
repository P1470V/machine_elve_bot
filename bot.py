import discord
from discord.ext import commands

bot_token = input("Bot Token: ")

client = commands.Bot(command_prefix="<")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Go Fuck yourself")

client.run(bot_token)
