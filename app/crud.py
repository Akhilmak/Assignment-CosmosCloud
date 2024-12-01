from typing import Dict, Optional
from fastapi import HTTPException
from app.database import get_database
from app.models import StudentBase
from bson import ObjectId


async def create_student(student: StudentBase):
    db = await get_database()
    student_dict = student.dict()
    result = await db.students.insert_one(student_dict)
    new_student = await db.students.find_one({"_id": result.inserted_id})
    return {"id": str(new_student["_id"])}


async def get_students_with_filters(country: Optional[str] = None, age: Optional[int] = None):
    db = await get_database()
    
    filters = {}
    
    if country:
        filters['address.country'] = country
    if age is not None:
        filters['age'] = {'$gte': age}
    
    students_cursor = db.students.find(filters)
    
    students_list = []
    async for student in students_cursor:
        student_data = {"name": student["name"], "age": student["age"]}
        students_list.append(student_data)
    
    return students_list

async def get_student_by_id(student_id: str):
    db = await get_database()
    
    try:
        student_object_id = ObjectId(student_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid student ID format")

    student = await db.students.find_one({"_id": student_object_id})
    
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student_data = {
        "name": student["name"],
        "age": student["age"],
        "address": {
            "city": student["address"]["city"],
            "country": student["address"]["country"]
        }
    }
    
    return student_data


async def update_student_by_id(student_id: str, student_data: Dict):
    db = await get_database()
    
    try:
        student_object_id = ObjectId(student_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid student ID format")
    
    result = await db.students.update_one(
        {"_id": student_object_id}, 
        {"$set": student_data}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return {"message": "Student updated successfully"}


async def delete_student_by_id(id: str):
    db = await get_database()
    
    if not ObjectId.is_valid(id):
        return None
    
    result = await db.students.delete_one({"_id": ObjectId(id)})
    
    if result.deleted_count == 0:
        return None
    
    return {"message": "Student deleted successfully"}
