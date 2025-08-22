from enum import Enum
from uuid import uuid4

from pydantic import BaseModel, Field

from app.models.debtor import Debtor


class Role(str, Enum):
    ADMIN = "admin"
    WORKER = "worker"


class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    organization: str
    workload: list[Debtor] = []
    role: Role
