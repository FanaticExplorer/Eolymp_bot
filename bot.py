import discord
from discord.ext import commands
import os
import eolymp as eo


description = '''I will give any information about any profile on Eolymp.
My github: https://github.com/FanaticExplorer/Eolymp_bot'''

bot = commands.Bot(command_prefix='>', description=description)
place_of_launch=os.environ.get('place')
if place_of_launch=='heroku':
    bot_token=os.environ.get('bot_token')
elif place_of_launch=='local':
    bot_token=os.environ.get('test_bot_token')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')





@bot.command()
async def get_info(ctx, username):
    user = eo.parser(username)
    embed = discord.Embed(color = 0xff9900,
                          title = username,
                          url = user.get_profile_url())
    embed.set_thumbnail(url=user.get_photo_link())
    embed.add_field(name = "Ранг", value=user.get_rating(), inline = False)
    embed.add_field(name = "Решенные задачи", value = user.get_solved(), inline = True)
    embed.add_field(name = "Отправки", value = user.get_total_submissions(), inline = True)
    embed.add_field(name = "Засчитанные решения", value = user.get_submits(), inline = True)
    embed.add_field(name="Последняя задача", value=user.get_last(), inline=False)
    embed.set_footer(text="Спросил: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)


bot.run(bot_token)
