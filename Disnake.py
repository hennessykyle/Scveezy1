import disnake
from disnake.ext import commands
import os
import random 
import datetime

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents, test_guilds={1200648917331755048})

channelIDS = 1200648917365301351

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(channelIDS)
    role = disnake.utils.get (member.guild.roles, id=1200652777454579712)
    await channel.send(embed=disnake.Embed(description=f'Добро пожаловать {member}! Запомни! Море виски и песок - теребонькаю сосок. Камень, Палка, Пиво, Пузо - на моем хуе медуза. ', color=disnake.Color.green()))

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(channelIDS)
    await channel.send(embed=disnake.Embed(description=f'Пользователь {member} решил сходить нахуй.', color=disnake.Color.green()))

@bot.event
async def on_message_delete(message):
    embed = disnake.Embed(title=f"{message.author.mention} удалил сообщение", description=f"`{message.content}`")
    channel = bot.get_channel(1200648918015422466)
    await channel.send(embed=embed)

@bot.event
async def on_message_edit(message_before, message_after):
    embed = disnake.Embed(title=f"{message_before.author.mention} отредактировал сообщение")
    embed.add_field(name="До редактирования", value=f"{message_before.content}", inline=False)
    embed.add_field(name="После Редактирования", value=f"{message_after.content}", inline=False)
    channel = bot.get_channel(1200648918015422466)
    await channel.send(embed=embed)

@bot.event
async def on_ready():
    print("Bot Online!")


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run("MTIxNDA4OTUxNTQwMDk2MjEyOA.GYn2H1.H8AQHcYmowiUCVzul4P5f-IFnAX0NHKAYBgsKg")