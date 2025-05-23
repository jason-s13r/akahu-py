from akahu.api.endpoints.accounts import AccountsEndpoint
from akahu.api.endpoints.me import MeEndpoint
from akahu.api.endpoints.payments import PaymentsEndpoint
from akahu.api.endpoints.pending_transactions import PendingTransactionsEndpoint
from akahu.api.endpoints.refresh import RefreshEndpoint
from akahu.api.endpoints.transactions import TransactionsEndpoint
from akahu.api.endpoints.transfers import TransfersEndpoint
from akahu.rest.base import ApiBase


class Client(ApiBase):
    def __init__(
        self,
        app_token: str,
        user_token: str,
        base: str = "https://api.akahu.io/v1",
        appTokenHeader: str = "X-Akahu-Id",
    ) -> None:
        super().__init__(
            base,
            {appTokenHeader: app_token, "Authorization": f"Bearer {user_token}"},
        )

        self.accounts = AccountsEndpoint(self)
        self.transactions = TransactionsEndpoint(self)
        self.pendingTransactions = PendingTransactionsEndpoint(self)
        self.refresh = RefreshEndpoint(self)
        self.me = MeEndpoint(self)
        self.payments = PaymentsEndpoint(self)
        self.transfers = TransfersEndpoint(self)
