import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client: AsyncIOMotorClient = None
async def init_db():
    global client
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        await client.admin.command('ping')  # Ping the server to confirm the connection
        print("Successfully connected to MongoDB Atlas!")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise e

async def get_database():
    if client is None:
        await init_db()
    return client.Student_Management_System
