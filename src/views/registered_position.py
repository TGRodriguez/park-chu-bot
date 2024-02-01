from discord import SelectOption
from discord.ui import View, select


class RegisteredPositionView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @select(
        placeholder="Elegí la posición registrada del jugador",
        options=[
            SelectOption(label="Arquero (PT)", value="1"),
            SelectOption(label="Libero (LIB)", value="2"),
            SelectOption(label="Central (CT)", value="3"),
            SelectOption(label="Carrilero (CA)", value="4"),
            SelectOption(label="Cinco (CCD)", value="5"),
            SelectOption(label="Lateral (LA)", value="6"),
            SelectOption(label="Mediocampista central (CC)", value="7"),
            SelectOption(label="Volante (VOL)", value="8"),
            SelectOption(label="Enganche (MP)", value="9"),
            SelectOption(label="Extremo (EX)", value="10"),
            SelectOption(label="Segunda punta (SD)", value="11"),
            SelectOption(label="Nueve (DC)", value="12"),
        ],
    )
    async def select_callback(self, select, interaction):
        self.selected_values = select.values
        self.stop()
