from pydantic import BaseModel,EmailStr
from typing import Optional

class Student(BaseModel):
    name: str ='himu'
    age: Optional[int]=None
    email:EmailStr
new_std={'age':'54','email':'himu@gmail.com'}

std=Student(**new_std)

print(std)