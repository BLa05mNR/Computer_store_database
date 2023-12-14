from datetime import datetime
from Server.db_manager import base_manager

from Server.models.models import New_ID

from Server.staff.models import Basemodel_Staff, Basemodel_certain_staff, New_staff, Update_staff


def get_staffs():
    res = base_manager.execute("SELECT S.id, S.name, S.full_name, S.position, S.date_of_employment, S.contact_information, D.id "
                               "FROM staff S "
                               "INNER JOIN departments D ON S.department_id = D.id", many=True)
    staffs = []
    for staff in res['data']:
        print()
        staffs.append(Basemodel_Staff(id=staff[0], name=staff[1], full_name=staff[2], position=staff[3],
                                      date_of_employment=datetime.strptime(staff[4],'%Y-%m-%d %H:%M:%S.%f'),
                                      contact_information=staff[5], department_id=staff[6]))
    return staffs

def get_staff(staff_id: int):
    res = base_manager.execute("SELECT S.id, S.name, S.full_name, S.department_id, S.position "
                               "FROM staff S WHERE id = ? ",
                               args=(staff_id,))
    print(res)
    return Basemodel_certain_staff(id=res['data'][0][0], name=res['data'][0][1],
                                   full_name=res['data'][0][2], department_id=res['data'][0][3], position=res['data'][0][4])

def add_new_staff(new_staff: New_staff):
    res = base_manager.execute("INSERT INTO staff(name, full_name, department_id, "
                               "date_of_employment, contact_information, position) "
                               "VALUES (?,?,?,?,?,?) "
                               "RETURNING id", args=(new_staff.name, new_staff.full_name,
                                                     new_staff.department_id, new_staff.date_of_employment,
                                                     new_staff.contact_information, new_staff.position))
    return New_ID(code=res['code'], id=res['data'][0][0])

def update_staff(staff_id: int, staff: Update_staff):
    res = base_manager.execute("UPDATE staff SET name = ?, full_name = ?, contact_information = ? WHERE id = ? ",
                               args=(staff.name, staff.full_name, staff.contact_information, staff_id))
    return New_ID(code=res['code'], id=staff_id)

def delete_staff(staff_id: int):
    res = base_manager.execute("DELETE FROM staff WHERE id = ?",
                               args=(staff_id,))
    return New_ID(code=res['code'], id=staff_id)