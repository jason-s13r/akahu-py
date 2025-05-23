from datetime import datetime
from pydantic import ConfigDict, Field
from pydantic.dataclasses import dataclass


@dataclass(config=ConfigDict(validate_by_name=True))
class User:
    email: str
    preferred_name: str
    access_granted_at: datetime
    mobile: str = None
    first_name: str = None
    last_name: str = None
    id: str = Field(..., alias="_id")
