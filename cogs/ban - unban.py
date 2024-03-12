import disnake
from disnake.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='бан', description="Забанить Участника")
    async def ban(self, interaction, ctx, user: disnake.User, *, reason=None):
        await interaction.guild.ban(user, reason=reason)
        await interaction.response.send_message(f"Администратор {ctx.author.name} заблокировал пользователя {user.mention} по причине {reason}, ephemeral=True")

    @commands.slash_command(name='разбан', description="Разбанить Участника")
    async def unban(self, interaction, ctx, user: disnake.User, *, reason=None):
        await interaction.guild.unban(user, reason=reason)
        await interaction.response.send_message(f"Администратор {ctx.author.name} разблокировал пользователя {user.mention} по причине {reason}, ephemeral=True")


def setup(bot):
    bot.add_cog(Ban(bot))