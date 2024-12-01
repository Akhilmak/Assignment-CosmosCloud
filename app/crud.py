from fastapi import HTTPException, status
from .database import get_database, get_students_collection
from .models import Student
from bson import ObjectId

db = get_database()
print(db)

# Assume db is already initialized and connected
async def create_student(student: Student):
    try:
        # Get the students collection (ensure it's accessed asynchronously)
        students_collection = await get_students_collection()
        
        # Convert Pydantic model to dictionary
        student_dict = student.dict()
        
        # Insert the student document into the collection asynchronously
        result = await students_collection.insert_one(student_dict)
        
        # Add MongoDB ObjectId to the response data as 'id'
        student_dict["id"] = str(result.inserted_id)
        
        # Return the created student
        return student_dict
    except Exception as e:
        # Raise an HTTP exception with error details if something goes wrong
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating student: {str(e)}"
        )

async def get_students():
    try:
        students = []
        async for student in db.students.find():
            students.append(Student(**student))
        return students
    except Exception as e:
        raise

async def get_student_by_id(student_id: str):
    try:
        student = await db.students.find_one({"_id": ObjectId(student_id)})
        if student:
            return Student(**student)
        return None
    except Exception as e:
        raise

async def update_student(student_id: str, student: Student):
    try:
        updated_student = await db.students.find_one_and_update(
            {"_id": ObjectId(student_id)},
            {"$set": student.dict()},
            return_document=True
        )
        if updated_student:
            return Student(**updated_student)
        return None
    except Exception as e:
        raise

async def delete_student(student_id: str):
    try:
        await db.students.delete_one({"_id": ObjectId(student_id)})
    except Exception as e:
        raise