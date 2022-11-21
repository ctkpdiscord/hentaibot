import discord
from discord import commands
import requests


token = ""
prefix = "h!"
commandlist = ["hass", "hmidriff", "pgif", "4k", "hentai", "hneko", "neko", "hkitsune", "kemonomimi", "anal", "hanal", "gonewild", "kanna", "ass", "pussy", "thigh", "hthigh",  "paizuri", "tentacle", "boobs", "hboobs", "yaoi"]

bot = commands.Bot(command_prefix="h!",intents=intents)

async def genimage(ctx,type)
  image = requests.get("https://nekobot.xyz/api/image", headers={
                        "User-Agent": "NekoBotAPI-py/1.0",
                        "Authorization": ""
                        },params={"type": type}).json()["message"]
  embed = discord.Embed(title="Hentai Image")
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

  
@bot.event
async def on_connect():
  print("起動完了")

@bot.listen("on_message")
async def cmdcommands(message):
  if message.content[:3] == "h!":
    if message.content == "h!help":
      embed = discord.Embed(title="HentaiHelp",description="\n".join("h!"+i for i in command))
      await ctx.send(embed=embed)
      return
    for command in commandlist:
      if message.content[3:] == command:
        await genimage(ctx,command)
        return

bot.run(token)
