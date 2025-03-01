from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from unicodedata import category

from app.database import SessionLocal
from app.crud import *
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

@router.get("/categories/")
def get_all_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_categories(db, skip=skip, limit=limit)

@router.get("/categories/{category_id}")
def get_single_category(category_id: int, db: Session = Depends(get_db)):
    return get_category(db, category_id)

@router.put("/categories/{category_id}")
def update_single_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    return update_category(db, category_id, category)

@router.delete("/categories/{category_id}")
def delete_single_category(category_id: int, db: Session = Depends(get_db)):
    return delete_category(db, category_id)