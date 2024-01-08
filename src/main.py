import discord
from env_vars import load_env_vars
from discord.ext import commands
import random
import csv
import os

load_env_vars()


def cargar_selecciones(ruta):
    selecciones = []
    with open(ruta) as archivo_selecciones:
        selecciones_reader = csv.reader(archivo_selecciones)
        for seleccion in selecciones_reader:
            selecciones.append((seleccion[0], seleccion[1]))
    return selecciones


selecciones = cargar_selecciones("src/selecciones.txt")


description = """Escuchen, corran la bola"""

intents = discord.Intents.default()
# intents.members = True  que carajos es esto???
intents.message_content = True  # esto creo que es para que pueda leer los mensajes

bot = commands.Bot(command_prefix="?", description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "selesion":
        seleccion, bandera = random.choice(selecciones)
        await message.channel.send(f"Mirá capo te toca jugar con {seleccion} {bandera}")


bot.run(os.environ.get("DISCORD_BOT_TOKEN"))
