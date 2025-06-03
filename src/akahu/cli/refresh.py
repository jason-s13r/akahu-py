import click

from akahu.client import Client
from akahu.cli.utils import get_tokens


@click.command("refresh")
def refresh():
    """Get current user."""
    app_token, user_token = get_tokens()

    api = Client(Client.Config(app_token, user_token))
    success = api.refresh.all()

    print(f"Refresh request successful: {success}")
