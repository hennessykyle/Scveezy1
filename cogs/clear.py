import disnake
from disnake.ext import commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='очистка', description="Очистить чат")
    async def clear(self, interaction, amount: int):
        embed = disnake.Embed(title="clear", description=f"Удалено {amount} сообщений", color=0x00ff00)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.channel.purge(limit=amount + 1)


def setup(bot):
    bot.add_cog(Clear(bot))