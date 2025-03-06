#
# Отримати список найактивніших учасників чату Telegram на основі останніх 1000 повідомлень (якщо він відкритий) (get_active_participants)
# Ліміт кількості повідомлень можна змінити.
# На виході отримуємо вивід у командний рядок зі списком учасників в форматі: User: Name (@username) - ID: xxxxxxxxxx
# Скрипт можна доробити й додати експорт в таблиці (xlsx).
#

from telethon.sync import TelegramClient

# Дані для авторизації
api_id = xxxxxxxxxxxx
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxx'
phone_number = '+xxxxxxxxxxx'

# ID або юзернейм чату
chat_id = xxxxxxxxxx # Замініть на ID чату

client = TelegramClient('messages_session', api_id, api_hash)

async def main():
    try:
        # Отримуємо об'єкт чату
        chat = await client.get_entity(chat_id)
        print(f"Chat title: {chat.title}")

        # Завантажуємо повідомлення та збираємо унікальних авторів
        print("Fetching messages...")
        authors = set()
        async for message in client.iter_messages(chat, limit=1000):  # Замініть limit за потреби
            if message.sender_id:
                authors.add(message.sender_id)

        print(f"Found {len(authors)} unique users who sent messages.")

        # Виводимо авторів
        with open('active_users_list.txt', 'w', encoding='utf-8') as file:
            for user_id in authors:
                try:
                    user = await client.get_entity(user_id)
                    if hasattr(user, 'first_name'):  # Перевірка, чи це користувач, а не канал
                        username = f"@{user.username}" if user.username else "No username"
                        first_name = user.first_name or "No first name"
                        last_name = user.last_name or "No last name"
                        telegram_id = user.id  # Додаємо Telegram ID
                        
                        # Вивід у консоль
                        print(f"User: {first_name} {last_name} ({username}) - ID: {telegram_id}")
                        
                        # Запис у файл
                        file.write(f"{first_name} {last_name} ({username}) - ID: {telegram_id}\n")
                    else:
                        print(f"Channel or bot: {user.title} ({user.id})")
                        file.write(f"Channel or bot: {user.title} ({user.id})\n")
                except Exception as e:
                    print(f"Error processing user {user_id}: {e}")
    except Exception as e:
        print(f"Error: {e}")

with client:
    client.start(phone=phone_number)
    client.loop.run_until_complete(main())
 
