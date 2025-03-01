from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.crud import *
from app.schemas import CheckCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/checks/")
def register_check(check: CheckCreate, db: Session = Depends(get_db)):
    return create_check(db, check)
@router.get("/checks/{check_id}")
def get_single_check(check_id: int, db: Session = Depends(get_db)):
    return get_check(db, check_id)

@router.get("/checks/")
def get_all_checks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_checks(db, skip=skip, limit=limit)

@router.put("/checks/{check_id}")
def update_single_check(check_id: int, check: CheckCreate, db: Session = Depends(get_db)):
    return update_check(db, check_id, check)

@router.delete("/checks/{check_id}")
def delete_single_check(check_id: int, db: Session = Depends(get_db)):
    return delete_check(db, check_id)