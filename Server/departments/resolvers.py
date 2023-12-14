from Server.db_manager import base_manager
from Server.departments.models import (Basemodel_departments, New_department)
from Server.models.models import New_ID


def get_departments():
    res = base_manager.execute("SELECT D.id, D.department_name, D.description "
                               "FROM departments D", many=True)
    departments = []
    for department in res['data']:
        print()
        departments.append(Basemodel_departments(id=department[0], department_name=department[1],
                                                 description=department[2]))
    return departments

def get_department(department_id: int):
        res = base_manager.execute("SELECT D.id, D.department_name, D.description "
                                   "FROM departments D WHERE id = ? ",
                                   args=(department_id,))
        print(res)
        return Basemodel_departments(id=department_id, department_name=res['data'][0][1],
                                     description=res['data'][0][2])

def add_new_departments(new_departments: New_department):
    res = base_manager.execute("INSERT INTO departments(department_name, description) "
                               "VALUES (?,?) "
                               "RETURNING id", args=(new_departments.department_name, new_departments.description))
    return New_ID(code=res['code'], id=res['data'][0][0])

def update_department(department_id: int, department: New_department):
    res = base_manager.execute("UPDATE departments SET department_name = ?, description = ? WHERE id = ? ",
                               args=(department.department_name, department.description, department_id))
    return New_ID(code=res['code'], id=department_id)

def delete_department(department_id: int):
    res = base_manager.execute("DELETE FROM departments WHERE id = ?",
                               args=(department_id, ))
    return New_ID(code=res['code'], id=department_id)