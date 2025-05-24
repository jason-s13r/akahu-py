from typing import Any
from akahu.api.rest.client import RestClient


class ApiBase:
    def __init__(self, base: str, headers: dict = {}) -> None:
        self._base = base
        self._rest: RestClient = RestClient(base, headers=headers)

    @property
    def endpoint(self) -> str:
        return ""


class ApiEndpoint(ApiBase):
    def __init__(self, client: ApiBase, endpoint: str, Ctor: Any = object) -> None:
        self._Ctor = Ctor
        self._client = client
        self._endpoint = endpoint

    @property
    def endpoint(self) -> str:
        return self._client.endpoint + self._endpoint

    @property
    def _rest(self):
        return self._client._rest
