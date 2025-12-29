from pydantic import BaseModel
from datetime import datetime


class AppointmentCreate(BaseModel):
    doctor_id: int
    start_time: datetime
    end_time: datetime


class AppointmentResponse(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    start_time: datetime
    end_time: datetime

    class Config:
        from_attributes = True
