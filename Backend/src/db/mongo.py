from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
mongo_db = client["museumnrdb"]

def get_mongo_db():
    return mongo_db
