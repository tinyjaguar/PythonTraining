from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import Availability


class AvailabilityRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_doctor_id(self, doctor_id: int):
        result = await self.db.execute(
            select(Availability).where(Availability.doctor_id == doctor_id)
        )
        return result.scalars().all()

    async def create(self, availability: Availability):
        self.db.add(availability)
        await self.db.commit()
        await self.db.refresh(availability)
        return availability
