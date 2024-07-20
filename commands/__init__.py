from .ping import register_ping_command
from .time import register_time_command
from .ava import register_ava_command
from .uptime import register_uptime_command
from .info import register_info_command
from .restart import register_restart_command
from .stop import register_stop_command
from .help import register_help_command

def register_all_commands(client, start_time, me):
    register_ping_command(client)
    register_time_command(client)
    register_ava_command(client)
    register_uptime_command(client, start_time)
    register_info_command(client, me)
    register_restart_command(client)
    register_stop_command(client)
    register_help_command(client)
