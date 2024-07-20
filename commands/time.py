from datetime import datetime
from telethon import events

def register_time_command(client):
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
