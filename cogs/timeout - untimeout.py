import datetime

import disnake
from disnake.ext import commands


class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='тайм-аут', description="Выдать Временный Мут")
    async def timeout(self, interaction, member: disnake.Member, time: str, reason: str):
        time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
        await member.timeout(reason=reason, until=time)
        cool_time = disnake.utils.format_dt(time, style="R")
        embed = disnake.Embed(title="тайм-аут", description=f"Администратор {member.author.mention} выдал времнный мут участнику {member.mention} на {cool_time} по причине: {reason}", color=0x00ff00)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @commands.slash_command(name='ютайм-аут', description="Снять Временный Мут")
    async def untimeout(self, interaction, member: disnake.Member):
        await member.timeout(reason=None, until=None)
        embed = disnake.Embed(title="ютайм-аут", description=f"Администратор {member.author.mention} снял времнный мут участнику {member.mention}", color=0x00ff00)
        await interaction.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Timeout(bot))
