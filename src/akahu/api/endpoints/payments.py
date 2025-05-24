from typing import List
from akahu.models.payment import Payment
from akahu.api.rest.base import ApiBase
from akahu.api.rest.endpoint.getbyid import ApiGetByIdEndpoint
from akahu.api.rest.endpoint.list import ApiListEndpoint


from datetime import datetime


class PaymentsEndpoint(ApiGetByIdEndpoint[Payment], ApiListEndpoint[Payment]):
    """Endpoints for retrieving information about payments.

    Arguments:
        client (ApiBase): The API client, or prefix-endpoint in the url path.
        endpoint (str): (optional) The endpoint for the payments API. Defaults to "/payments".
    """

    def __init__(self, client: ApiBase, endpoint="/payments") -> None:
        super().__init__(client, endpoint, Payment)

    def list(self, start: datetime, end: datetime, **kwargs) -> List[Payment]:
        return super().list(start=start, end=end, **kwargs)
