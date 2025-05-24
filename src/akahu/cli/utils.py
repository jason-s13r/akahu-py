from pathlib import Path
import shelve

from xdg_base_dirs import xdg_config_home


def config_directory() -> Path:
    directory = xdg_config_home() / "akahu"
    directory.mkdir(exist_ok=True, parents=True)
    return directory


def config_file() -> Path:
    return config_directory() / "config.shelf"


def set_tokens(app_token: str, user_token: str) -> None:
    config = config_file()

    with shelve.open(config, writeback=True) as db:
        db["app_token"] = app_token
        db["user_token"] = user_token
        db.close()


def get_tokens() -> tuple[str, str]:
    config = config_file()

    with shelve.open(config) as db:
        app_token = db.get("app_token", "")
        user_token = db.get("user_token", "")
        db.close()

    return app_token, user_token


def clear_tokens():
    config = config_file()

    with shelve.open(config, writeback=True) as db:
        db.clear()
        db.close()
