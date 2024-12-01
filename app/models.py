from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    email: str
    course: str

    class Config:
        orm_mode = True