# app/main.py

from typing import List
from fastapi import FastAPI, HTTPException
from app.models import StudentBase, Student
from app.crud import create_student, get_all_students
from app.database import init_db

app = FastAPI()

# Initialize database connection at startup
@app.on_event("startup")
async def startup_db():
    await init_db()  # Initialize MongoDB connection

# POST endpoint to add a student
@app.post("/students/", response_model=dict, status_code=201)
async def add_student(student: StudentBase):
    # Create student in the database
    created_student = await create_student(student)
    return created_student  # Return only the 'id' field

# GET endpoint to fetch all students
@app.get("/students/", response_model=List[Student])
async def get_students():
    students = await get_all_students()
    if not students:
        raise HTTPException(status_code=404, detail="No students found")
    return students