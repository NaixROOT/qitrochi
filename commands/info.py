from telethon import events

def register_info_command(client, me):
    @client.on(events.NewMessage(outgoing=True, pattern='Xinfo'))
    async def info_command(event):
        info_text = f"""
<b>🎀 qitrochi</b>
<b>🪧 Префикс:</b> <code>X</code>
<b>🌐 Версия:</b> <code>0.01</code>

<b>😎 Владелец:</b> @{me.username}
        """
        await event.edit(info_text, parse_mode='html')
