from discord import SelectOption
from discord.ui import View, select


class FavouredSideView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @select(
        placeholder="Elegí el lado del jugador",
        options=[
            SelectOption(label="Derecho", value="R"),
            SelectOption(label="Izquierdo", value="L"),
            SelectOption(label="Ambos", value="B"),
        ],
    )
    async def select_callback(self, select, interaction):
        self.selected_values = select.values
        self.stop()
