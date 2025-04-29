import discord
from typing import List
from .cmds.ping import PingCommand


commands: List[discord.SlashCommand] = [PingCommand]


def register(bot, guild_id):
    global commands
    for command in commands:
        bot.register_command(command, guild_ids=[guild_id])
