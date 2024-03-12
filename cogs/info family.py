import disnake
from disnake.ext import commands


class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='информация', description="Информация о Семье")
    async def info(self, interaction):
        embed = disnake.Embed(title="Информация о Семье Hennessy", description="", color=0x00ff00)
        embed.add_field(name="Лидер Семьи: Jonny_Hennessy", value="Discord: jhennessyy", inline=False)
        embed.add_field(name="Заместитель Семьи №1: Adolf_Hennessy", value="Discord: henenssy5865", inline=False)
        embed.add_field(name="Заместитель Семьи №2: Kyle_Hennessy", value="Discord: hennessy.k", inline=False)
        embed.add_field(name="Заместитель Семьи №3: Alfred_Hennessy", value="Discord: kro11er", inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Embed(bot))