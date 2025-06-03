from backoff import expo, on_exception
from ratelimit import RateLimitException, limits
from akahu.api.rest.base import ApiBase, ApiEndpoint
from akahu.api.rest.endpoint.defaults import DEFAULT_RETRY_LIMIT


class RefreshEndpoint(ApiEndpoint):
    """Endpoints for refreshing data.

    Arguments:
        client (ApiBase): The API client, or prefix-endpoint in the url path.
        endpoint (str): (optional) The endpoint for the data refresh API. Defaults to "/refresh".
    """

    def __init__(self, client: ApiBase, endpoint="/refresh") -> None:
        super().__init__(client, endpoint, bool)

    @on_exception(expo, RateLimitException, max_tries=DEFAULT_RETRY_LIMIT)
    @limits(calls=1, period=900)
    def all(self, **kwargs) -> bool:
        raw = self._rest.post(self.endpoint, **kwargs)

        return bool(raw.get("success", False))

    @on_exception(expo, RateLimitException, max_tries=DEFAULT_RETRY_LIMIT)
    @limits(calls=1, period=900)
    def byId(self, id: str, **kwargs) -> bool:
        raw = self._rest.post(f"{self.endpoint}/{id}", **kwargs)

        return bool(raw.get("success", False))
