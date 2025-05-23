from akahu.models.user import User
from akahu.rest.base import ApiBase
from akahu.rest.endpoint.get import ApiGetEndpoint


class MeEndpoint(ApiGetEndpoint[User]):
    def __init__(self, client: ApiBase, endpoint="/me") -> None:
        super().__init__(client, endpoint, User)
