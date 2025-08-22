from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from app.db import get_db
from app.models.user import User, Role
from app.models.debtor import Debtor
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.schemas.debtor import DebtorCreate

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    user = User(organization=payload.organization, role=payload.role)

    # si mandan workload, crear debtors asociados
    for d in payload.workload:
        user.workload.append(Debtor(**d.model_dump()))

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    # joinedload para traer workload en una sola query
    users = db.query(User).options(joinedload(User.workload)).all()
    return users

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).options(joinedload(User.workload)).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User no encontrado")
    return user

@router.patch("/{user_id}", response_model=UserOut)
def update_user(user_id: str, payload: UserUpdate, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User no encontrado")

    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(user, k, v)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User no encontrado")
    db.delete(user)
    db.commit()
    return None
