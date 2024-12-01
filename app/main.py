from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from app.models import StudentBase, Student, StudentUpdateRequest
from app.crud import create_student, delete_student_by_id, get_student_by_id, get_students_with_filters, update_student_by_id
from app.database import init_db

app = FastAPI()
@app.on_event("startup")
async def startup_db():
    await init_db() 


@app.post("/students/", response_model=dict, status_code=201)
async def add_student(student: StudentBase):
    created_student = await create_student(student)
    return created_student 


@app.get("/students/", response_model=dict, status_code=200)
async def list_students(
    country: Optional[str] = Query(None, description="Filter students by country"),
    age: Optional[int] = Query(None, description="Filter students by age (age >= provided value)")
):
    
    students = await get_students_with_filters(country=country, age=age)
    
    if not students:
        raise HTTPException(status_code=404, detail="No students found matching the filters")
    
    return {"data": students}


@app.get("/students/{id}", response_model=dict, status_code=200)
async def fetch_student(id: str):
    student = await get_student_by_id(id)
    
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return student


@app.patch("/students/{id}", status_code=204)
async def update_student(id: str, student: StudentUpdateRequest):
   
    update_data = {key: value for key, value in student.dict(exclude_unset=True).items()}
    
    
    response = await update_student_by_id(id, update_data)
    
    
    if not response:
        raise HTTPException(status_code=404, detail="Student not found")

    
    return None


@app.delete("/students/{id}", response_model=dict, status_code=200)
async def delete_student(id: str):
    
    result = await delete_student_by_id(id)
    
    
    if not result:
        raise HTTPException(status_code=404, detail="Student not found")
    
   
    return {}
