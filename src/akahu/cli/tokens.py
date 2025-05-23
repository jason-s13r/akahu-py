import click
import shelve

from akahu.utils import config_file


@click.group("tokens")
def tokens():
    pass


@tokens.command("set")
def set_tokens():
    """Set tokens."""
    app_token = click.prompt("App token")
    user_token = click.prompt("User token")
    config = config_file()

    with shelve.open(config, writeback=True) as db:
        db["app_token"] = app_token
        db["user_token"] = user_token
        db.close()

    click.echo("Tokens saved.")


@tokens.command("clear")
def clear_tokens():
    """Clear tokens."""
    config = config_file()

    with shelve.open(config, writeback=True) as db:
        db.clear()
        db.close()

    click.echo("Tokens cleared.")
