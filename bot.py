import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('OTE0MjIyMzU2NDkzMzc3NTc2.YaJ56w.9RC7c4WiorqTe9_iyn2-1T5V-eo')