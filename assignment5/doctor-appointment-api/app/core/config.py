import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite+aiosqlite:///./doctor.db"
)

JWT_SECRET = "SUPER_SECRET_KEY"
JWT_ALGORITHM = "HS256"
