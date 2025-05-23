from requests import HTTPError, request

from akahu.rest.models.api_error import ApiError


class RestClient:
    def __init__(self, base_url: str, headers: dict = None) -> None:
        self._base_url = base_url
        self._headers = headers if headers else {}

    def _request(
        self, method: str, endpoint: str, headers: dict = {}, **kwargs
    ) -> dict:
        url = f"{self._base_url}{endpoint}"
        try:
            request_headers = {}
            request_headers.update(self._headers)
            request_headers.update(headers)
            response = request(method, url, headers=request_headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except HTTPError as error:
            exception = ApiError(error)
            exception.raise_rate_limit_error()
            raise exception

    def get(self, endpoint: str, **kwargs) -> dict:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> dict:
        return self._request("POST", endpoint, **kwargs)
