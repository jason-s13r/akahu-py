from datetime import UTC, datetime, timedelta
from typing import List
import click
from click_extra.tabulate import render_table

from akahu.client import Client as AkahuClient
from akahu.models.transaction import PendingTransaction, Transaction
from akahu.cli.utils import get_tokens


@click.group("transactions")
def transactions():
    """Transaction commands."""
    pass


@transactions.command("list")
@click.option(
    "--days", default=7, type=click.IntRange(0, 30, min_open=True, max_open=True)
)
def list_transactions(days: int):
    app_token, user_token = get_tokens()

    api = AkahuClient(AkahuClient.Config(app_token, user_token))

    end = datetime.now(UTC)
    start = end - timedelta(days=days)

    cursor = api.transactions.list(start=start, end=end)
    transactions = cursor.items

    def meta(tx: Transaction) -> str:
        m = []
        if tx.category:
            if tx.category.groups and tx.category.groups.personal_finance:
                m.append(tx.category.groups.personal_finance.name)
            m.append(tx.category.name)
        if tx.merchant:
            m.append(tx.merchant.name)
        return " > ".join(m)

    def tx_row(tx: Transaction) -> List:
        row = [tx.date, tx.type.value, tx.amount, tx.balance, meta(tx)]
        return row

    headers = [
        "Date",
        "Type",
        "Amount",
        "Balance",
        "Group",
        "Category",
        "Merchant",
    ]

    items = transactions
    rows = [tx_row(item) for item in items]
    total = sum([item.amount for item in items], 0)
    totals = [["", "Total", total, "", "", "", ""]]

    render_table(
        rows + totals,
        headers=headers,
        tablefmt="fancy_grid",
    )


@transactions.command("pending")
def pending_transactions():
    app_token, user_token = get_tokens()

    api = AkahuClient(AkahuClient.Config(app_token, user_token))

    transactions = api.transactions.pending.list()

    def tx_row(tx: PendingTransaction) -> List:
        row = [
            tx.date,
            tx.account,
            tx.type.value,
            tx.amount,
            tx.description,
        ]
        return row

    headers = [
        "Date",
        "Account",
        "Type",
        "Amount",
        "Description",
    ]

    items = transactions
    rows = [tx_row(item) for item in items]
    total = sum([item.amount for item in items], 0)
    totals = [["", "Total", total, "", "", "", ""]]

    render_table(
        rows + totals,
        headers=headers,
        tablefmt="fancy_grid",
    )
