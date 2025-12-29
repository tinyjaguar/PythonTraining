from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_
from datetime import datetime
from app.db.models import Appointment


class AppointmentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, appointment_id: int):
        result = await self.db.execute(
            select(Appointment).where(Appointment.id == appointment_id)
        )
        return result.scalar_one_or_none()

    async def get_by_doctor_id(self, doctor_id: int):
        result = await self.db.execute(
            select(Appointment).where(Appointment.doctor_id == doctor_id)
        )
        return result.scalars().all()

    async def get_by_patient_id(self, patient_id: int):
        result = await self.db.execute(
            select(Appointment).where(Appointment.patient_id == patient_id)
        )
        return result.scalars().all()

    async def check_conflict(self, doctor_id: int, start_time: datetime, end_time: datetime, exclude_id: int = None):
        query = select(Appointment).where(
            and_(
                Appointment.doctor_id == doctor_id,
                or_(
                    and_(Appointment.start_time <= start_time, Appointment.end_time > start_time),
                    and_(Appointment.start_time < end_time, Appointment.end_time >= end_time),
                    and_(Appointment.start_time >= start_time, Appointment.end_time <= end_time)
                )
            )
        )

        if exclude_id:
            query = query.where(Appointment.id != exclude_id)

        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def create(self, appointment: Appointment):
        self.db.add(appointment)
        await self.db.commit()
        await self.db.refresh(appointment)
        return appointment

    async def delete(self, appointment: Appointment):
        await self.db.delete(appointment)
        await self.db.commit()
