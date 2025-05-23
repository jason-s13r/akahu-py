from functools import reduce
from typing import List
import click
from click_extra.tabulate import render_table
import shelve
import math

from akahu.client import Client as AkahuClient
from akahu.models.account import Account, AccountStatus, AccountType
from akahu.utils import config_file


@click.group("account")
def account():
    """Account commands."""
    pass


@account.command("list")
@click.option(
    "--account-type", type=click.Choice(AccountType), help="Account types to filter by."
)
@click.option("--currency", type=click.STRING, help="Currency to filter by.")
@click.option(
    "--show-inactive", is_flag=True, default=False, help="Show inactive accounts."
)
def list_accounts(account_type: AccountType, currency: str, show_inactive: bool):
    """List accounts."""

    app_token = None
    user_token = None
    with shelve.open(config_file(), writeback=False) as db:
        app_token = db.get("app_token")
        user_token = db.get("user_token")

    api = AkahuClient(app_token, user_token)
    accounts: List[Account] = api.accounts.list()

    def account_row(account: Account) -> List:
        row = [
            account.connection.name,
            account.name,
            account.type.value,
            account.formatted_account,
            account.balance.currency,
            account.balance.current,
            account.balance.available,
        ]

        if show_inactive:
            row + [account.status]

        return row

    headers = [
        "Provider",
        "Name",
        "Type",
        "Account Number",
        "Currency",
        "Current",
        "Available",
    ]

    if show_inactive:
        headers.append("Status")

    items = accounts

    if not show_inactive:
        items = filter(lambda account: account.status == AccountStatus.ACTIVE, items)
    if account_type:
        items = filter(lambda account: account.type == account_type, items)
    if currency:
        items = filter(lambda account: account.balance.currency == currency, items)

    items = sorted(items, key=lambda account: account.type.value)
    items = sorted(
        items,
        key=lambda account: account.balance.current
        if account.balance.current is not None
        else -math.inf,
    )
    items = sorted(
        items,
        key=lambda account: account.balance.available
        if account.balance.available is not None
        else -math.inf,
    )
    items = sorted(items, key=lambda account: account.balance.currency)

    rows = [account_row(item) for item in items]

    def reducer(acc: dict, row: list):
        currency = row[4]
        current = row[5]
        available = row[6]
        item = acc.get(currency, [currency, 0, 0])
        item[1] = round(item[1] + (current or 0.0), 2)
        item[2] = round(item[2] + (available or 0.0), 2)
        acc[currency] = item
        return acc

    totals = reduce(reducer, rows, {})

    totals = list([["", "", "", "Total"] + value for value in totals.values()])
    if show_inactive:
        totals = [total + [] for total in totals]

    render_table(
        rows + totals,
        headers=headers,
        tablefmt="fancy_grid",
    )
