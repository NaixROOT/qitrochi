import asyncio
from telethon.tl import functions

async def set_profile_photo(client, photo):
    await client(functions.photos.UploadProfilePhotoRequest(
        file=await client.upload_file(photo)
    ))

async def get_self_avatar(client):
    chat = await client.get_entity('self')
    photos = await client.get_profile_photos(chat)
    if photos:
        photo = photos[0]
        file_path = await client.download_media(photo, 'ava.jpg')
        return file_path
    else:
        print("Ирод у тебя нету аватарки!")
        return None

async def update_message(event, ava_count, last_ava_count):
    while True:
        if ava_count != last_ava_count:
            await event.message.edit(f'❤ Установлено аватарок: {ava_count}')
            last_ava_count = ava_count
        await asyncio.sleep(20)
