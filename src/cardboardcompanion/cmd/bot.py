import logging
import click

import cardboardcompanion.bot as companion

logger = logging.getLogger(__name__)


@click.group()
def bot():
    return


@bot.command()
def start():
    logger.info("Starting up your cardboard companion!")

    companion.Start()
