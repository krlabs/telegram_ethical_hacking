# getchannels.py
#
# Скрипт отримує список доступних для парсингу Telegram-ресурсів в обліковому записі користувача (get_telegram_resources_lists): чати, канали, групи, юзери.
# На виході отримуємо в командний рядок список всіх чатів в форматі: Chat: Telegram | ID: 777000 | Type: User.
# За бажанням можна доробити скрипт і додати експорт в таблиці (.xlsx).
# Дані API ID та API HASH беруться з додатку, який створюється тут: https://my.telegram.org/auth?to=apps
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
        # Додатково, якщо хочете побачити більше атрибутів у вигляді технічних характеристик каналів в JSON
        # print(dialog.stringify())

with client:
    # Авторизація
    client.start(phone=phone_number)
    # Запуск основної функції
    client.loop.run_until_complete(main())
