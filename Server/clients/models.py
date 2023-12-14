from pydantic import BaseModel


class Basemodel_Clients(BaseModel):
    id: int
    name: str
    full_name: str
    email: str
    login: str
    password: str

class Basemodel_NewClient(BaseModel):
    name: str
    full_name: str
    email: str
    login: str
    password: str

class Basemodel_correct_client(BaseModel):
    id: int
    name: str
    full_name: str


class UpdateClient(BaseModel):
    name: str
    full_name: str


