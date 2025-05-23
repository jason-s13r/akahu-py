from datetime import datetime
from enum import Enum
from typing import List
from pydantic import ConfigDict, Field
from pydantic.dataclasses import dataclass


class PaymentStatus(Enum):
    READY = "READY"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    SENT = "SENT"
    PAUSED = "PAUSED"
    DECLINED = "DECLINED"
    CANCELLED = "CANCELLED"
    ERROR = "ERROR"


@dataclass(config=ConfigDict(validate_by_name=True))
class To:
    account_number: str
    name: str


@dataclass(config=ConfigDict(validate_by_name=True))
class Timeline:
    status: str
    time: datetime
    eta: datetime


@dataclass(config=ConfigDict(validate_by_name=True))
class Source:
    code: str
    reference: str


@dataclass
class Destination:
    code: str
    particulars: str
    reference: str


@dataclass
class Meta:
    destination: Destination
    source: Source


@dataclass(config=ConfigDict(validate_by_name=True))
class Payment:
    sid: str
    to: To
    meta: Meta
    amount: float
    status: PaymentStatus
    status_text: str
    timeline: List[Timeline]
    created_at: datetime
    updated_at: datetime
    received_at: datetime | None

    id: str = Field(..., alias="_id")
    from_: str = Field(..., alias="from")
