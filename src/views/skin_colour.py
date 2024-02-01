from discord import SelectOption
from discord.ui import View, select


class SkinColourView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @select(
        placeholder="Elegí el color de piel del jugador",
        options=[
            SelectOption(label="Palido", value="1"),
            SelectOption(label="Blanco", value="2"),
            SelectOption(label="Riquelme", value="3"),
            SelectOption(label="Negro", value="4"),
        ],
    )
    async def select_callback(self, select, interaction):
        self.selected_values = select.values
        self.stop()
