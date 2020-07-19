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

    await author.send(embed=embed)

client.run(bot_token)
