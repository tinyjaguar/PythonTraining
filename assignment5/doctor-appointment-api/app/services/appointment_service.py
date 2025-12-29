from datetime import datetime
from fastapi import HTTPException
from app.repositories.appointment_repo import AppointmentRepository
from app.repositories.user_repo import UserRepository
from app.repositories.availability_repo import AvailabilityRepository
from app.db.models import Appointment
from app.utils.enums import UserRole


class AppointmentService:
    def __init__(self, appointment_repo: AppointmentRepository, user_repo: UserRepository, availability_repo: AvailabilityRepository):
        self.appointment_repo = appointment_repo
        self.user_repo = user_repo
        self.availability_repo = availability_repo

    async def create_appointment(self, patient_id: int, doctor_id: int, start_time: datetime, end_time: datetime):
        # Validate doctor exists and is a doctor
        doctor = await self.user_repo.get_by_id(doctor_id)
        if not doctor or doctor.role != UserRole.DOCTOR:
            raise HTTPException(404, "Doctor not found")

        # Check if patient exists
        patient = await self.user_repo.get_by_id(patient_id)
        if not patient or patient.role != UserRole.PATIENT:
            raise HTTPException(403, "Invalid patient")

        # Validate appointment time range
        if end_time <= start_time:
            raise HTTPException(400, "End time must be after start time")

        # Check for appointment conflicts
        conflict = await self.appointment_repo.check_conflict(doctor_id, start_time, end_time)
        if conflict:
            raise HTTPException(409, "Appointment time conflicts with existing appointment")

        # Check if the time slot is within doctor's availability
        availability = await self.availability_repo.get_by_doctor_id(doctor_id)
        if not availability:
            raise HTTPException(400, "Doctor has no availability slots set up")

        slot_available = False
        for avail in availability:
            # Check if appointment fits within availability (appointment can be smaller than availability slot)
            if (avail.start_time <= start_time and avail.end_time >= end_time):
                slot_available = True
                break

        if not slot_available:
            raise HTTPException(400, "Requested time slot is not within doctor's available hours")

        appointment = Appointment(
            doctor_id=doctor_id,
            patient_id=patient_id,
            start_time=start_time,
            end_time=end_time
        )

        return await self.appointment_repo.create(appointment)

    async def get_user_appointments(self, user_id: int, user_role: UserRole):
        if user_role == UserRole.DOCTOR:
            return await self.appointment_repo.get_by_doctor_id(user_id)
        elif user_role == UserRole.PATIENT:
            return await self.appointment_repo.get_by_patient_id(user_id)
        else:
            raise HTTPException(403, "Invalid user role")

    async def cancel_appointment(self, appointment_id: int, user_id: int, user_role: UserRole):
        appointment = await self.appointment_repo.get_by_id(appointment_id)
        if not appointment:
            raise HTTPException(404, "Appointment not found")

        # Only patients can cancel their own appointments
        if user_role != UserRole.PATIENT or appointment.patient_id != user_id:
            raise HTTPException(403, "You can only cancel your own appointments")

        await self.appointment_repo.delete(appointment)
        return {"message": "Appointment cancelled successfully"}
