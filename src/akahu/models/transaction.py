from enum import Enum
from datetime import datetime

from pydantic import ConfigDict, Field
from pydantic.dataclasses import dataclass


class TransactionType(Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    PAYMENT = "PAYMENT"
    TRANSFER = "TRANSFER"
    STANDING_ORDER = "STANDING ORDER"
    EFTPOS = "EFTPOS"
    INTEREST = "INTEREST"
    FEE = "FEE"
    TAX = "TAX"
    CREDIT_CARD = "CREDIT CARD"
    DIRECT_DEBIT = "DIRECT DEBIT"
    DIRECT_CREDIT = "DIRECT CREDIT"
    ATM = "ATM"
    LOAN = "LOAN"


@dataclass(config=ConfigDict(validate_by_name=True))
class Merchant:
    name: str
    nzbn: str = None
    website: str = None
    id: str = Field(..., alias="_id")


@dataclass(config=ConfigDict(validate_by_name=True))
class Group:
    name: str
    id: str = Field(..., alias="_id")


@dataclass(config=ConfigDict(extra="allow"))
class Groups:
    personal_finance: Group = None


@dataclass(config=ConfigDict(validate_by_name=True))
class Category:
    name: str
    groups: Groups = None
    id: str = Field(..., alias="_id")


@dataclass(config=ConfigDict(extra="allow"))
class Conversion:
    amount: float
    currency: str
    rate: float


@dataclass(config=ConfigDict(extra="allow"))
class Meta:
    particulars: str = None
    code: str = None
    reference: str = None
    other_account: str = None
    conversion: Conversion = None
    card_suffix: str = None
    logo: str = None


@dataclass(config=ConfigDict(validate_by_name=True))
class Transaction:
    created_at: datetime
    updated_at: datetime
    date: datetime
    description: str
    amount: float
    balance: float
    type: TransactionType

    meta: Meta = None
    merchant: Merchant = None
    category: Category = None

    id: str = Field(..., alias="_id")
    account: str = Field(..., alias="_account")
    user: str = Field(..., alias="_user")
    connection: str = Field(..., alias="_connection")


@dataclass(config=ConfigDict(validate_by_name=True))
class PendingTransaction:
    updated_at: datetime
    date: datetime
    description: str
    amount: float
    type: TransactionType

    account: str = Field(..., alias="_account")
    user: str = Field(..., alias="_user")
    connection: str = Field(..., alias="_connection")
