# exportchat.py
#
# Скрипт на базі Telegram API і Telethon для експрорту історії повідомлень в відкритому публічному чаті Telegram.
# На виході отримуємо в файл xlsx такі колонки: Chat ID, Chat Name, User ID, User Info, Message ID, Message. 
# API ID та API HASH беруться з додатку, який створюється тут: https://my.telegram.org/auth?to=apps
# Номер телефону вказуєте зі свого облікового запису (не бота).
#

from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel
import pandas as pd

# Дані для авторизації
api_id = xxxxxxxxxxxxxx
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
phone_number = 'xxxxxxxxxxxxxxxxx'

# ID або юзернейм чату
chat_id = -100xxxxxxxxxx  # Замініть на ваш ID чату

client = TelegramClient('export_chat_session', api_id, api_hash)

async def main():
    try:
        # Отримуємо об'єкт чату
        chat = await client.get_entity(chat_id)
        print(f"Chat title: {chat.title}")
        
        # Ліст для збереження даних
        data = []
        
        # Завантажуємо всі повідомлення (можна змінити limit)
        print("Fetching messages...")
        async for message in client.iter_messages(chat, limit=None):  # Завантажуємо всі повідомлення
            # Перевіряємо, чи є у повідомлення автора
            if message.sender_id:
                try:
                    user = await client.get_entity(message.sender_id)
                    username = f"@{user.username}" if user.username else "No username"
                    first_name = user.first_name or "No first name"
                    last_name = user.last_name or "No last name"
                    user_info = f"{first_name} {last_name} ({username})"
                except:
                    user_info = "Deleted Account"
            else:
                user_info = "Unknown"

            # Додаємо дані в список
            data.append({
                "Chat ID": chat.id,
                "Chat Name": chat.title,
                "User ID": message.sender_id,
                "User Info": user_info,
                "Message ID": message.id,
                "Message": message.text or "Media/Other"
            })
        
        # Зберігаємо дані у файл Excel
        print("Saving to Excel...")
        df = pd.DataFrame(data)
        df.to_excel("chat_export.xlsx", index=False)
        print("Export completed! Data saved to chat_export.xlsx.")
    
    except Exception as e:
        print(f"Error: {e}")

with client:
    client.start(phone=phone_number)
    client.loop.run_until_complete(main())
