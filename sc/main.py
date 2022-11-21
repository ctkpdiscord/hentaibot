import discord
from discord import commands
import requests


token = ""
prefix = "h!"
bot = commands.Bot(command_prefix="h!",intents=intents)

@bot.event
async def on_connect():
  print("起動完了")
command = ["hass", "hmidriff", "pgif", "4k", "hentai", "hneko", "neko", "hkitsune", "kemonomimi", "anal", "hanal", "gonewild", "kanna", "ass", "pussy", "thigh", "hthigh",  "paizuri", "tentacle", "boobs", "hboobs", "yaoi"]
@bot.listen("on_message")
async def cmdcommands(message):
  if message.content[:3] == "h!":
    if message.content[3:]:
  if message.content == prefix+"hentai":
    image = requests.get("https://nekobot.xyz/api/image", headers={
                        "User-Agent": "NekoBotAPI-py/1.0",
                        "Authorization": ""
                        },params={"type": "hentai"}).json()["message"]
  elif message.content == prefix+"anal":
    image = requests.get("https://nekobot.xyz/api/image", headers={
                        "User-Agent": "NekoBotAPI-py/1.0",
                        "Authorization": ""
                        },params={"type": "anal"}).json()["message"]
  elif message.content == prefix+"anal":
    image = requests.get("https://nekobot.xyz/api/image", headers={
                        "User-Agent": "NekoBotAPI-py/1.0",
                        "Authorization": ""
                        },params={"type": "anal"}).json()["message"]
  embed = discord.Embed(title="Hentai Image")
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)


bot.run(token)
