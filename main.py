import discord
import requests
import json
import random

client = discord.Client(intents=discord.Intents.default())

sad_words = ["kotu", "iyi degilim", "moralim bozuk", "tartistik", "istemiyorum", "iyi gitmiyor", "ekonomi"]

starter_happys = ["heyy bazen kafana fazla takiyosun", "bosverrrr", "en kotu gunumuz boyle olsun", "her sey duzelecek", "sadece biraz zamana ihtiyacin var", "bir sure dusunmemeye calis", "en iyi terapi hareket etmek"]


def get_quote():
    response = requests.get("https://g.tenor.com/v1/search?q=excited&key=LIVDSRZULELA&limit=8")
    json_data = response.json()
    quote = json_data['results'][0]['media'][0]['loopedmp4']['url']
    return quote

@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hehehe'):
        quote = get_quote()
        await message.channel.send(quote)

    for item in sad_words:
        if item in message.content:
            await message.channel.send(random.choice(starter_happys))

    if message.content.startswith('$heyfolks'):
        await message.channel.send('Hiee!')



TOKEN = ''
client.run(TOKEN)