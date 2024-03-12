import disnake
from disnake.ext import commands

from utils.databases import UsersDataBase

class PaginatorView(disnake.ui.View):
    def __init__(self, embeds, author, footer: bool, timeout=30.0):
        self.embeds = embeds  # Список эмбедов для отображения.
        self.author = author  # Автор сообщения.
        self.footer = footer  # Флаг для отображения подвала с номером страницы.
        self.timeout = timeout  # Время ожидания в секундах для автоматической очистки интерфейса.
        self.page = 0  # Текущая страница (индекс) из списка эмбедов.
        super().__init__(timeout=self.timeout)

        # Если флаг footer установлен, то добавляем номер страницы в подвал каждого эмбеда.
        if self.footer:
            for emb in self.embeds:
                emb.set_footer(text=f'Страница {self.embeds.index(emb) + 1} из {len(self.embeds)}')

    # Создаем кнопку "Назад" со стрелкой влево.
    @disnake.ui.button(label='◀️', style=disnake.ButtonStyle.grey)
    async def back(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        # Проверяем, что автор кнопки совпадает с автором интерфейса.
        if self.author.id == interaction.author.id:
            if self.page == 0:  # Если текущая страница - первая, перейдем на последнюю.
                self.page = len(self.embeds) - 1
            else:
                self.page -= 1  # В противном случае перейдем на предыдущую страницу.
        else:
            return

        await self.button_callback(interaction)

    # Создаем кнопку "Вперед" со стрелкой вправо.
    @disnake.ui.button(label='▶️', style=disnake.ButtonStyle.grey)
    async def next(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        # Проверяем, что автор кнопки совпадает с автором интерфейса.
        if self.author.id == interaction.author.id:
            if self.page == len(self.embeds) - 1:  # Если текущая страница - последняя, перейдем на первую.
                self.page = 0
            else:
                self.page += 1  # В противном случае перейдем на следующую страницу.
        else:
            return

        await self.button_callback(interaction)

    # Обработчик нажатия кнопки, который отображает соответствующий эмбед.
    async def button_callback(self, interaction):
        # Проверяем, что автор кнопки совпадает с автором интерфейса.
        if self.author.id == interaction.author.id:
            await interaction.response.edit_message(embed=self.embeds[self.page])
        else:
            return await interaction.response.send_message('Вы не можете использовать эту кнопку!', ephemeral=True)





class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = UsersDataBase()

    @commands.slash_command(name='баланс', description='Посмотреть баланс')
    async def balance(self, interaction, member: disnake.Member = None):
        await self.db.create_table()
        if not member:
            member = interaction.author
        await self.db.add_user(member)
        user = await self.db.get_user(member)
        embed = disnake.Embed(color=0x2F3136, title=f'Баланс пользователя - {member}')
        embed.add_field(name='🪙 Деньги', value=f'```{user[1]}```')
        embed.add_field(name='💎 Премиум', value=f'```{user[2]}```')
        embed.set_thumbnail(url=member.display_avatar.url)
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name='выдать', description='Выдать деньги пользователю')
    async def give(self, interaction, member: disnake.Member,
                   amount: int, arg=commands.Param(choices=['деньги', 'премиум'])):
        await self.db.create_table()
        await self.db.add_user(member)
        if arg == 'деньги':
            await self.db.update_money(member, amount, 0)
            embed = disnake.Embed(color=0x2F3136, title=f'Выдача денег пользователю - {member}')
            embed.description = f'{interaction.author.mention} выдал {member.mention} {amount} денег.'
            embed.set_thumbnail(url=member.display_avatar.url)
        else:
            await self.db.update_money(member, 0, amount)
            embed = disnake.Embed(color=0x2F3136, title=f'Выдача премиума пользователю - {member}')
            embed.description = f'{interaction.author.mention} выдал {member.mention} {amount} премиума.'
            embed.set_thumbnail(url=member.display_avatar.url)
        await interaction.response.send_message(embed=embed)

    @commands.slash_command(name='топ', description='Посмотреть топ пользователей')
    async def top(self, interaction):
        await self.db.create_table()
        top = await self.db.get_top()
        embeds = []
        loop_count = 0
        n = 0
        text = ''
        for user in top:
            n += 1
            loop_count += 1
            text += f'**{n}.** {self.bot.get_user(user[0])} - {user[1]} :coin:\n'
            if loop_count % 10 == 0 or loop_count - 1 == len(top) - 1:
                embed = disnake.Embed(color=0x2F3136, title='Топ пользователей')
                embed.description = text
                embed.set_thumbnail(url=interaction.author.display_avatar.url)
                embeds.append(embed)
                text = ''
        view = PaginatorView(embeds, interaction.author, True)
        await interaction.response.send_message(embed=embeds[0], view=view)


def setup(bot):
    bot.add_cog(Economy(bot))
