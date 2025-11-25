import os
from motor.motor_asyncio import AsyncIOMotorClient

# Heroku config var names
MONGO_URI = os.getenv("MONGO_URI") or os.getenv("BASE_URL")
if not MONGO_URI:
    raise RuntimeError("Mongo URI not set")

client = AsyncIOMotorClient(MONGO_URI)
db = client["yourdbname"]   # apna db name yahan likho
