from sqlalchemy.orm import Session
from app.models import User, Category, Check
from app.schemas import UserCreate, CategoryCreate, CheckCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def create_check(db: Session, check: CheckCreate):
    db_check = Check(name=check.name, sum=check.sum, category_id=check.category_id, date=check.date, description=check.description)
    db.add(db_check)
    db.commit()
    db.refresh(db_check)
    return db_check