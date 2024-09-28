import discord
import random
import os
print(os.listdir('imagenes'))
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def coin(ctx):
    await ctx.send(f'flip_coin()')

@bot.command()
async def coin(ctx):
    await ctx.send(f'flip_coin()')

@bot.command()
async def suerte(ctx):
    x = random.randint(1,2)
    await ctx.send(x)
    if x == 1:
        await ctx.send(f'¡Ho! perdiste')
    else:
        await ctx.send(f'¡eee! ganaste')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('images/meme.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def lista_de_memes(ctx):
    carpeta=os.listdir("img")
    meme = random.choice(carpeta)
    with open(f'images/{meme.jpeg}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

bot.run("token")
