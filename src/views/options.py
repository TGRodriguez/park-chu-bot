from discord import SelectOption
from discord.ui import View, select
from views.age import AgeInput
from views.height import HeightInput
from views.available_positions import AvailablePositionsView
from views.favoured_foot import FavouredFootView
from views.favoured_side import FavouredSideView
from views.nationality import NationalityView
from views.registered_position import RegisteredPositionView
from views.skin_colour import SkinColourView


class OptionsView(View):
    def __init__(self, bot, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = {}
        self.bot = bot

    @select(
        placeholder="Elegí las opciones que querés configurar",
        max_values=8,
        options=[
            SelectOption(label="Posición Registrada", value="registered_position"),
            SelectOption(label="Posiciones Disponibles", value="positions"),
            SelectOption(label="Nacionalidad", value="nationality"),
            SelectOption(label="Color de Piel", value="skin_colour"),
            SelectOption(label="Edad Mínima", value="min_age"),
            SelectOption(label="Edad Máxima", value="max_age"),
            SelectOption(label="Altura Mínima", value="min_height"),
            SelectOption(label="Altura Máxima", value="max_height"),
            SelectOption(label="Lado", value="favoured_side"),
            SelectOption(label="Pie Hábil", value="favoured_foot"),
        ],
    )
    async def select_callback(self, select, interaction):
        await interaction.response.send_message(
            f"Elegiste {select.values}", ephemeral=True
        )
        for value in select.values:
            if value == "registered_position":
                registered_position_view = RegisteredPositionView()
                msg = await interaction.followup.send(
                    "Dale capo, decime la posición",
                    ephemeral=True,
                    view=registered_position_view,
                )
                await registered_position_view.wait()
                self.selected_values[value] = registered_position_view.selected_values
                await msg.delete()
            elif value == "positions":
                available_positions_view = AvailablePositionsView()
                msg = await interaction.followup.send(
                    "Dale capo, decime las posiciones",
                    ephemeral=True,
                    view=available_positions_view,
                )
                await available_positions_view.wait()
                self.selected_values[value] = available_positions_view.selected_values
                await msg.delete()
            elif value == "nationality":
                nationality_view = NationalityView()
                msg = await interaction.followup.send(
                    "Dale capo, decime la nacionalidad",
                    ephemeral=True,
                    view=nationality_view,
                )
                await nationality_view.wait()
                self.selected_values[value] = nationality_view.selected_values
                await msg.delete()
            elif value == "skin_colour":
                skin_color_view = SkinColourView()
                msg = await interaction.followup.send(
                    "Dale capo, decime el color de piel",
                    ephemeral=True,
                    view=skin_color_view,
                )
                await skin_color_view.wait()
                self.selected_values[value] = skin_color_view.selected_values
                await msg.delete()
            elif value == "favoured_side":
                favoured_side_view = FavouredSideView()
                msg = await interaction.followup.send(
                    "Dale capo, decime el lado", ephemeral=True, view=favoured_side_view
                )
                await favoured_side_view.wait()
                self.selected_values[value] = favoured_side_view.selected_values
                await msg.delete()
            elif value == "favoured_foot":
                favoured_foot_view = FavouredFootView()
                msg = await interaction.followup.send(
                    "Dale capo, decime el pie hábil",
                    ephemeral=True,
                    view=favoured_foot_view,
                )
                await favoured_foot_view.wait()
                self.selected_values[value] = favoured_foot_view.selected_values
                await msg.delete()
            elif value == "min_age":
                min_age_input = AgeInput(interaction, self.bot, "mínima")
                await min_age_input.send()
                self.selected_values[value] = min_age_input.selected_values
            elif value == "max_age":
                max_age_input = AgeInput(interaction, self.bot, "máxima")
                await max_age_input.send()
                self.selected_values[value] = max_age_input.selected_values
            elif value == "min_height":
                min_height_input = HeightInput(interaction, self.bot, "mínima")
                await min_height_input.send()
                self.selected_values[value] = min_height_input.selected_values
            elif value == "max_height":
                max_height_input = HeightInput(interaction, self.bot, "máxima")
                await max_height_input.send()
                self.selected_values[value] = max_height_input.selected_values
        self.stop()
