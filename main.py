import requests
from discord.ext import commands

TOKEN = ""

client = commands.Bot(command_prefix='$', self_bot=True)

@client.command(name="kidnap")
async def emoji(ctx, emoji, name):
    if ctx.guild.id != 1192800308296953926:
        return
    split = emoji.split(":")
    emoji_ID = split[2].replace(">", "")
    url = "https://cdn.discordapp.com/emojis/{}.gif".format(emoji_ID)
    r = requests.get(url)
    if r.status_code == 415:
        url = "https://cdn.discordapp.com/emojis/{}.png".format(emoji_ID)
        r = requests.get(url)
    image = r.content
    await ctx.guild.create_custom_emoji(name=name, image=image)
    emojis = ctx.guild.emojis
    for e in emojis:
        emoji = f"<:{e.name}:{e.id}>"
    msg = await ctx.reply(f"Succesfully created emoji {emoji} and named it {name}")
    await msg.add_reaction(f"{e.name}:{e.id}")

client.run(TOKEN)
