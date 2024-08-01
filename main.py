import os
import discord
from discord.ext import commands
from discord import app_commands
from server import server_on

token = os.getenv("TOKEN") or ""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("bot online !!")
    synced = await bot.tree.sync()
    print(f"{len(synced)}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 

    if message.content == 'hello':
        print("has messaged")
        await message.channel.send("Hello good luck!")

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx, arg):
    await ctx.send(arg)

@bot.tree.command(name="hollow", description="Say hi to the bot")
async def hi(interaction:discord.Interaction):
    await interaction.response.send_message("Hi!")
    
@bot.tree.command(name="mannu",description="Mannu is a good boy")
async def mannufast(interaction:discord.Interaction):
    await interaction.response.send_message("Hi!")

server_on()
bot.run(token)