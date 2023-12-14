from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Basemodel_orders(BaseModel):
    id: int
    client_id: int
    date: Optional[datetime] = None
    status: str
    address_delivery: str
    method_payment: str

class Basemodel_certain_order(BaseModel):
    id: int
    client_id: int
    status: str

class Basemodel_New_order(BaseModel):
    client_id: int
    date: Optional[datetime] = None
    status: str
    address_delivery: str
    method_payment: str

class Update_order(BaseModel):
    status: Optional[str]