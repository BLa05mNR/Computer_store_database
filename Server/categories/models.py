from pydantic import BaseModel


class Basemodel_categories(BaseModel):
    id: int
    name: str
    description: str


class New_category(BaseModel):
    name: str
    description: str