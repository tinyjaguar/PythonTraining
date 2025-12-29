from enum import Enum

class UserRole(str, Enum):
    DOCTOR = "DOCTOR"
    PATIENT = "PATIENT"
