from typing import List
from akahu.models.payment import Payment
from akahu.rest.base import ApiBase
from akahu.rest.endpoint.getbyid import ApiGetByIdEndpoint
from akahu.rest.endpoint.list import ApiListEndpoint


from datetime import datetime


class TransfersEndpoint(ApiGetByIdEndpoint[Payment], ApiListEndpoint[Payment]):
    """Endpoints for retrieving information about transfers.

    Arguments:
        client (ApiBase): The API client, or prefix-endpoint in the url path.
        endpoint (str): (optional) The endpoint for the transfers API. Defaults to "/transfers".
    """

    def __init__(self, client: ApiBase, endpoint="/transfers") -> None:
        super().__init__(client, endpoint, Payment)

    def list(self, start: datetime, end: datetime, **kwargs) -> List[Payment]:
        return super().list(start=start, end=end, **kwargs)
