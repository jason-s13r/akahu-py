import click

from akahu.cli.refresh import refresh
from akahu.cli.tokens import tokens
from akahu.cli.me import me
from akahu.cli.account import account
from akahu.cli.transactions import transactions


@click.group()
def cli():
    """Akahu CLI."""
    pass


cli.add_command(tokens)
cli.add_command(me)
cli.add_command(account)
cli.add_command(transactions)
cli.add_command(refresh)
