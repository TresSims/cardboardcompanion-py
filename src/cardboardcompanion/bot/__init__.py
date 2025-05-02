import logging

import discord
from cardboardcompanion import cfg
# from .slash_commands import commands

logger = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot()


@bot.event
async def on_ready():
    logger.info(f"Your friend {bot.user} is here!")
    # await bot.register_commands(commands)
    print(f"Your friend {bot.user} is here!")


def Start():
    logger.info(f"Starting cardboard companion with token {cfg.values.token}")
    bot.run(cfg.values.token)


@bot.command(description="A description")
async def pong(ctx):
    await ctx.respond("ping")
