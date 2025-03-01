from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class CategoryCreate(BaseModel):
    name: str