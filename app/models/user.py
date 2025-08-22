from uuid import uuid4
from enum import Enum

from pydantic import BaseModel, Field

class Role(str, Enum):
    ADMIN = "admin"
    WORKER = "worker"

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    organization: str
    role: Role
