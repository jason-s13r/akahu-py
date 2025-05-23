from akahu.models.transaction import PendingTransaction
from akahu.rest.base import ApiBase
from akahu.rest.endpoint.list import ApiListEndpoint


class PendingTransactionsEndpoint(ApiListEndpoint[PendingTransaction]):
    def __init__(self, client: ApiBase, endpoint="/transactions/pending") -> None:
        super().__init__(client, endpoint, PendingTransaction)
