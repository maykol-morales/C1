from datetime import datetime
from app.models.debtor import DebtorStatus

from pydantic import BaseModel

class DebtorCreate(BaseModel):
    dni_bank: str
    status: DebtorStatus
    phone: str
    nextUpdate: datetime
    debtorRating: int

class DebtorUpdate(BaseModel):
    dni_bank: str | None = None
    status: DebtorStatus | None = None
    phone: str | None = None
    nextUpdate: datetime | None = None
    debtorRating: int | None = None

class DebtorOut(DebtorCreate):
    uid: str

    class Config:
        from_attributes = True
