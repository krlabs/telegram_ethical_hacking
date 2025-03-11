#
# Цей Python-скрипт на базі Telethon отримує з облікового запису користувача особисті повідомлення, відправлені службою Telegram.
# Таким чином можна прочитати коди активації і відновити доступ до облікового запису, доступ до якого було втрачено. Навіть якщо ви не маєте доступу до прив'язаного мобільного номера (наприклад, реєструвади колись на віртуальний).
# Але, щоб це спрацювало - попередньо в обліковому записі повинна бути налаштована конфігурація API ID & API HASH для здійснення авторизації через Telegram API (отримується через створення додатку в my.telegram.org/apps). #
#

from telethon import TelegramClient

# Дані для авторизації
api_id = xxxxxxxxxxx
api_hash = 'xxxxxxxxxxxxxxxxxx'
phone_number = '+xxxxxxxxxxxxxx'

# Ініціалізація TelegramClient
client = TelegramClient('list_chats_session', api_id, api_hash)

async def main():
    # Отримуємо всі діалоги (чати, в тому числі особисті)
    dialogs = await client.get_dialogs()

    # Шукаємо чат з Telegram (особистий, а не канал)
    telegram_chat = None
    for dialog in dialogs:
        if dialog.name == "Telegram" and not dialog.is_channel:  # Уникаємо каналу
            telegram_chat = dialog
            break

    if telegram_chat:
        messages = await client.get_messages(telegram_chat, limit=10)  # Отримуємо 10 останніх повідомлень
        for msg in messages:
            print(msg.text)  # Виводимо текст повідомлення
    else:
        print("Чат з Telegram не знайдено!")

# Запускаємо клієнт і виконуємо головну функцію
with client:
    client.loop.run_until_complete(main())
