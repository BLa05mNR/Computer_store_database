from typing import List
from fastapi import APIRouter
from Server.models.models import New_ID
from Server.products.models import Basemodel_products, New_product, Update_product
from Server.products.resolvers import (get_products, get_product, add_new_product,
                                       update_product, delete_product)


router = APIRouter()

@router.get('/', tags=["products"])
def router_products() -> List[Basemodel_products]:
    return get_products()

@router.get('/{product_id}', tags=["products"])
def router_product(id: int) -> Basemodel_products:
    return get_product(id)

@router.post('/', tags=["products"])
def router_new_product(new_product: New_product) -> New_ID:
    return add_new_product(new_product)

@router.put('/{product_id}', tags=["products"])
def router_new_product(id: int, product: Update_product) -> New_ID:
    return update_product(id, product)

@router.delete('/{product_id}', tags=["products"])
def router_delete_product(id: int) -> New_ID:
    return delete_product(id)