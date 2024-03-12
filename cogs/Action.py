import disnake
from disnake.ext import commands
import random

kiss = ['https://24.media.tumblr.com/ab0cb466ca57304d9b59a12755c8e9cd/tumblr_mutiqnNtUW1sg82qmo1_400.gif']
hug = ['https://media.tenor.com/Glql1LPSciQAAAAM/milk-and-mocha-milk-mocha.gif']
slap = ['https://img10.joyreactor.cc/pics/comment/%D0%B3%D0%B8%D1%84%D0%BA%D0%B8-%D0%BF%D0%BE%D0%B5%D0%B4%D0%B8%D0%BD%D0%BE%D0%BA-Slap-%D1%83%D0%B4%D0%B0%D0%BB%D1%91%D0%BD%D0%BD%D0%BE%D0%B5-2444013.gif']

class Action(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Модуль {} загружен'.format(self.__init__.__name__))

    @commands.slash_command(name='кисс', description="Поцеловать")
    async def kiss(self, ctx, member: disnake.Member):
        embed = disnake.Embed()
        embed.set_image(url=random.choice(kiss))
        await ctx.send(f"{ctx.author.mention} поцеловал {member.mention}", embed=embed)

    @commands.slash_command(name='хьюг', description="Обнять")
    async def hug(self, ctx, member: disnake.Member):
        embed = disnake.Embed()
        embed.set_image(url=random.choice(hug))
        await ctx.send(f"{ctx.author.mention} крепко обнял {member.mention}", embed=embed)

    @commands.slash_command(name='слап', description="Ударить")
    async def slap(self, ctx, member: disnake.Member):
        embed = disnake.Embed()
        embed.set_image(url=random.choice(slap))
        await ctx.send(f"{ctx.author.mention} ударил {member.mention}", embed=embed)


def setup(bot):
    bot.add_cog(Action(bot))