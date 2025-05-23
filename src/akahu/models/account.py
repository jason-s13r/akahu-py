from datetime import datetime
from enum import Enum
from typing import List
from pydantic import ConfigDict, Field
from pydantic.dataclasses import dataclass


class AccountType(Enum):
    CHECKING = "CHECKING"
    SAVINGS = "SAVINGS"
    CREDITCARD = "CREDITCARD"
    LOAN = "LOAN"
    KIWISAVER = "KIWISAVER"
    INVESTMENT = "INVESTMENT"
    TERMDEPOSIT = "TERMDEPOSIT"
    FOREIGN = "FOREIGN"
    TAX = "TAX"
    REWARDS = "REWARDS"
    WALLET = "WALLET"


class AccountStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class AccountAttributes(Enum):
    TRANSACTIONS = "TRANSACTIONS"
    TRANSFER_TO = "TRANSFER_TO"
    TRANSFER_FROM = "TRANSFER_FROM"
    PAYMENT_TO = "PAYMENT_TO"
    PAYMENT_FROM = "PAYMENT_FROM"


@dataclass
class Balance:
    current: float
    currency: str
    available: float = None
    limit: float = None
    overdrawn: bool = None


@dataclass(config=ConfigDict(validate_by_name=True))
class Connection:
    name: str
    logo: str
    id: str = Field(..., alias="_id")


@dataclass(config=ConfigDict(validate_by_name=True))
class Refreshed:
    balance: datetime
    meta: datetime
    transactions: datetime = None
    party: datetime = None


@dataclass(config=ConfigDict(validate_by_name=True, extra="allow"))
class Meta:
    holder: str = None
    payment_details: dict = None
    loan_details: dict = None
    breakdown: dict = None
    portfolio: dict = None


@dataclass(config=ConfigDict(validate_by_name=True))
class Account:
    _authorisation: str
    _credentials: str
    name: str
    type: AccountType
    status: AccountStatus
    balance: Balance
    connection: Connection
    refreshed: Refreshed
    attributes: List[AccountAttributes]
    id: str = Field(..., alias="_id")
    meta: Meta = None
    formatted_account: str = None
