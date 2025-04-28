import click
from cardboardcompanion import cfg as config
import logging

from .bot import bot

logger = logging.getLogger(__name__)


@click.group()
@click.option("--cfg", default="./cardboardcompanion.yml", type=click.Path(exists=True))
def ccompanion(cfg):
    if cfg:
        config.cfg_file = cfg

    logger.info("Reading config...")
    print("Reading config.")
    config.import_config()


ccompanion.add_command(bot)
