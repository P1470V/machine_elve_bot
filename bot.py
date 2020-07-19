import discord
from discord.ext import commands

client = commands.Bot(command_prefix="<")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Go Fuck yourself")

client.run("NzM0NDUxMTk5NjE2NjE0NDkx.XxR5Yg.YIy1CHn55dkdVmt5dbFb5Lf7zxw")
