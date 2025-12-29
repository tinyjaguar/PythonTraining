from fastapi import FastAPI
from app.api import auth, doctors, appointments
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Doctor Appointment API")

app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(appointments.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
