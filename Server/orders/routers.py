from typing import List
from fastapi import APIRouter

from Server.models.models import New_ID
from Server.orders.models import (Basemodel_orders, Basemodel_certain_order,
                                  Basemodel_New_order, Update_order)
from Server.orders.resolvers import (get_orders, get_order, add_new_order,
                                     delete_order, update_order)

router = APIRouter()

@router.get('/', tags=["orders"])
def router_orders() -> List[Basemodel_orders]:
    return get_orders()

@router.get('/{order_id}', tags=["orders"])
def router_certain_order(order_id: int) -> Basemodel_certain_order:
    return get_order(order_id)

@router.post('/', tags=["orders"])
def router_new_order(new_order: Basemodel_New_order) -> New_ID:
    return add_new_order(new_order)

@router.put('/{order_id}', tags=["orders"])
def router_update_order(order_id: int, new_status: Update_order) -> New_ID:
    return update_order(order_id, new_status)

@router.delete('/{order_id}', tags=["orders"])
def router_delete_order(id: int) -> New_ID:
    return delete_order(id)