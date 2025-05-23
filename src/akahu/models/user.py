from datetime import datetime
from pydantic import ConfigDict, Field
from pydantic.dataclasses import dataclass


@dataclass(config=ConfigDict(validate_by_name=True))
class User:
    email: str
    mobile: str
    first_name: str
    last_name: str
    preferred_name: str
    access_granted_at: datetime
    id: str = Field(..., alias="_id")
