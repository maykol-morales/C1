from uuid import uuid4
from enum import Enum

from sqlalchemy import Column, String, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class Role(str, Enum):
    ADMIN = "admin"
    WORKER = "worker"


class User(Base):
    __tablename__ = "users"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )
    organization = Column(String(100), nullable=False)
    role = Column(SQLEnum(Role), nullable=False)

    workload = relationship(
        "Debtor",
        back_populates="user",
        cascade="all, delete-orphan"
    )
