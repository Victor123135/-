# Імпортування discord.py
import discord
# Дозволяє зробити HTTP - запит
import requests
# Полегшує роботу з повернутими даними
import json
# Випадковим чином вибирає повідомлення зі списку
import random

# Створення зв'язку з Discord
client = discord.Client()

# Сумні слова
sad_words = ["сумний", "пригнічений", "нещасний", "злий"]

# Обнадійливі повідомлення
starter_encouragements = [
    "Підбадьорся!",
    "Тримайся там.",
    "Ви чудова людина / bot!"
]


# Використанння модулю запиту для API
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text) # Переклад із файлу JSON в рядковий формат
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event # Використовується для реєстрації події
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) # Тут виводить повідомлення про успішне підключення бота


@client.event
async def on_message(message):
    if message.author == client.user: # якщо повідомлення написане від самого себе. Тоді ця умова виконується.
        return

    msg = message.content

    if msg.startswith('$inspire'): # Якщо прописати команду то виведеться цитата
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words): # Прописавши сумні слова виведеться підбадьорюючі повідомлення
        await message.channel.send(random.choice(starter_encouragements))


client.run('ODQ3NTA1NTE2NzE5NzY3NjM2.YK_DBQ.HCNM0_HsTCMaWVpFTbwOlKjn41o') # Запуск бота
