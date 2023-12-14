from typing import List
from fastapi import APIRouter
from Server.categories.models import Basemodel_categories, New_category
from Server.categories.resolvers import (get_categories, gat_category, add_new_category,
                                         update_category, delete_category)
from Server.models.models import New_ID

router = APIRouter()


@router.get('/', tags=["categories"])
def router_clients() -> List[Basemodel_categories]:
    return get_categories()

@router.get('/{client_id}', tags=["categories"])
def router_correct_client(cat_id: int) -> Basemodel_categories:
    return gat_category(cat_id)

@router.post('/', tags=["categories"])
def router_new_client(new_cat: New_category) -> New_ID:
    return add_new_category(new_cat)

@router.put('/{client_id}', tags=["categories"])
def router_update_client(cat_id: int, new_client: New_category) -> New_ID:
    return update_category(cat_id, new_client)

@router.delete('/{client_id}', tags=["categories"])
def router_delete_client(id: int) -> New_ID:
    return delete_category(id)