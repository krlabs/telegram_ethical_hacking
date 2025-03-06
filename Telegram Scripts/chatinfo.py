# Отримати інформацію по чату (get_info_telegram_resouce)

from telethon.sync import TelegramClient

# Дані для авторизації
api_id = xxxxxx
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
phone_number = '+xxxxxxxxxxxxxx'

# Вкажіть ID або юзернейм чату
chat_id = -100xxxxxxxxxx  # Замініть на ID чату який треба проаналізувати

client = TelegramClient('chat_info_session', api_id, api_hash)

async def main():
    try:
        # Отримуємо інформацію про чат
        chat = await client.get_entity(chat_id)
        print("Chat information:")
        print(chat.stringify())  # Виведе всю доступну інформацію про чат
    except Exception as e:
        print(f"Error: {e}")

with client:
    # Авторизація
    client.start(phone=phone_number)
    # Запуск основної функції
    client.loop.run_until_complete(main())
