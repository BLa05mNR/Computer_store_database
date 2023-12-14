from pydantic import BaseModel


class Basemodel_manufacturers(BaseModel):
    id: int
    name: str
    contact_information: str

class New_manufacturer(BaseModel):
    name: str
    contact_information: str