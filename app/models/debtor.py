from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel, Field, constr, conint
from enum import Enum


class DebtorStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"


class Debtor(BaseModel):
    uid: str = Field(default_factory=lambda: str(uuid4()))

    dni_bank: str
    status: DebtorStatus
    phone: str
    nextUpdate: datetime
    debtorRating: int
