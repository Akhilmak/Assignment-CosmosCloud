
from app.database import get_database
from app.models import StudentBase
from bson import ObjectId


# Create a new student and return only the 'id'
async def create_student(student: StudentBase):
    db = await get_database()
    student_dict = student.dict()  # Convert to dictionary
    result = await db.students.insert_one(student_dict)  # Insert into MongoDB collection
    new_student = await db.students.find_one({"_id": result.inserted_id})  # Retrieve the inserted student
    return {"id": str(new_student["_id"])}  # Return only the id field


async def get_all_students():
    db = await get_database()
    students_cursor = db.students.find()  # MongoDB find all students
    students_list = []
    
    async for student in students_cursor:
        student_data = {"id": str(student["_id"]), **student}  # Convert _id to id
        students_list.append(student_data)
    
    return students_list
