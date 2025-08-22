from app.models.user import Role
from app.schemas.debtor import DebtorOut, DebtorCreate

from pydantic import BaseModel

class UserCreate(BaseModel):
    organization: str
    role: Role
    workload: list[DebtorCreate] = []

class UserUpdate(BaseModel):
    organization: str | None = None
    role: Role | None = None

class UserOut(BaseModel):
    id: str
    organization: str
    role: Role
    workload: list[DebtorOut] = []

    class Config:
        from_attributes = True
