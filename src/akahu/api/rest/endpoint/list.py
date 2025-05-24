from typing import List
from backoff import expo, on_exception
from ratelimit import RateLimitException, limits

from akahu.api.rest.base import ApiBase, ApiEndpoint
from akahu.api.rest.endpoint.defaults import (
    DEFAULT_RATE_LIMIT,
    DEFAULT_RATE_LIMIT_PERIOD,
    DEFAULT_RETRY_LIMIT,
)
from akahu.api.rest.models.paged_response import PagedResponse


class ApiListEndpoint[T](ApiEndpoint):
    def __init__(self, client: ApiBase, endpoint: str, Ctor: T.__class__) -> None:
        super().__init__(client, endpoint, Ctor)

    @on_exception(expo, RateLimitException, max_tries=DEFAULT_RETRY_LIMIT)
    @limits(calls=DEFAULT_RATE_LIMIT, period=DEFAULT_RATE_LIMIT_PERIOD)
    def list(self, **params) -> List[T]:
        def next(**kwargs):
            return self._rest.get(self.endpoint, params=kwargs)

        data = next(**params)
        cursor = PagedResponse[T](self._Ctor, next, **data)
        return cursor.items


class ApiPagedEndpoint[T](ApiEndpoint):
    def __init__(self, client: ApiBase, endpoint: str, Ctor: T.__class__) -> None:
        super().__init__(client, endpoint, Ctor)

    @on_exception(expo, RateLimitException, max_tries=DEFAULT_RETRY_LIMIT)
    @limits(calls=DEFAULT_RATE_LIMIT, period=DEFAULT_RATE_LIMIT_PERIOD)
    def list(self, **params) -> PagedResponse[T]:
        def next(**kwargs):
            return self._rest.get(self.endpoint, params=kwargs)

        data = next(**params)
        return PagedResponse[T](self._Ctor, next, **data)
