from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGO_URI

client: AsyncIOMotorClient = None


async def init_db():
    global client
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        # Ping the server to confirm the connection
        await client.admin.command('ping')
        print(client)
        print("Successfully connected to MongoDB Atlas!")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise e

async def get_database():
    if client is None:
        await init_db()
    return client.Student_Management_System

# Get the collection reference
async def get_students_collection():
    db = await get_database()
    return db.Students  # Collection name: Students





