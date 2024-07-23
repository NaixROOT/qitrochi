import os
import time
import sys
from telethon.sync import TelegramClient
from config import get_config
from commands import register_all_commands
from helpers import set_profile_photo, get_self_avatar, update_message
from commands.misc import miscqit

session_name = 'selfdestruct'
config_file = 'config.cfg'

api_id, api_hash = get_config(config_file)


client = TelegramClient(session_name, api_id, api_hash).start()

me = client.get_me()

print("  _. o _|_ ._ _   _ |_  o ")
print(" (_| |  |_ | (_) (_ | | | ")
print("   |                     ")
print(" V1337 (Hacked By Naix)")
print("Здраствуйте,", me.first_name, "!")
start_time = time.time()
miscqit()

register_all_commands(client, start_time, me)

client.run_until_disconnected()
