import os
import sys
from telethon import events

def register_restart_command(client):
    @client.on(events.NewMessage(outgoing=True, pattern='Xrestart'))
    async def restart_command(event):
        await event.edit('🔄 Перезапускаю селф бота...')
        python = sys.executable
        os.execl(python, python, *sys.argv)
