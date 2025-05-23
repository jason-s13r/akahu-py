from akahu.api.endpoints.transactions import TransactionsEndpoint
from akahu.models.account import Account
from akahu.rest.base import ApiBase
from akahu.rest.endpoint.getbyid import ApiGetByIdEndpoint
from akahu.rest.endpoint.list import ApiListEndpoint


class AccountsEndpoint(ApiGetByIdEndpoint[Account], ApiListEndpoint[Account]):
    def __init__(self, client: ApiBase, endpoint="/accounts") -> None:
        super().__init__(client, endpoint, Account)

    def transactions(self, id: str) -> TransactionsEndpoint:
        return TransactionsEndpoint(self, f"/{id}/transactions")
