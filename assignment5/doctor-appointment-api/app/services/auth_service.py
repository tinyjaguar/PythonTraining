from app.repositories.user_repo import UserRepository
from app.db.models import User
from app.core.security import hash_password, verify_password, create_token
from fastapi import HTTPException

class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def register(self, payload):
        if await self.repo.get_by_email(payload.email):
            raise HTTPException(400, "User exists")

        user = User(
            email=payload.email,
            password_hash=hash_password(payload.password),
            name=payload.name,
            role=payload.role
        )
        return await self.repo.create(user)

    async def login(self, payload):
        user = await self.repo.get_by_email(payload.email)
        if not user or not verify_password(payload.password, user.password_hash):
            raise HTTPException(401, "Invalid credentials")

        return create_token({"user_id": user.id, "role": user.role})

    async def forgot_password(self, payload):
        user = await self.repo.get_by_email(payload.email)
        if not user:
            # For security, we don't reveal if email exists or not
            return {"message": "If the email exists, a reset link has been sent"}

        # In a real application, you would send an email here
        # For this assignment, we'll just return a mock response
        return {"message": "Password reset link sent to your email"}
