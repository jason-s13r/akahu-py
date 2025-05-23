from akahu.rest.base import ApiBase
from akahu.rest.endpoint.get import ApiGetEndpoint
from akahu.rest.endpoint.getbyid import ApiGetByIdEndpoint


class RefreshEndpoint(ApiGetEndpoint[bool], ApiGetByIdEndpoint[bool]):
    def __init__(self, client: ApiBase, endpoint="/refresh") -> None:
        super().__init__(client, endpoint, bool)
