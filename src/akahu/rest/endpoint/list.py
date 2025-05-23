from typing import List
from backoff import expo, on_exception
from ratelimit import RateLimitException, limits

from akahu.rest.base import ApiBase, ApiEndpoint
from akahu.rest.models.paged_response import PagedResponse
from akahu.utils import (
    AKAHU_DEFAULT_RATE_LIMIT,
    AKAHU_DEFAULT_RATE_LIMIT_PERIOD,
    AKAHU_DEFAULT_RETRY_LIMIT,
)


class ApiListEndpoint[T](ApiEndpoint):
    def __init__(self, client: ApiBase, endpoint: str, Ctor: T.__class__) -> None:
        super().__init__(client, endpoint, Ctor)

    @on_exception(expo, RateLimitException, max_tries=AKAHU_DEFAULT_RETRY_LIMIT)
    @limits(calls=AKAHU_DEFAULT_RATE_LIMIT, period=AKAHU_DEFAULT_RATE_LIMIT_PERIOD)
    def list(self, **params) -> List[T]:
        def next(**kwargs):
            return self._rest.get(self.endpoint, params=kwargs)

        data = next(**params)
        cursor = PagedResponse[T](self._Ctor, next, **data)
        return cursor.items


class ApiPagedEndpoint[T](ApiEndpoint):
    def __init__(self, client: ApiBase, endpoint: str, Ctor: T.__class__) -> None:
        super().__init__(client, endpoint, Ctor)

    @on_exception(expo, RateLimitException, max_tries=AKAHU_DEFAULT_RETRY_LIMIT)
    @limits(calls=AKAHU_DEFAULT_RATE_LIMIT, period=AKAHU_DEFAULT_RATE_LIMIT_PERIOD)
    def list(self, **params) -> PagedResponse[T]:
        def next(**kwargs):
            return self._rest.get(self.endpoint, params=kwargs)

        data = next(**params)
        return PagedResponse[T](self._Ctor, next, **data)
