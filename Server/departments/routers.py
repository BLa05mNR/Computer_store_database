from typing import List
from fastapi import APIRouter
from Server.models.models import New_ID
from Server.departments.models import (Basemodel_departments, New_department)
from Server.departments.resolvers import (get_departments, get_department,
                                          add_new_departments, update_department,
                                          delete_department)


router = APIRouter()

@router.get('/', tags=["departments"])
def router_departments() -> List[Basemodel_departments]:
    return get_departments()

@router.get('/{department_id}', tags=["departments"])
def router_department(department_id: int) -> Basemodel_departments:
    return get_department(department_id)

@router.post('/', tags=["departments"])
def router_new_department(new_departments: New_department) -> New_ID:
    return add_new_departments(new_departments)

@router.put('/{department_id}', tags=["departments"])
def router_update_department(department_id: int, new_department: New_department) -> New_ID:
    return update_department(department_id, new_department)

@router.delete('/{department_id}', tags=["departments"])
def router_delete_department(id: int) -> New_ID:
    return delete_department(id)