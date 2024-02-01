from discord import SelectOption
from discord.ui import View, select


class AvailablePositionsView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @select(
        placeholder="Elegí las posiciones disponibles del jugador",
        max_values=12,
        options=[
            SelectOption(label="Libero (LIB)", value="LIBERO"),
            SelectOption(label="Arquero (PT)", value="ARQUERO"),
            SelectOption(label="Central (CT)", value="CENTRAL"),
            SelectOption(label="Carrilero (CA)", value="CARRILERO"),
            SelectOption(label="Cinco (CCD)", value="CINCO"),
            SelectOption(label="Lateral (LA)", value="LATERAL"),
            SelectOption(
                label="Mediocampista central (CC)", value="MEDIOCAMPISTA CENTRAL"
            ),
            SelectOption(label="Volante (VOL)", value="VOLANTE"),
            SelectOption(label="Enganche (MP)", value="ENGANCHE"),
            SelectOption(label="Extremo (EX)", value="EXTREMO"),
            SelectOption(label="Segunda punta (SD)", value="SEGUNDA PUNTA"),
            SelectOption(label="Nueve (DC)", value="NUEVE"),
        ],
    )
    async def select_callback(self, select, interaction):
        self.selected_values = select.values
        self.stop()
