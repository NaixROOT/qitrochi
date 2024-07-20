import time
from telethon import events

def register_uptime_command(client, start_time):
    @client.on(events.NewMessage(outgoing=True, pattern='Xuptime'))
    async def uptime_command(event):
        current_time = time.time()
        uptime_seconds = int(current_time - start_time)
        uptime_hours = uptime_seconds // 3600
        uptime_minutes = (uptime_seconds % 3600) // 60
        uptime_seconds = uptime_seconds % 60
        await event.message.edit(f'💿 Время работы бота: {uptime_hours}:{uptime_minutes}:{uptime_seconds}')
