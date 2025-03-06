# chatinfo.py
#
# Скрипт на базі Telegram API і Telethon для збору детальної інформації по чату/ресурсу (get_info_telegram_resouce).
# На виході отримуємо в командний рядок технічну інформацію (у форматі структури): id, title, photo, date, creator та інші. 
# Дані API ID та API HASH беруться з додатку, який створюється тут: https://my.telegram.org/auth?to=apps
# Номер телефону вказуєте зі свого облікового запису.
#

from telethon.sync import TelegramClient

# Дані для авторизації
api_id = xxxxxx
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
phone_number = '+xxxxxxxxxxxxxx'

# Вкажіть ID або юзернейм чату
chat_id = -xxxxxxxxxxxxx  # Замініть на ID чату який треба проаналізувати

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
