from pydantic import BaseModel, EmailStr
from app.utils.enums import UserRole


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    role: UserRole

    class Config:
        from_attributes = True
