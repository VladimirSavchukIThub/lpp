from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: str

class CategoryCreate(BaseModel):
    name: str

class CheckCreate(BaseModel):
    name: str
    sum: int
    category_id: int
    date: datetime
    description: str