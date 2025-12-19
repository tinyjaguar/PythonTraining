from fastapi import FastAPI
from app.database import Base, engine
from app.routers.user import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Login Management")

app.include_router(user_router)

@app.get("/")
def health_check():
    return {"status": "UP"}
