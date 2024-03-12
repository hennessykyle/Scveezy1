import disnake
from disnake.ext import commands

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='мут', description="Замутить Участника")
    @commands.has_any_role(1217054655175983204)
    async def mute(self, ctx, user: disnake.Member, *, reason=None):
        await user.move_to(channel=None)
        mute = disnake.utils.get(ctx.guild.roles, name="Официально ГЕЙ")
        await user.add_roles(mute)
        await ctx.send(f"Администратор {ctx.author.mention} замутил участника {user.mention} по причине: {reason}")

    @commands.slash_command(name='размут', description="Размутить Участника")
    @commands.has_any_role(1217054655175983204)
    async def unmute(self, ctx, user: disnake.Member):
        mute = disnake.utils.get(ctx.guild.roles, name="Официально ГЕЙ")
        await user.remove_roles(mute)
        await ctx.send(f"Администратор {ctx.author.mention} размутил пользователя {user.mention}")   

def setup(bot):
    bot.add_cog(Mute(bot)) 