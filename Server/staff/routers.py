from typing import List
from fastapi import APIRouter

from Server.models.models import New_ID
from Server.staff.models import (Basemodel_Staff, Basemodel_certain_staff,
                                 New_staff, Update_staff)

from Server.staff.resolvers import (get_staffs, get_staff,
                                    add_new_staff, update_staff, delete_staff)

router = APIRouter()


@router.get('/', tags=["staff"])
def router_staffs() -> List[Basemodel_Staff]:
    return get_staffs()

@router.get('/{staff_id}', tags=["staff"])
def router_staff(staff_id: int) -> Basemodel_certain_staff:
    return get_staff(staff_id)

@router.post('/', tags=["staff"])
def router_new_staff(new_staff: New_staff) -> New_ID:
    return add_new_staff(new_staff)

@router.put('/{staff_id}', tags=["staff"])
def router_update_staff(staff_id: int, staff: Update_staff) -> New_ID:
    return update_staff(staff_id, staff)

@router.delete('/{staff_id}', tags=["staff"])
def router_delete(staff_id: int) -> New_ID:
    return delete_staff(staff_id)