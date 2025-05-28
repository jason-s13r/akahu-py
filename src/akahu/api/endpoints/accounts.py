from akahu.api.endpoints.transactions import TransactionsEndpoint
from akahu.models.account import Account
from akahu.api.rest.base import ApiBase
from akahu.api.rest.endpoint.getbyid import ApiGetByIdEndpoint
from akahu.api.rest.endpoint.list import ApiListEndpoint


class AccountsEndpoint(ApiGetByIdEndpoint[Account], ApiListEndpoint[Account]):
    """Endpoints for retrieving accounts.

    Arguments:
        client (ApiBase): The API client, or prefix-endpoint in the url path.
        endpoint (str): (optional) The endpoint for the accounts API. Defaults to "/accounts".
    """

    def __init__(self, client: ApiBase, endpoint="/accounts") -> None:
        super().__init__(client, endpoint, Account)

    def transactions(self, id: str) -> TransactionsEndpoint:
        """Endpoint for retrieving transactions for a specific account.

        Args:
            id (str): The account ID.

        Returns:
            TransactionsEndpoint: A transactions endpoint scoped to the account.
            Route: /accounts/{id}/transactions.
        """
        print(f"TransactionsEndpoint: {id}")
        return TransactionsEndpoint(self, f"/{id}/transactions")
