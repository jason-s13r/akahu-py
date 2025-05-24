from akahu.models.user import User
from akahu.rest.base import ApiBase
from akahu.rest.endpoint.get import ApiGetEndpoint


class MeEndpoint(ApiGetEndpoint[User]):
    """Endpoints for retrieving current user details.

    Arguments:
        client (ApiBase): The API client, or prefix-endpoint in the url path.
        endpoint (str): (optional) The endpoint for the me API. Defaults to "/me".
    """

    def __init__(self, client: ApiBase, endpoint="/me") -> None:
        super().__init__(client, endpoint, User)
