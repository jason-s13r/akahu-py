from akahu.models.transaction import PendingTransaction
from akahu.rest.base import ApiBase
from akahu.rest.endpoint.list import ApiListEndpoint


class PendingTransactionsEndpoint(ApiListEndpoint[PendingTransaction]):
    """Endpoints for retrieving pending transactions.

    Arguments:
        client (ApiBase): The API client, or prefix-endpoint in the url path.
        endpoint (str): (optional) The endpoint for the pending transactions API. Defaults to "/transactions/pending".
    """

    def __init__(self, client: ApiBase, endpoint="/transactions/pending") -> None:
        super().__init__(client, endpoint, PendingTransaction)
