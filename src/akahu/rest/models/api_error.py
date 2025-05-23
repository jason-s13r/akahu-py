from ratelimit import RateLimitException
from requests import HTTPError

UNKNOWN_ERROR_MESSAGE = "An unknown error occurred"
DEFAULT_ERROR_MESSAGE = {429: "Rate limit exceeded. Please try again later."}


class ApiError(HTTPError):
    def __init__(self, error: HTTPError) -> None:
        super(error)
        self._data = None

    @property
    def status_code(self) -> int:
        return self.response.status_code

    @property
    def data(self) -> dict:
        if self._data is None:
            try:
                self._data = self.response.json()
            except ValueError:
                self._data = {}
        return self._data

    @property
    def success(self) -> bool:
        return self.data.get("success", False)

    @property
    def message(self) -> str:
        return (
            self.data.get("message")
            or DEFAULT_ERROR_MESSAGE.get(self.status_code)
            or UNKNOWN_ERROR_MESSAGE
        )

    @classmethod
    def raise_rate_limit_error(self) -> None:
        if self.status_code == 429:
            raise RateLimitException(self.message)
