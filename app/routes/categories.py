from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from unicodedata import category

from app.database import SessionLocal
from app.crud import create_category
from app.schemas import CategoryCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/categories/")
def register_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)