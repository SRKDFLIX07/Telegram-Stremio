import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("MONGO_URI not set")

client = AsyncIOMotorClient(MONGO_URI)
db = client["yourdbname"]   # apna db name yahan likho

