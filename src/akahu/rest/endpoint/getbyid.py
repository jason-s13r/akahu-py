from backoff import expo, on_exception
from ratelimit import RateLimitException, limits

from akahu.rest.base import ApiBase, ApiEndpoint
from akahu.utils import (
    AKAHU_DEFAULT_RATE_LIMIT,
    AKAHU_DEFAULT_RATE_LIMIT_PERIOD,
    AKAHU_DEFAULT_RETRY_LIMIT,
)


class ApiGetByIdEndpoint[T](ApiEndpoint):
    def __init__(self, client: ApiBase, endpoint: str, Ctor: T.__class__) -> None:
        super().__init__(client, endpoint, Ctor)

    @on_exception(expo, RateLimitException, max_tries=AKAHU_DEFAULT_RETRY_LIMIT)
    @limits(calls=AKAHU_DEFAULT_RATE_LIMIT, period=AKAHU_DEFAULT_RATE_LIMIT_PERIOD)
    def getById(self, id: str, **kwargs) -> T:
        data = self._rest.get(f"{self.endpoint}/{id}", **kwargs)
        item = data.get("item")
        if not item:
            return None
        return self._Ctor(**item)
