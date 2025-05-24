import click

from akahu.cli.utils import clear_tokens, set_tokens


@click.group("tokens")
def tokens():
    pass


@tokens.command("set")
def set_command():
    """Set tokens."""
    app_token = click.prompt("App token")
    user_token = click.prompt("User token")
    set_tokens(app_token, user_token)
    click.echo("Tokens saved.")


@tokens.command("clear")
def clear_command():
    clear_tokens()
    click.echo("Tokens removed.")
