from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Basemodel_Staff(BaseModel):
    id: int
    name: str
    full_name: str
    position: str
    date_of_employment: Optional[datetime] = None
    contact_information: str
    department_id: int

class Basemodel_certain_staff(BaseModel):
    id: int
    name: str
    full_name: str
    department_id: int
    position: str

class New_staff(BaseModel):
    name: str
    full_name: str
    department_id: int
    date_of_employment: Optional[datetime] = None
    contact_information: str
    position: str

class Update_staff(BaseModel):
    name: str
    full_name: str
    contact_information: str