from fastapi import APIRouter, Depends
from app.schemas.auth import RegisterRequest, LoginRequest, ForgotPasswordRequest
from app.services.auth_service import AuthService
from app.repositories.user_repo import UserRepository
from app.db.session import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(payload: RegisterRequest, db=Depends(get_db)):
    service = AuthService(UserRepository(db))
    user = await service.register(payload)
    return {"id": user.id}

@router.post("/login")
async def login(payload: LoginRequest, db=Depends(get_db)):
    service = AuthService(UserRepository(db))
    token = await service.login(payload)
    return {"access_token": token}

@router.post("/forgot-password")
async def forgot_password(payload: ForgotPasswordRequest, db=Depends(get_db)):
    service = AuthService(UserRepository(db))
    result = await service.forgot_password(payload)
    return result
