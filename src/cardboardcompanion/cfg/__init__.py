from os import PathLike, getenv
from .defaults import CardboardConfig
import yaml

import logging

logger = logging.getLogger(__name__)


def import_config() -> CardboardConfig:
    global values, cfg_file

    tmp_cfg: dict = {}

    if cfg_file:
        logger.info(f"Reading config from {cfg_file}")
        with open(cfg_file, "r") as cfg_file_stream:
            tmp_cfg = yaml.safe_load(cfg_file_stream)

    for field in CardboardConfig.model_fields:
        value = getenv(f"CC_{field.upper()}", "")
        if value != "":
            logger.info(f"Overwriting {field} from config with environment variable")
            tmp_cfg[field] = value

    values = CardboardConfig(**tmp_cfg)
    return values


values: CardboardConfig
cfg_file: PathLike
