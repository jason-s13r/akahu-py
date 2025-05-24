from functools import cached_property
from typing import Unpack
from pydantic import ConfigDict
from pydantic.dataclasses import dataclass

from akahu.api.endpoints.accounts import AccountsEndpoint
from akahu.api.endpoints.me import MeEndpoint
from akahu.api.endpoints.payments import PaymentsEndpoint
from akahu.api.endpoints.pending_transactions import PendingTransactionsEndpoint
from akahu.api.endpoints.refresh import RefreshEndpoint
from akahu.api.endpoints.transactions import TransactionsEndpoint
from akahu.api.endpoints.transfers import TransfersEndpoint
from akahu.rest.base import ApiBase


class Client(ApiBase):
    """Akahu API client.

    Arguments:
        config (Client.Config): (optional) Configuration for the Akahu API client.
        **kwargs (Client.Config): Additional configuration parameters.
    """

    @dataclass(config=ConfigDict(extra="ignore"))
    class Config:
        """Configuration for the Akahu API client.

        Attributes:
            app_token (str): The application token.
            user_token (str): The user token.
            base (str): (optional) Override the base URL for the API. Defaults to "https://api.akahu.io/v1".
            app_token_header_name (str): (optional) Override the header name for the application token. Defaults to "X-Akahu-Id".
        """

        app_token: str
        user_token: str
        base: str = "https://api.akahu.io/v1"
        app_token_header_name: str = "X-Akahu-Id"

    def __init__(self, config: Config = None, **kwargs: Unpack[Config]) -> None:
        if not config:
            config = self.Config(**kwargs)
        super().__init__(
            config.base,
            {
                config.app_token_header_name: config.app_token,
                "Authorization": f"Bearer {config.user_token}",
            },
        )

    @cached_property
    def accounts(self) -> AccountsEndpoint:
        """Endpoints for retreiving accounts."""
        return AccountsEndpoint(self)

    @cached_property
    def transactions(self) -> TransactionsEndpoint:
        """Endpoints for retreiving transactions."""
        return TransactionsEndpoint(self)

    @cached_property
    def pending_transactions(self) -> PendingTransactionsEndpoint:
        """Endpoints for retreiving pending transctions."""
        return PendingTransactionsEndpoint(self)

    @cached_property
    def refresh(self) -> RefreshEndpoint:
        """Endpoints for requesting a data refresh."""
        return RefreshEndpoint(self)

    @cached_property
    def me(self) -> MeEndpoint:
        """Endpoints for retreiving current user information."""
        return MeEndpoint(self)

    @cached_property
    def payments(self) -> PaymentsEndpoint:
        """Endpoints for retreiving payments."""
        return PaymentsEndpoint(self)

    @cached_property
    def transfers(self) -> TransfersEndpoint:
        """Endpoints for retreiving transfers."""
        return TransfersEndpoint(self)
