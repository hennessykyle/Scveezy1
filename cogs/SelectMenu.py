import disnake
from disnake.ext import commands


class SelectGames(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Dota 2", value="1215266605039226940", emoji="<:dota:1070792276793626715>"),
            disnake.SelectOption(label="Valorant", value="1215266680964517960",
                                 emoji="<:valorant:1070792273102651584>"),
            disnake.SelectOption(label="Genshin Impact", value="1215266737793278042",
                                 emoji="<:genshin:1070792271055831110>")]
        super().__init__(placeholder="Select a game", options=options, custom_id="games", min_values=0, max_values=3)


    async def callback(self, interaction: disnake.MessageInteraction):
        await interaction.response.defer()
        all_roles = {1215266605039226940, 1215266680964517960, 1215266737793278042}
        to_remove = []
        to_add = []

        if not interaction.values:
            for role_id in all_roles:
                role = interaction.guild.get_role(role_id)
                to_remove.append(role)

            await interaction.author.remove_roles(*to_remove, reason="Removed all roles")

        else:
            chosen_roles = {int(value) for value in interaction.values}
            ids_to_remove = all_roles - chosen_roles

            for role_id in ids_to_remove:
                role = interaction.guild.get_role(role_id)
                to_remove.append(role)

            for role_id in chosen_roles:
                role = interaction.guild.get_role(role_id)
                to_add.append(role)

            await interaction.author.remove_roles(*to_remove, reason="Removed roles")
            await interaction.author.add_roles(*to_add, reason="Added roles")


class GameRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistents_views_added = False

    @commands.command()
    async def games(self, ctx):
        view = disnake.ui.View(timeout=None)
        view.add_item(SelectGames())
        embed = disnake.Embed(color=0x2F3136)
        embed.set_author(name="Game roles:")
        embed.description = "Under this post, you can choose your role by clicking on the appropriate" \
                            " role button in the selection menu.\n\n" \
                            "<:dota:1070792276793626715> - Dota 2\n" \
                            "<:valorant:1070792273102651584> - Valorant\n" \
                            "<:genshin:1070792271055831110> - Genshin Impact"
        embed.set_image(url="https://i.imgur.com/QzB7q9J.png")
        await ctx.send(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return

        view = disnake.ui.View(timeout=None)
        view.add_item(SelectGames())
        self.bot.add_view(view, message_id=1070794323689476178)


def setup(bot):
    bot.add_cog(GameRoles(bot))