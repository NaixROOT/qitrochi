import asyncio
import random
from telethon import events
from telethon.errors import FloodWaitError
from helpers import set_profile_photo, get_self_avatar, update_message

def format_time(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    parts = []
    if days > 0:
        parts.append(f"{days} дн.")
    if hours > 0:
        parts.append(f"{hours} ч.")
    if minutes > 0:
        parts.append(f"{minutes} мин.")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} сек.")
    return ' '.join(parts)

def register_ava_command(client):
    ava_count = 0
    last_ava_count = 0

    @client.on(events.NewMessage(outgoing=True, pattern='Xava'))
    async def ava_command(event):
        nonlocal ava_count
        message = await event.message.edit('🩻 Ожидайте, скачиваем вашу аватарку... Это может занять некоторое время.')
        await get_self_avatar(client)
        message = await event.message.edit('🔶 Начинаю установку аватарок...')
        asyncio.create_task(update_message(event, ava_count, last_ava_count))

        while True:
            try:
                await set_profile_photo(client, 'ava.jpg')
                ava_count += 1
                print(f"Установил {ava_count}-ую аватарку!")
                await message.edit(f'❤ Установлено аватарок: {ava_count}')
                await asyncio.sleep(3)
            except FloodWaitError as e:
                wait_time = e.seconds
                formatted_time = format_time(wait_time)
                await message.edit(f'🚫 Обнаружен флуд-вейт! Ожидание {formatted_time}...')
                print(f'Обнаружен флуд-вейт! Ожидание {formatted_time}...')
                await asyncio.sleep(wait_time)

            try:
                await set_profile_photo(client, 'ava.jpg')
                ava_count += 1
                print(f"Установил {ava_count}-ую аватарку!")
                await message.edit(f'❤ Установлено аватарок: {ava_count}')
                await asyncio.sleep(3)
            except FloodWaitError as e:
                wait_time = e.seconds
                formatted_time = format_time(wait_time)
                await message.edit(f'🚫 Обнаружен флуд-вейт! Ожидание {formatted_time}...')
                print(f'Обнаружен флуд-вейт! Ожидание {formatted_time}...')
                await asyncio.sleep(wait_time)

            try:
                await set_profile_photo(client, 'ava.jpg')
                ava_count += 1
                print(f"Установил {ava_count}-ую аватарку!")
                await message.edit(f'❤ Установлено аватарок: {ava_count}')
                await asyncio.sleep(3)
            except FloodWaitError as e:
                wait_time = e.seconds
                formatted_time = format_time(wait_time)
                await message.edit(f'🚫 Обнаружен флуд-вейт! Ожидание {formatted_time}...')
                print(f'Обнаружен флуд-вейт! Ожидание {formatted_time}...')
                await asyncio.sleep(wait_time)

            await asyncio.sleep(random.randint(100, 260))

