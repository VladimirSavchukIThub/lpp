from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.crud import create_check
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