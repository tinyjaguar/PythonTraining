from app.repositories.user_repo import UserRepository
from app.repositories.availability_repo import AvailabilityRepository
from app.db.models import Availability
from app.utils.enums import UserRole
from fastapi import HTTPException


class DoctorService:
    def __init__(self, user_repo: UserRepository, availability_repo: AvailabilityRepository):
        self.user_repo = user_repo
        self.availability_repo = availability_repo

    async def get_all_doctors(self):
        return await self.user_repo.get_all_doctors()

    async def get_doctor_availability(self, doctor_id: int):
        return await self.availability_repo.get_by_doctor_id(doctor_id)

    async def set_doctor_availability(self, doctor_id: int, start_time, end_time):
        # Verify the user is a doctor
        doctor = await self.user_repo.get_by_id(doctor_id)
        if not doctor or doctor.role != UserRole.DOCTOR:
            raise HTTPException(403, "Only doctors can set availability")

        availability = Availability(
            doctor_id=doctor_id,
            start_time=start_time,
            end_time=end_time
        )

        return await self.availability_repo.create(availability)
