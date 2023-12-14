from pydantic import BaseModel


class New_ID(BaseModel):
    code: int
    notification: str = "Запрос выполнен успешно :)"
    id: int