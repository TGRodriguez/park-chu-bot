from discord import SelectOption
from discord.ui import View, select


class NationalityView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @select(
        placeholder="Europa A",
        # all the options with the label in spanish and value in english
        options=[
            SelectOption(label="Albania", value="Albania"),
            SelectOption(label="Austria", value="Austria"),
            SelectOption(label="Bielorrusia", value="Belarus"),
            SelectOption(label="Bélgica", value="Belgium"),
            SelectOption(label="Bosnia y Herzegovina", value="Bosnia and Herzegovina"),
            SelectOption(label="Bulgaria", value="Bulgaria"),
            SelectOption(label="Croacia", value="Croatia"),
            SelectOption(label="Chipre", value="Cyprus"),
            SelectOption(label="República Checa", value="Czech Republic"),
            SelectOption(label="Dinamarca", value="Denmark"),
            SelectOption(label="Inglaterra", value="England"),
            SelectOption(label="Estonia", value="Estonia"),
            SelectOption(label="Finlandia", value="Finland"),
            SelectOption(label="Francia", value="France"),
            SelectOption(label="Alemania", value="Germany"),
            SelectOption(label="Grecia", value="Greece"),
            SelectOption(label="Hungría", value="Hungary"),
            SelectOption(label="Islandia", value="Iceland"),
            SelectOption(label="Irlanda", value="Ireland"),
            SelectOption(label="Italia", value="Italy"),
            SelectOption(label="Letonia", value="Latvia"),
            SelectOption(label="Liechtenstein", value="Liechtenstein"),
            SelectOption(label="Lituania", value="Lithuania"),
            SelectOption(label="Macedonia", value="Macedonia"),
        ],
    )
    async def select_callback_europe_a(self, select, interaction):
        await self.handle_selection(select, interaction)

    @select(
        placeholder="Europa B",
        options=[
            SelectOption(label="Países Bajos", value="Netherlands"),
            SelectOption(label="Irlanda del Norte", value="Northern Ireland"),
            SelectOption(label="Noruega", value="Norway"),
            SelectOption(label="Polonia", value="Poland"),
            SelectOption(label="Portugal", value="Portugal"),
            SelectOption(label="Rumania", value="Romania"),
            SelectOption(label="Rusia", value="Russia"),
            SelectOption(label="Escocia", value="Scotland"),
            SelectOption(label="Serbia y Montenegro", value="Serbia and Montenegro"),
            SelectOption(label="Eslovaquia", value="Slovakia"),
            SelectOption(label="Eslovenia", value="Slovenia"),
            SelectOption(label="España", value="Spain"),
            SelectOption(label="Suecia", value="Sweden"),
            SelectOption(label="Suiza", value="Switzerland"),
            SelectOption(label="Ucrania", value="Ukraine"),
            SelectOption(label="Gales", value="Wales"),
        ],
    )
    async def select_callback_europe_b(self, select, interaction):
        await self.handle_selection(select, interaction)

    @select(
        placeholder="África",
        options=[
            SelectOption(label="Angola", value="Angola"),
            SelectOption(label="Benin", value="Benin"),
            SelectOption(label="Burkina Faso", value="Burkina Faso"),
            SelectOption(label="Cabo Verde", value="Cape Verde"),
            SelectOption(label="Camerún", value="Cameroon"),
            SelectOption(label="RD Congo", value="DR Congo"),
            SelectOption(label="Costa de Marfil", value="Cote d'Ivoire"),
            SelectOption(label="Egipto", value="Egypt"),
            SelectOption(label="Gabón", value="Gabon"),
            SelectOption(label="Gambia", value="Gambia"),
            SelectOption(label="Ghana", value="Ghana"),
            SelectOption(label="Guinea", value="Guinea"),
            SelectOption(label="Guinea-Bissau", value="Guinea-Bissau"),
            SelectOption(label="Guinea Ecuatorial", value="Equatorial Guinea"),
            SelectOption(label="Kenia", value="Kenya"),
            SelectOption(label="Nigeria", value="Nigeria"),
            SelectOption(label="Senegal", value="Senegal"),
            SelectOption(label="Sudáfrica", value="South Africa"),
            SelectOption(label="Libia", value="Libya"),
            SelectOption(label="Liberia", value="Liberia"),
            SelectOption(label="Mali", value="Mali"),
            SelectOption(label="Mozambique", value="Mozambique"),
            SelectOption(label="Zimbabue", value="Zimbabwe"),
            SelectOption(label="Togo", value="Togo"),
            SelectOption(label="Sierra Leona", value="Sierra Leone"),
        ],
    )
    async def select_callback_africa(self, select, interaction):
        await self.handle_selection(select, interaction)

    @select(
        placeholder="América",
        options=[
            SelectOption(label="Argentina", value="Argentina"),
            SelectOption(label="Bolivia", value="Bolivia"),
            SelectOption(label="Brasil", value="Brazil"),
            SelectOption(label="Canadá", value="Canada"),
            SelectOption(label="Chile", value="Chile"),
            SelectOption(label="Colombia", value="Colombia"),
            SelectOption(label="Costa Rica", value="Costa Rica"),
            SelectOption(label="Ecuador", value="Ecuador"),
            SelectOption(label="Honduras", value="Honduras"),
            SelectOption(label="Jamaica", value="Jamaica"),
            SelectOption(label="México", value="Mexico"),
            SelectOption(label="Panamá", value="Panama"),
            SelectOption(label="Paraguay", value="Paraguay"),
            SelectOption(label="Perú", value="Peru"),
            SelectOption(label="Estados Unidos", value="United States"),
            SelectOption(label="Uruguay", value="Uruguay"),
            SelectOption(label="Venezuela", value="Venezuela"),
            SelectOption(label="Granada", value="Grenada"),
            SelectOption(label="Guadalupe", value="Guadeloupe"),
            SelectOption(label="Martinica", value="Martinique"),
            SelectOption(label="Trinidad y Tobago", value="Trinidad and Tobago"),
            SelectOption(label="Antillas Neerlandesas", value="Netherlands Antilles"),
        ],
    )
    async def select_callback_america(self, select, interaction):
        await self.handle_selection(select, interaction)

    @select(
        placeholder="Asia y Oceanía",
        options=[
            SelectOption(label="Australia", value="Australia"),
            SelectOption(label="Armernia", value="Armenia"),
            SelectOption(label="China", value="China"),
            SelectOption(label="Georgia", value="Georgia"),
            SelectOption(label="Irán", value="Iran"),
            SelectOption(label="Israel", value="Israel"),
            SelectOption(label="Japón", value="Japan"),
            SelectOption(label="Nueva Zelanda", value="New Zealand"),
            SelectOption(label="Omán", value="Oman"),
            SelectOption(label="Arabia Saudita", value="Saudi Arabia"),
            SelectOption(label="Corea del Sur", value="South Korea"),
            SelectOption(label="Túnez", value="Tunisia"),
            SelectOption(label="Turquía", value="Turkey"),
            SelectOption(label="Uzbekistán", value="Uzbekistan"),
            SelectOption(label="Argelia", value="Algeria", emoji="🌍"),
            SelectOption(label="Marruecos", value="Morocco", emoji="🌍"),
        ],
    )
    async def select_callback_asia_oceania(self, select, interaction):
        await self.handle_selection(select, interaction)

    async def handle_selection(self, select, interaction):
        if self.selected_values:
            await interaction.response.send_message(
                "Mirá capo, solo podés elegir una nacionalidad", ephemeral=True
            )
        else:
            self.selected_values = select.values
            self.stop()
