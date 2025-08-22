from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.debtor import Debtor, DebtorStatus
from app.models.user import User
from app.schemas.debtor import DebtorCreate, DebtorUpdate, DebtorOut

router = APIRouter(prefix="/debtor", tags=["Debtor"])

@router.post("/", response_model=DebtorOut, status_code=status.HTTP_201_CREATED)
def create_debtor(payload: DebtorCreate, db: Session = Depends(get_db), user_id: str | None = Query(default=None)):
    debtor = Debtor(**payload.model_dump())

    # opcional: asociar a un user
    if user_id:
        user = db.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User no encontrado para asociar")
        debtor.user = user

    db.add(debtor)
    db.commit()
    db.refresh(debtor)
    return debtor

@router.get("/", response_model=list[DebtorOut])
def list_debtors(db: Session = Depends(get_db), user_id: str | None = None, status: DebtorStatus | None = None):
    q = db.query(Debtor)
    if user_id:
        q = q.filter(Debtor.user_id == user_id)
    if status:
        q = q.filter(Debtor.status == status)
    return q.all()

@router.get("/{uid}", response_model=DebtorOut)
def get_debtor(uid: str, db: Session = Depends(get_db)):
    obj = db.get(Debtor, uid)
    if not obj:
        raise HTTPException(status_code=404, detail="Debtor no encontrado")
    return obj

@router.patch("/{uid}", response_model=DebtorOut)
def update_debtor(uid: str, payload: DebtorUpdate, db: Session = Depends(get_db)):
    obj = db.get(Debtor, uid)
    if not obj:
        raise HTTPException(status_code=404, detail="Debtor no encontrado")

    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(obj, k, v)

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{uid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_debtor(uid: str, db: Session = Depends(get_db)):
    obj = db.get(Debtor, uid)
    if not obj:
        raise HTTPException(status_code=404, detail="Debtor no encontrado")
    db.delete(obj)
    db.commit()
    return None
