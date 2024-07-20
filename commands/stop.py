from telethon import events

def register_stop_command(client):
    @client.on(events.NewMessage(outgoing=True, pattern='Xstop'))
    async def shutdown_command(event):
        await event.edit('Надеюсь еще увидимся!')
        await client.disconnect()
