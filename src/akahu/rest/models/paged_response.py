from typing import List


class PagedResponse[T]:
    def __init__(
        self, Ctor: T.__class__, next, success: bool, items: List, cursor: dict = None
    ):
        self._success = success
        self._items: List[T] = [Ctor(**item) for item in items] if items else []
        self._cursor = cursor or dict(next=None)
        self._next = next

    @property
    def success(self) -> bool:
        return self._success

    @property
    def items(self) -> List[T]:
        return self._items

    @property
    def size(self) -> int:
        return len(self._items)

    @property
    def cursor(self) -> str | None:
        return self._cursor.get("next", None)

    @property
    def has_next(self) -> bool:
        return self.cursor is not None

    def next(self, **kwargs) -> "PagedResponse[T]":
        if not self.has_next:
            return None
        if not self._next:
            return None

        response = self._next(cursor=self.cursor, **kwargs)
        return PagedResponse[T](self._next, **response)
