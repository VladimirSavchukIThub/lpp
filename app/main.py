from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, categories, checks

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(categories.router, prefix="/api", tags=["categories"])
app.include_router(checks.router, prefix="/api", tags=["checks"])