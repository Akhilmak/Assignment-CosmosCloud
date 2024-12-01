# app/models.py

from pydantic import BaseModel
from typing import Optional

# Define the Address model (embedded object in Student)
class Address(BaseModel):
    city: str
    country: str

# Define the base student model (including Address)
class StudentBase(BaseModel):
    name: str
    age: int
    address: Address  # Embedded Address object

# Define the response model for Student (includes the id)
class Student(StudentBase):
    id: str

    class Config:
        orm_mode = True
