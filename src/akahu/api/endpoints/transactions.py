from functools import cached_property

from akahu.api.endpoints.pending_transactions import PendingTransactionsEndpoint
from akahu.models.transaction import Transaction
from akahu.api.rest.base import ApiBase
from akahu.api.rest.endpoint.getbyid import ApiGetByIdEndpoint
from akahu.api.rest.endpoint.list import ApiPagedEndpoint


from datetime import datetime

from akahu.api.rest.models.paged_response import PagedResponse


class TransactionsEndpoint(
    ApiGetByIdEndpoint[Transaction], ApiPagedEndpoint[Transaction]
):
    """Endpoints for retrieving transactions.

    Arguments:
        client (ApiBase): The API client, or prefix-endpoint in the url path.
        endpoint (str): (optional) The endpoint for the transactions API. Defaults to "/transactions".
    """

    def __init__(self, client: ApiBase, endpoint="/transactions") -> None:
        super().__init__(client, endpoint, Transaction)

        self.pending = PendingTransactionsEndpoint(self, "/pending")

    def list(
        self, start: datetime, end: datetime, cursor: str = None, **kwargs
    ) -> PagedResponse[Transaction]:
        """List transactions.

        Arguments:
            start (datetime): Start date for the transactions.
            end (datetime): End date for the transactions.
            cursor (str): Cursor for pagination.
        """
        return super().list(**kwargs)

    @cached_property
    def pending(self) -> PendingTransactionsEndpoint:
        """Endpoint for retrieving pending transactions. Might be scoped to a specific account."""
        return PendingTransactionsEndpoint(self, "/pending")
