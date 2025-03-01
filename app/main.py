from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, categories

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(categories.router, prefix="/api", tags=["categories"])