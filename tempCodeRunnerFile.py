import discord
from discord import intents

# Replace BOT_TOKEN with your bot's token
BOT_TOKEN = "MTA1MTE4ODU5MDAxODgyMjE3NA.G-tHPP.y70l4T7NRGWpkossRLRp5hGp7tq7P2u1XJ_Ia8"

# Replace CHANNEL_ID with the ID of the channel you want to send the message to
CHANNEL_ID = 684006775602544715

intents = intents.DefaultIntents()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("James is Short")

client.run(BOT_TOKEN)
