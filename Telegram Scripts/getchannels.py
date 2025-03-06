# getchannels.py
#
# Скрипт на базі Telegram API і Telethon отримує список доступних для парсингу Telegram-ресурсів в обліковому записі користувача (get_telegram_resources_lists): чати, канали, групи, юзери.
# На виході отримуємо в командний рядок список всіх чатів в форматі: Chat: Telegram | ID: 777000 | Type: User.
# За бажанням можна доробити скрипт і додати експорт в таблиці (.xlsx).
# Дані API ID та API HASH беруться з додатку, який створюється тут: https://my.telegram.org/auth?to=apps
# Номер телефону вказуєте зі свого облікового запису.
#

from telethon.sync import TelegramClient

# Дані для авторизації
api_id = xxxxxx
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
phone_number = '+xxxxxxxxxxxxxx'

# Ініціалізація TelegramClient
client = TelegramClient('list_chats_session', api_id, api_hash)

async def main():
    print("Fetching available chats...\n")
    async for dialog in client.iter_dialogs():
        print(f"Chat: {dialog.name} | ID: {dialog.id} | Type: {type(dialog.entity).__name__}")
        # Додатково, якщо хочете побачити технічну інформацію для кожного каналу в структурованому форматі
        # print(dialog.stringify())

with client:
    # Авторизація
    client.start(phone=phone_number)
    # Запуск основної функції
    client.loop.run_until_complete(main())
