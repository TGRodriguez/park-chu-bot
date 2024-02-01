from discord import SelectOption
from discord.ui import View, select


class FavouredFootView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @select(
        placeholder="Elegí el pie hábil del jugador",
        options=[
            SelectOption(label="Derecho", value="R"),
            SelectOption(label="Izquierdo", value="L"),
        ],
    )
    async def select_callback(self, select, interaction):
        self.selected_values = select.values
        self.stop()
