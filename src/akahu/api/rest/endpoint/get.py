from pydantic.dataclasses import dataclass
from backoff import expo, on_exception
from ratelimit import RateLimitException, limits

from akahu.api.rest.base import ApiBase, ApiEndpoint
from akahu.api.rest.endpoint.defaults import (
    DEFAULT_RATE_LIMIT,
    DEFAULT_RATE_LIMIT_PERIOD,
    DEFAULT_RETRY_LIMIT,
)


@dataclass
class GetResponse[D]:
    success: bool
    item: D = None


class ApiGetEndpoint[T](ApiEndpoint):
    def __init__(self, client: ApiBase, endpoint: str, Ctor: T.__class__) -> None:
        super().__init__(client, endpoint, Ctor)

    @on_exception(expo, RateLimitException, max_tries=DEFAULT_RETRY_LIMIT)
    @limits(calls=DEFAULT_RATE_LIMIT, period=DEFAULT_RATE_LIMIT_PERIOD)
    def get(self, **kwargs) -> T:
        raw = self._rest.get(self.endpoint, **kwargs)
        data = GetResponse[T](**raw)
        if not data.item:
            return None
        return self._Ctor(**data.item)
