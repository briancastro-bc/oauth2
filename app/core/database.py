from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings

async def connect_db():
    client = AsyncIOMotorClient(settings.MONGO_URI)