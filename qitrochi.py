import os
import random
import time
from telethon.sync import TelegramClient, events
from telethon import events
from telethon.tl import functions
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
import asyncio
import sys

session_name = 'selfdestruct'
config_file = 'config.cfg'

if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        lines = f.read().splitlines()
    if len(lines) >= 2:
        api_id, api_hash = lines[:2]
    else:
        print("Заполните поля ниже.")
        print("🔎 Если вы незнаете где взять данные напишите в лс @ghosvx")
        api_id = input("Введите API ID: ")
        api_hash = input("Введите API Hash: ")
        with open(config_file, 'w') as f:
            f.write(api_id + '\n')
            f.write(api_hash + '\n')
        print("Готово! Эти данные не надо будет вводить в будущем.")

client = TelegramClient(session_name, api_id, api_hash).start()

photo_path = 'ava.jpg'

me = client.get_me()

print("  _. o _|_ ._ _   _ |_  o ")
print(" (_| |  |_ | (_) (_ | | | ")
print("   |                     ")
print(" V0.01b1")
print("Здраствуйте,", me.first_name, "!")
start_time = time.time()

@client.on(events.NewMessage(outgoing=True, pattern='Xping'))
async def ping_command(event):
    start_time = time.time()
    message = await event.respond('🚀 Проверяю пинг...')
    end_time = time.time()
    ping_time = (end_time - start_time) * 1000
    if ping_time < 152:
        emoji = '🟢'
    elif ping_time < 228:
        emoji = '🟡'
    else:
        emoji = '🔴'
    ping_text = f'{emoji} Пинг: `{ping_time:.2f}ms`'
    await message.edit(ping_text, parse_mode='markdown')

@client.on(events.NewMessage(outgoing=True, pattern='Xtime'))
async def time_command(event):
    args = event.message.message.split()[1:]
    if args:
        try:
            seconds = int(args[0])
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            await event.message.edit(f'Время: {hours} часов, {minutes} минут, {seconds} секунд')
        except ValueError:
            await event.message.edit('🚫 Ошибка: Некорректный аргумент')
    else:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await event.message.edit(f'Текущее время: {current_time}')

ava_count = 0
last_ava_count = 0

async def set_profile_photo(photo):
    await client(functions.photos.UploadProfilePhotoRequest(
        file=await client.upload_file(photo)
    ))

async def get_self_avatar():
    chat = await client.get_entity('self')
    photos = await client.get_profile_photos(chat)
    if photos:
        photo = photos[0]
        file_path = await client.download_media(photo, 'ava.jpg')
        return file_path
    else:
        print("Ирод у тебя нету аватарки!")
        return None

async def update_message(event):
    global ava_count, last_ava_count
    while True:
        if ava_count != last_ava_count:
            await event.message.edit(f'❤ Установлено аватарок: {ava_count}')
            last_ava_count = ava_count
        await asyncio.sleep(20)

@client.on(events.NewMessage(outgoing=True, pattern='Xava'))
async def ava_command(event):
    global ava_count
    message = await event.message.edit('🩻 Ожидайте скачиваем вашу аватарку... Это может занять достаточно времени.')    
    await get_self_avatar()
    message = await event.message.edit('🔶 Начинаю установку аватарок...')
    asyncio.create_task(update_message(event))
    while True:
        await set_profile_photo(photo_path)
        ava_count += 1
        print(f"Установил {ava_count}-ую аватарку!")
        await message.edit(f'❤ Установлено аватарок: {ava_count}')
        await asyncio.sleep(3)
        await set_profile_photo(photo_path)
        ava_count += 1
        print(f"Установил {ava_count}-ую аватарку!")
        await message.edit(f'❤ Установлено аватарок: {ava_count}')
        await asyncio.sleep(3)
        await set_profile_photo(photo_path)
        ava_count += 1        
        print(f"Установил {ava_count}-ую аватарку!")      
        await message.edit(f'❤ Установлено аватарок: {ava_count}')
        await asyncio.sleep(3)
        await asyncio.sleep(random.randint(100, 260))

@client.on(events.NewMessage(outgoing=True, pattern='Xuptime'))
async def uptime_command(event):
    global start_time
    current_time = time.time()
    uptime_seconds = int(current_time - start_time)
    uptime_hours = uptime_seconds // 3600
    uptime_minutes = (uptime_seconds % 3600) // 60
    uptime_seconds = uptime_seconds % 60
    await event.message.edit(f'💿 Время работы бота: {uptime_hours}:{uptime_minutes}:{uptime_seconds}')

@client.on(events.NewMessage(outgoing=True, pattern='Xinfo'))
async def info_command(event):
    info_text = f"""
🎀 qitrochi
🪧 Префикс <X>
🌐 Версия 0.01

😎 Владелец @{me.username}
🧑‍💻 Автор @ghosvx
    """
    await event.respond(info_text, parse_mode='markdown')

@client.on(events.NewMessage(outgoing=True, pattern='Xrestart'))
async def restart_command(event):
    await event.respond('🔄 Перезапускаю селф бота...')
    python = sys.executable
    os.execl(python, python, *sys.argv)

@client.on(events.NewMessage(outgoing=True, pattern='Xstop'))
async def shutdown_command(event):
    await event.respond('Надеюсь еще увидимся!')
    await client.disconnect()

@client.on(events.NewMessage(outgoing=True, pattern='Xhelp'))
async def help_command(event):
    help_text = """
🆘 Список доступных команд:
- `Xping`: Проверка пинга.
- `Xtime [секунды]`: Вывод текущего времени или времени, прошедшего с указанного количества секунд.
- `Xava`: Зацикливает установку вашей аватарки.
- `Xuptime`: Время работы бота.
- `Xinfo`: Информация о боте и его создателе.
- `Xrestart`: Перезапуск бота.
- `Xstop`: Остановка работы бота.
    """
    await event.respond(help_text, parse_mode='markdown')

client.run_until_disconnected()
