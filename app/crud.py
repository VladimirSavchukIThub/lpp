from sqlalchemy.orm import Session
from app.models import User, Category, Check
from app.schemas import UserCreate, CategoryCreate, CheckCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Category).offset(skip).limit(limit).all()


def update_category(db: Session, category_id: int, category: CategoryCreate):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db_category.name = category.name
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category
    return None


def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return db_category
    return None

def create_check(db: Session, check: CheckCreate):
    db_check = Check(name=check.name, sum=check.sum, category_id=check.category_id, date=check.date, description=check.description)
    db.add(db_check)
    db.commit()
    db.refresh(db_check)
    return db_check

def get_check(db: Session, check_id: int):
    return db.query(Check).filter(Check.id == check_id).first()


def get_checks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Check).offset(skip).limit(limit).all()


def update_check(db: Session, check_id: int, check: CheckCreate):
    db_check = db.query(Check).filter(Check.id == check_id).first()
    if db_check:
        db_check.name = check.name
        db_check.sum = check.sum
        db_check.category_id = check.category_id
        db_check.date = check.date
        db_check.description = check.description
        db.add(db_check)
        db.commit()
        db.refresh(db_check)
        return db_check
    return None


def delete_check(db: Session, check_id: int):
    db_check = db.query(Check).filter(Check.id == check_id).first()
    if db_check:
        db.delete(db_check)
        db.commit()
        return db_check
    return None