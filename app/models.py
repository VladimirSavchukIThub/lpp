import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    checks = relationship("Check", back_populates="category")

class Check(Base):
    __tablename__ = "checks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sum = Column(Integer, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    date = Column(DateTime)
    description = Column(String, index=True)

    category = relationship("Category", back_populates="checks")