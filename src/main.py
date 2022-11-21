import discord,requests,json,random
from discord.ext import commands
jsondata = json.load(open("./config/config.json","r"))


token = jsondata["TOKEN"]
prefix = jsondata["PREFIX"]
proxy = jsondata["proxysetting"]["proxyset"]
proxys = jsondata["proxysetting"]["proxys"]

commandlist = ["hass", "hmidriff", "pgif", "4k", "hentai", "hneko", "neko", "hkitsune", "kemonomimi", "anal", "hanal", "gonewild", "kanna", "ass", "pussy", "thigh", "hthigh",  "paizuri", "tentacle", "boobs", "hboobs", "yaoi"]
intents = discord.Intents.default()
#intents.message_content = True
bot = commands.Bot(command_prefix=prefix,intents=intents)
bot.remove_command("help")

async def genimage(ctx,type):
  if proxy:
    proxies = {"https": random.choice(proxys)}
  else:
    proxies = None
  image = requests.get("https://nekobot.xyz/api/image", headers={
                        "User-Agent": "NekoBotAPI-py/1.0",
                        "Authorization": ""
                        },params={"type": type},proxies=proxies).json()["message"]
  embed = discord.Embed(title="Hentai Image")
  embed.set_image(url=image)
  await ctx.channel.send(embed=embed)


@bot.event
async def on_connect():
  print("起動完了")

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="This is HentaiBot",description="\n".join(prefix+i for i in commandlist))
  await ctx.send(embed=embed)

@bot.listen("on_message")
async def cmdcommands(message):
  for command in commandlist:
    if message.content == prefix+command:
      await genimage(message,command)
      return


bot.run(token)
