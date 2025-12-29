from fastapi import APIRouter, Depends, HTTPException
from app.schemas.appointment import AppointmentCreate, AppointmentResponse
from app.services.appointment_service import AppointmentService
from app.repositories.appointment_repo import AppointmentRepository
from app.repositories.user_repo import UserRepository
from app.repositories.availability_repo import AvailabilityRepository
from app.core.security import get_current_user
from app.db.models import User
from app.db.session import get_db

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.post("", response_model=AppointmentResponse)
async def create_appointment(
    payload: AppointmentCreate,
    current_user: User = Depends(get_current_user),
    db=Depends(get_db)
):
    if current_user.role.name != "PATIENT":
        raise HTTPException(403, "Only patients can book appointments")

    service = AppointmentService(
        AppointmentRepository(db),
        UserRepository(db),
        AvailabilityRepository(db)
    )

    appointment = await service.create_appointment(
        current_user.id,
        payload.doctor_id,
        payload.start_time,
        payload.end_time
    )
    return appointment


@router.get("", response_model=list[AppointmentResponse])
async def get_appointments(
    current_user: User = Depends(get_current_user),
    db=Depends(get_db)
):
    service = AppointmentService(
        AppointmentRepository(db),
        UserRepository(db),
        AvailabilityRepository(db)
    )

    appointments = await service.get_user_appointments(current_user.id, current_user.role)
    return appointments


@router.delete("/{appointment_id}")
async def cancel_appointment(
    appointment_id: int,
    current_user: User = Depends(get_current_user),
    db=Depends(get_db)
):
    service = AppointmentService(
        AppointmentRepository(db),
        UserRepository(db),
        AvailabilityRepository(db)
    )

    result = await service.cancel_appointment(appointment_id, current_user.id, current_user.role)
    return result
