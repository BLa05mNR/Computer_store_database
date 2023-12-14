from pydantic import BaseModel

class Basemodel_departments(BaseModel):
    id: int
    department_name: str
    description: str

class New_department(BaseModel):
    department_name: str
    description: str