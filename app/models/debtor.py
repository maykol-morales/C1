from datetime import datetime
from enum import Enum
from uuid import uuid4

from sqlalchemy import Column, String, Integer, DateTime, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class DebtorStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"


class Debtor(Base):
    __tablename__ = "debtors"

    uid = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )
    dni_bank = Column(String(64), nullable=False)
    status = Column(SQLEnum(DebtorStatus), nullable=False)
    phone = Column(String(20), nullable=False)
    nextUpdate = Column(DateTime, default=datetime.utcnow, nullable=False)
    debtorRating = Column(Integer, nullable=False)

    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="workload")