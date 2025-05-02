import logging

from discord.ext import commands
from cardboardcompanion import cfg
from .slash_commands import SlashCommandsCog

logger = logging.getLogger(__name__)

bot = commands.Bot()


@bot.event
async def on_ready():
    logger.info(f"Your friend {bot.user} is here!")
    bot.add_cog(SlashCommandsCog(bot))
    print(f"Your friend {bot.user} is here!")


def Start():
    logger.info(f"Starting cardboard companion with token {cfg.values.token}")
    bot.run(cfg.values.token)
