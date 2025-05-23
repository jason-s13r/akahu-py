from pathlib import Path

from xdg_base_dirs import xdg_config_home

AKAHU_DEFAULT_RATE_LIMIT = 200
AKAHU_DEFAULT_RATE_LIMIT_PERIOD = 60
AKAHU_DEFAULT_RETRY_LIMIT = 8


def config_directory() -> Path:
    directory = xdg_config_home() / "akahu"
    directory.mkdir(exist_ok=True, parents=True)
    return directory


def config_file() -> Path:
    return config_directory() / "config.shelf"
