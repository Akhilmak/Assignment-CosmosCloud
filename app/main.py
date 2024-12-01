from fastapi import FastAPI, HTTPException
from typing import List
from .models import Student
from .crud import create_student, get_students, get_student_by_id, update_student, delete_student
from .database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    try:
        await init_db()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Error initializing database: {e}")

@app.post("/students/", response_model=Student)
async def add_student(student: Student):
    try:
        return await create_student(student)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating student: {e}")

@app.get("/students/", response_model=List[Student])
async def list_students():
    try:
        return await get_students()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing students: {e}")

@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: str):
    try:
        student = await get_student_by_id(student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return student
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting student: {e}")

@app.put("/students/{student_id}", response_model=Student)
async def modify_student(student_id: str, student: Student):
    try:
        return await update_student(student_id, student)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating student: {e}")

@app.delete("/students/{student_id}")
async def remove_student(student_id: str):
    try:
        await delete_student(student_id)
        return {"message": "Student deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting student: {e}")