from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.routes import router

app = FastAPI(
    title="Energy Price Intelligence Platform",
    version="1.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)
