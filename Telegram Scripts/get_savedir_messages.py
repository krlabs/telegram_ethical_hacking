#
# Читаємо папку Saved з облікового запису через API Telegram.
#

from telethon import TelegramClient

# Дані для авторизації
api_id = xxxxxxxx
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxx'
phone_number = '+xxxxxxxxxxxxxx'

# Ініціалізація TelegramClient
client = TelegramClient('list_chats_session', api_id, api_hash)

async def main():
    me = await client.get_me()
    saved = await client.get_entity('me')  # Saved Messages — це чат з собою
    messages = await client.get_messages(saved, limit=10)

    for msg in messages:
        print(msg.text)

with client:
    client.loop.run_until_complete(main())
