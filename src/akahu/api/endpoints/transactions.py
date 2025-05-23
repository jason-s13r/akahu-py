from akahu.api.endpoints.pending_transactions import PendingTransactionsEndpoint
from akahu.models.transaction import Transaction
from akahu.rest.base import ApiBase
from akahu.rest.endpoint.getbyid import ApiGetByIdEndpoint
from akahu.rest.endpoint.list import ApiPagedEndpoint


from datetime import datetime

from akahu.rest.models.paged_response import PagedResponse


class TransactionsEndpoint(
    ApiGetByIdEndpoint[Transaction], ApiPagedEndpoint[Transaction]
):
    def __init__(self, client: ApiBase, endpoint="/transactions") -> None:
        super().__init__(client, endpoint, Transaction)

        self.pending = PendingTransactionsEndpoint(self, "/pending")

    def list(
        self, start: datetime, end: datetime, cursor: str = None, **kwargs
    ) -> PagedResponse[Transaction]:
        return super().list(start=start, end=end, cursor=cursor, **kwargs)
