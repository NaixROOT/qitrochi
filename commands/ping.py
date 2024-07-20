import time
from telethon import events

def register_ping_command(client):
    @client.on(events.NewMessage(outgoing=True, pattern='Xping'))
    async def ping_command(event):
        start_time = time.time()
        message = await event.edit('🚀 Проверяю пинг...')
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
