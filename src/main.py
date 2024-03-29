import discord
from env_vars import load_env_vars
import random
import csv
import os
import request
from views.options import OptionsView

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
    await ctx.respond(f"Mirá capo te toca jugar con {seleccion} {bandera}")


@bot.command()
async def jugador(ctx):
    view = OptionsView(ctx.bot)

    await ctx.respond(
        f"{ctx.author.mention}, mirá capo, elegí los filtros que quieras:", view=view
    )
    await view.wait()
    total_filters = view.selected_values
    await ctx.send(f"Mirá capo, elegiste {total_filters}")

    jugadores = await request.get(os.getenv("API_URL") + "/v1/players", total_filters)
    if len(jugadores) == 0:
        await ctx.send(
            f"{ctx.author.mention} mirá capo, no hay jugadores que cumplan con eso"
        )
    else:
        jugador = jugadores[0]
        await ctx.send(
            f"{ctx.author.mention} mirá capo, te toca comprarte a:\n"
            f"* Nombre: {jugador['name']}\n"
            f"* Nacionalidad: {jugador['nationality']}\n"
            f"* Color de Piel: {jugador['skin_colour']}\n"
            f"* Edad: {jugador['age']}\n"
            f"* Altura: {jugador['height']}\n"
            f"* Pie Hábil: {jugador['strong_foot']}\n"
            f"* Lado: {jugador['favoured_side']}\n"
            f"* Posición Registrada: {jugador['favoured_position']}\n"
            f"* Posiciones Disponibles: {jugador['positions']}\n"
            f"* Media: {jugador['average_stats']}\n"
            f"* Equipos:\n"
            f"  * Selección: {jugador['teams']['national_team']}\n"
            f"  * Club: {jugador['teams']['club_team']}\n"
        )


bot.run(os.environ.get("DISCORD_BOT_TOKEN"))
