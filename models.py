from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    city: str
    country: str


class StudentBase(BaseModel):
    name: str
    age: int
    address: Address  
class Student(StudentBase):
    id: str

    class Config:
        orm_mode = True

class StudentUpdateRequest(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[dict] = None 