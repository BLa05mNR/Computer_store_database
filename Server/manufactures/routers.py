from typing import List
from fastapi import APIRouter
from Server.models.models import New_ID
from Server.manufactures.models import  Basemodel_manufacturers, New_manufacturer
from Server.manufactures.resolvers import (get_manufacturers, get_manufacturer,
                                           add_new_manufacturers, update_manufacturer,
                                           delete_manufacturer)


router = APIRouter()

@router.get('/', tags=["manufacturers"])
def router_manufacturers() -> List[Basemodel_manufacturers]:
    return get_manufacturers()

@router.get('/{manufacturer_id}', tags=["manufacturers"])
def router_get_manufacturer(man_id: int) -> Basemodel_manufacturers:
    return get_manufacturer(man_id)

@router.post ('/', tags=["manufacturers"])
def router_new_manufacturer(new_man: New_manufacturer) -> New_ID:
    return add_new_manufacturers(new_man)

@router.put('/{manufacturer_id}', tags=["manufacturers"])
def router_update_manufacturer(man_id: int, manufacturer: New_manufacturer) -> New_ID:
    return update_manufacturer(man_id, manufacturer)

@router.delete('/{manufacturer_id}', tags=["manufacturers"])
def router_delete_manufacturer(man_id: int) -> New_ID:
    return delete_manufacturer(man_id)