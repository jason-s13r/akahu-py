import click
from click_extra.tabulate import render_table

from akahu.client import Client
from akahu.models.user import User
from akahu.cli.utils import get_tokens


@click.command("me")
def me():
    """Get current user."""
    app_token, user_token = get_tokens()

    api = Client(Client.Config(app_token, user_token))
    user: User = api.me.get()

    row = [
        user.email,
        user.preferred_name,
        user.access_granted_at,
        user.mobile,
        user.first_name,
        user.last_name,
        user.id,
    ]

    headers = [
        "Email",
        "Preferred Name",
        "Access Granted At",
        "Mobile",
        "First Name",
        "Last Name",
        "ID",
    ]

    render_table(
        [row],
        headers=headers,
        tablefmt="fancy_grid",
    )
