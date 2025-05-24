from akahu.api.rest.base import ApiBase
from akahu.api.rest.endpoint.get import ApiGetEndpoint
from akahu.api.rest.endpoint.getbyid import ApiGetByIdEndpoint


class RefreshEndpoint(ApiGetEndpoint[bool], ApiGetByIdEndpoint[bool]):
    """Endpoints for refreshing data.

    Arguments:
        client (ApiBase): The API client, or prefix-endpoint in the url path.
        endpoint (str): (optional) The endpoint for the data refresh API. Defaults to "/refresh".
    """

    def __init__(self, client: ApiBase, endpoint="/refresh") -> None:
        super().__init__(client, endpoint, bool)
