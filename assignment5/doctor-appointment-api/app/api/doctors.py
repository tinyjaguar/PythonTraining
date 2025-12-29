from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserResponse
from app.schemas.availability import AvailabilityResponse, AvailabilityCreate
from app.services.doctor_service import DoctorService
from app.repositories.user_repo import UserRepository
from app.repositories.availability_repo import AvailabilityRepository
from app.core.security import get_current_user
from app.db.models import User
from app.db.session import get_db

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.get("", response_model=list[UserResponse])
async def get_doctors(db=Depends(get_db)):
    service = DoctorService(UserRepository(db), AvailabilityRepository(db))
    doctors = await service.get_all_doctors()
    return doctors


@router.get("/{doctor_id}/availability", response_model=list[AvailabilityResponse])
async def get_doctor_availability(doctor_id: int, db=Depends(get_db)):
    service = DoctorService(UserRepository(db), AvailabilityRepository(db))

    # First check if doctor exists
    doctor = await service.user_repo.get_by_id(doctor_id)
    if not doctor:
        raise HTTPException(404, "Doctor not found")

    availability = await service.get_doctor_availability(doctor_id)
    return availability


@router.post("/availability", response_model=AvailabilityResponse)
async def set_doctor_availability(
    payload: AvailabilityCreate,
    current_user: User = Depends(get_current_user),
    db=Depends(get_db)
):
    if current_user.role.name != "DOCTOR":
        raise HTTPException(403, "Only doctors can set their availability")

    service = DoctorService(UserRepository(db), AvailabilityRepository(db))
    availability = await service.set_doctor_availability(
        current_user.id,
        payload.start_time,
        payload.end_time
    )
    return availability
