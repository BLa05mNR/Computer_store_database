from pydantic import BaseModel


class Basemodel_products(BaseModel):
    id: int
    product_name: str
    description: str
    price: int
    quantity_in_stock: int
    manufacturer_id: int
    category_id: int
    model: str
    specifications: str


class New_product(BaseModel):
    product_name: str
    description: str
    price: int
    quantity_in_stock: int
    manufacturer_id: int
    category_id: int
    model: str
    specifications: str


class Update_product(BaseModel):
    product_name: str
    description: str
    price: int
    quantity_in_stock: int
    model: str
    specifications: str