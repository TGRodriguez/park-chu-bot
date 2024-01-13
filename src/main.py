import asyncio
import discord
from env_vars import load_env_vars
import random
import csv
import os
import request

load_env_vars()


def cargar_selecciones(ruta):
    selecciones = []
    with open(ruta) as archivo_selecciones:
        selecciones_reader = csv.reader(archivo_selecciones)
        for seleccion in selecciones_reader:
            selecciones.append((seleccion[0], seleccion[1]))
    return selecciones


selecciones = cargar_selecciones("src/selecciones.txt")

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.command()
async def selesion(ctx):
    seleccion, bandera = random.choice(selecciones)
    await ctx.send(f"Mirá capo te toca jugar con {seleccion} {bandera}")


class FavouredSide(discord.ui.View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @discord.ui.select(
        placeholder="Elegí el lado del jugador",
        options=[
            discord.SelectOption(label="Derecho", value="R"),
            discord.SelectOption(label="Izquierdo", value="L"),
            discord.SelectOption(label="Ambos", value="B"),
        ],
    )
    async def select_callback(self, select, interaction):
        self.selected_values = select.values
        self.stop()


class FavouredFoot(discord.ui.View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @discord.ui.select(
        placeholder="Elegí el pie hábil del jugador",
        options=[
            discord.SelectOption(label="Derecho", value="R"),
            discord.SelectOption(label="Izquierdo", value="L"),
        ],
    )
    async def select_callback(self, select, interaction):
        self.selected_values = select.values
        self.stop()


class AgeInput:
    def __init__(self, interaction, bot, type):
        self.interaction = interaction
        self.user = interaction.user
        self.channel = interaction.channel
        self.bot = bot
        self.selected_values = None
        self.type = type
        self.msg = None

    async def send(self):
        self.msg = await self.interaction.followup.send(
            f"Dale capo, decime la edad {self.type}", ephemeral=False
        )

        def check(msg):
            return (
                msg.author == self.user
                and msg.channel == self.channel
                and msg.content.isdigit()
            )

        try:
            msg = await self.bot.wait_for("message", timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await self.interaction.followup.send(
                "Mirá capo, tardaste mucho en responder", ephemeral=True
            )
            return
        else:
            age = int(msg.content)
            self.selected_values = age
            await self.msg.delete()
            await msg.delete()


class NationalityView(discord.ui.View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @discord.ui.select(
        placeholder="Europa A",
        # all the options with the label in spanish and value in english
        options=[
            discord.SelectOption(label="Albania", value="Albania"),
            discord.SelectOption(label="Austria", value="Austria"),
            discord.SelectOption(label="Bielorrusia", value="Belarus"),
            discord.SelectOption(label="Bélgica", value="Belgium"),
            discord.SelectOption(
                label="Bosnia y Herzegovina", value="Bosnia and Herzegovina"
            ),
            discord.SelectOption(label="Bulgaria", value="Bulgaria"),
            discord.SelectOption(label="Croacia", value="Croatia"),
            discord.SelectOption(label="Chipre", value="Cyprus"),
            discord.SelectOption(label="República Checa", value="Czech Republic"),
            discord.SelectOption(label="Dinamarca", value="Denmark"),
            discord.SelectOption(label="Inglaterra", value="England"),
            discord.SelectOption(label="Estonia", value="Estonia"),
            discord.SelectOption(label="Finlandia", value="Finland"),
            discord.SelectOption(label="Francia", value="France"),
            discord.SelectOption(label="Alemania", value="Germany"),
            discord.SelectOption(label="Grecia", value="Greece"),
            discord.SelectOption(label="Hungría", value="Hungary"),
            discord.SelectOption(label="Islandia", value="Iceland"),
            discord.SelectOption(label="Irlanda", value="Ireland"),
            discord.SelectOption(label="Italia", value="Italy"),
            discord.SelectOption(label="Letonia", value="Latvia"),
            discord.SelectOption(label="Liechtenstein", value="Liechtenstein"),
            discord.SelectOption(label="Lituania", value="Lithuania"),
            discord.SelectOption(label="Macedonia", value="Macedonia"),
        ],
    )
    async def select_callback_europe_a(self, select, interaction):
        await self.handle_selection(select, interaction)

    @discord.ui.select(
        placeholder="Europa B",
        options=[
            discord.SelectOption(label="Países Bajos", value="Netherlands"),
            discord.SelectOption(label="Irlanda del Norte", value="Northern Ireland"),
            discord.SelectOption(label="Noruega", value="Norway"),
            discord.SelectOption(label="Polonia", value="Poland"),
            discord.SelectOption(label="Portugal", value="Portugal"),
            discord.SelectOption(label="Rumania", value="Romania"),
            discord.SelectOption(label="Rusia", value="Russia"),
            discord.SelectOption(label="Escocia", value="Scotland"),
            discord.SelectOption(
                label="Serbia y Montenegro", value="Serbia and Montenegro"
            ),
            discord.SelectOption(label="Eslovaquia", value="Slovakia"),
            discord.SelectOption(label="Eslovenia", value="Slovenia"),
            discord.SelectOption(label="España", value="Spain"),
            discord.SelectOption(label="Suecia", value="Sweden"),
            discord.SelectOption(label="Suiza", value="Switzerland"),
            discord.SelectOption(label="Ucrania", value="Ukraine"),
            discord.SelectOption(label="Gales", value="Wales"),
        ],
    )
    async def select_callback_europe_b(self, select, interaction):
        await self.handle_selection(select, interaction)

    @discord.ui.select(
        placeholder="África",
        options=[
            discord.SelectOption(label="Angola", value="Angola"),
            discord.SelectOption(label="Benin", value="Benin"),
            discord.SelectOption(label="Burkina Faso", value="Burkina Faso"),
            discord.SelectOption(label="Cabo Verde", value="Cape Verde"),
            discord.SelectOption(label="Camerún", value="Cameroon"),
            discord.SelectOption(label="RD Congo", value="DR Congo"),
            discord.SelectOption(label="Costa de Marfil", value="Cote d'Ivoire"),
            discord.SelectOption(label="Egipto", value="Egypt"),
            discord.SelectOption(label="Gabón", value="Gabon"),
            discord.SelectOption(label="Gambia", value="Gambia"),
            discord.SelectOption(label="Ghana", value="Ghana"),
            discord.SelectOption(label="Guinea", value="Guinea"),
            discord.SelectOption(label="Guinea-Bissau", value="Guinea-Bissau"),
            discord.SelectOption(label="Guinea Ecuatorial", value="Equatorial Guinea"),
            discord.SelectOption(label="Kenia", value="Kenya"),
            discord.SelectOption(label="Nigeria", value="Nigeria"),
            discord.SelectOption(label="Senegal", value="Senegal"),
            discord.SelectOption(label="Sudáfrica", value="South Africa"),
            discord.SelectOption(label="Libia", value="Libya"),
            discord.SelectOption(label="Liberia", value="Liberia"),
            discord.SelectOption(label="Mali", value="Mali"),
            discord.SelectOption(label="Mozambique", value="Mozambique"),
            discord.SelectOption(label="Zimbabue", value="Zimbabwe"),
            discord.SelectOption(label="Togo", value="Togo"),
            discord.SelectOption(label="Sierra Leona", value="Sierra Leone"),
        ],
    )
    async def select_callback_africa(self, select, interaction):
        await self.handle_selection(select, interaction)

    @discord.ui.select(
        placeholder="América",
        options=[
            discord.SelectOption(label="Argentina", value="Argentina"),
            discord.SelectOption(label="Bolivia", value="Bolivia"),
            discord.SelectOption(label="Brasil", value="Brazil"),
            discord.SelectOption(label="Canadá", value="Canada"),
            discord.SelectOption(label="Chile", value="Chile"),
            discord.SelectOption(label="Colombia", value="Colombia"),
            discord.SelectOption(label="Costa Rica", value="Costa Rica"),
            discord.SelectOption(label="Ecuador", value="Ecuador"),
            discord.SelectOption(label="Honduras", value="Honduras"),
            discord.SelectOption(label="Jamaica", value="Jamaica"),
            discord.SelectOption(label="México", value="Mexico"),
            discord.SelectOption(label="Panamá", value="Panama"),
            discord.SelectOption(label="Paraguay", value="Paraguay"),
            discord.SelectOption(label="Perú", value="Peru"),
            discord.SelectOption(label="Estados Unidos", value="United States"),
            discord.SelectOption(label="Uruguay", value="Uruguay"),
            discord.SelectOption(label="Venezuela", value="Venezuela"),
            discord.SelectOption(label="Granada", value="Grenada"),
            discord.SelectOption(label="Guadalupe", value="Guadeloupe"),
            discord.SelectOption(label="Martinica", value="Martinique"),
            discord.SelectOption(label="Trinidad y Tobago", value="Trinidad and Tobago"),
            discord.SelectOption(
                label="Antillas Neerlandesas", value="Netherlands Antilles"
            ),
        ],
    )
    async def select_callback_america(self, select, interaction):
        await self.handle_selection(select, interaction)

    @discord.ui.select(
        placeholder="Asia y Oceanía",
        options=[
            discord.SelectOption(label="Australia", value="Australia"),
            discord.SelectOption(label="Armernia", value="Armenia"),
            discord.SelectOption(label="China", value="China"),
            discord.SelectOption(label="Georgia", value="Georgia"),
            discord.SelectOption(label="Irán", value="Iran"),
            discord.SelectOption(label="Israel", value="Israel"),
            discord.SelectOption(label="Japón", value="Japan"),
            discord.SelectOption(label="Nueva Zelanda", value="New Zealand"),
            discord.SelectOption(label="Omán", value="Oman"),
            discord.SelectOption(label="Arabia Saudita", value="Saudi Arabia"),
            discord.SelectOption(label="Corea del Sur", value="South Korea"),
            discord.SelectOption(label="Túnez", value="Tunisia"),
            discord.SelectOption(label="Turquía", value="Turkey"),
            discord.SelectOption(label="Uzbekistán", value="Uzbekistan"),
            discord.SelectOption(label="Argelia", value="Algeria", emoji="🌍"),
            discord.SelectOption(label="Marruecos", value="Morocco", emoji="🌍"),
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


class SkinColorView(discord.ui.View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @discord.ui.select(
        placeholder="Elegí el color de piel del jugador",
        options=[
            discord.SelectOption(label="Palido", value="1"),
            discord.SelectOption(label="Blanco", value="2"),
            discord.SelectOption(label="Riquelme", value="3"),
            discord.SelectOption(label="Negro", value="4"),
        ],
    )
    async def select_callback(self, select, interaction):
        self.selected_values = select.values
        self.stop()


class RegisteredPositionView(discord.ui.View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @discord.ui.select(
        placeholder="Elegí la posición registrada del jugador",
        options=[
            discord.SelectOption(label="Arquero (PT)", value="1"),
            discord.SelectOption(label="Libero (LIB)", value="2"),
            discord.SelectOption(label="Central (CT)", value="3"),
            discord.SelectOption(label="Carrilero (CA)", value="4"),
            discord.SelectOption(label="Cinco (CCD)", value="5"),
            discord.SelectOption(label="Lateral (LA)", value="6"),
            discord.SelectOption(label="Mediocampista central (CC)", value="7"),
            discord.SelectOption(label="Volante (VOL)", value="8"),
            discord.SelectOption(label="Enganche (MP)", value="9"),
            discord.SelectOption(label="Extremo (EX)", value="10"),
            discord.SelectOption(label="Segunda punta (SD)", value="11"),
            discord.SelectOption(label="Nueve (DC)", value="12"),
        ],
    )
    async def select_callback(self, select, interaction):
        self.selected_values = select.values
        self.stop()


class AvailablePositionsView(discord.ui.View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = None

    @discord.ui.select(
        placeholder="Elegí las posiciones disponibles del jugador",
        max_values=12,
        options=[
            discord.SelectOption(label="Arquero (PT)", value="ARQUERO"),
            discord.SelectOption(label="Libero (LIB)", value="LIBERO"),
            discord.SelectOption(label="Central (CT)", value="CENTRAL"),
            discord.SelectOption(label="Carrilero (CA)", value="CARRILERO"),
            discord.SelectOption(label="Cinco (CCD)", value="CINCO"),
            discord.SelectOption(label="Lateral (LA)", value="LATERAL"),
            discord.SelectOption(
                label="Mediocampista central (CC)", value="MEDIOCAMPISTA CENTRAL"
            ),
            discord.SelectOption(label="Volante (VOL)", value="VOLANTE"),
            discord.SelectOption(label="Enganche (MP)", value="ENGANCHE"),
            discord.SelectOption(label="Extremo (EX)", value="EXTREMO"),
            discord.SelectOption(label="Segunda punta (SD)", value="SEGUNDA PUNTA"),
            discord.SelectOption(label="Nueve (DC)", value="NUEVE"),
        ],
    )
    async def select_callback(self, select, interaction):
        self.selected_values = select.values
        self.stop()


class OptionsView(discord.ui.View):
    def __init__(self, bot, **kwargs):
        super().__init__(**kwargs)
        self.selected_values = {}
        self.bot = bot

    @discord.ui.select(
        placeholder="Elegí las opciones que querés configurar",
        max_values=6,
        options=[
            discord.SelectOption(
                label="Posición Registrada", value="registered_position"
            ),
            discord.SelectOption(label="Posiciones Disponibles", value="positions"),
            discord.SelectOption(label="Nacionalidad", value="nationality"),
            discord.SelectOption(label="Color de Piel", value="skin_colour"),
            discord.SelectOption(label="Edad Mínima", value="min_age"),
            discord.SelectOption(label="Edad Máxima", value="max_age"),
            discord.SelectOption(label="Lado", value="favoured_side"),
            discord.SelectOption(label="Pie Hábil", value="favoured_foot"),
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
                skin_color_view = SkinColorView()
                msg = await interaction.followup.send(
                    "Dale capo, decime el color de piel",
                    ephemeral=True,
                    view=skin_color_view,
                )
                await skin_color_view.wait()
                self.selected_values[value] = skin_color_view.selected_values
                await msg.delete()
            elif value == "favoured_side":
                favoured_side_view = FavouredSide()
                msg = await interaction.followup.send(
                    "Dale capo, decime el lado", ephemeral=True, view=favoured_side_view
                )
                await favoured_side_view.wait()
                self.selected_values[value] = favoured_side_view.selected_values
                await msg.delete()
            elif value == "favoured_foot":
                favoured_foot_view = FavouredFoot()
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
        self.stop()


@bot.command()
async def jugador(ctx):
    view = OptionsView(ctx.bot)

    await ctx.respond(
        f"{ctx.author.mention}, mirá capo, elegí los filtros que quieras:", view=view
    )
    await view.wait()
    total_filters = view.selected_values

    jugadores = await request.get(os.getenv("API_URL") + "/v1/players", total_filters)
    if len(jugadores) == 0:
        await ctx.send(
            f"{ctx.author.mention} mirá capo, no hay jugadores que cumplan con eso"
        )
    else:
        jugador = jugadores[0]
        await ctx.send(
            f"""{ctx.author.mention} mirá capo, te toca comprarte a:
                       \nNombre: {jugador['name']}
                       \nNacionalidad: {jugador['nationality']}
                       \nColor de Piel: {jugador['skin_colour']}
                       \nEdad: {jugador['age']}
                       \nPie Hábil: {jugador['strong_foot']}
                       \nLado: {jugador['favoured_side']}
                       \nPosición Registrada: {jugador['favoured_position']}
                       \nPosiciones Disponibles: {jugador['positions']}
                       """
        )


bot.run(os.environ.get("DISCORD_BOT_TOKEN"))
