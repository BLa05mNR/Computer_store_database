from Server.db_manager import base_manager
from Server.manufactures.models import Basemodel_manufacturers, New_manufacturer
from Server.models.models import New_ID


def get_manufacturers():
    res = base_manager.execute("SELECT M.id, M.name, M.contact_information "
                               "FROM manufacturers M ", many=True)
    manufacturers = []
    for man in res['data']:
        print()
        manufacturers.append(Basemodel_manufacturers(id=man[0], name=man[1], contact_information=man[2]))
    return manufacturers

def get_manufacturer(man_id: int):
    res = base_manager.execute("SELECT M.id, M.name, M.contact_information "
                               "FROM manufacturers M WHERE id = ? ",
                               args=(man_id, ))
    print(res)
    return Basemodel_manufacturers(id=man_id, name=res['data'][0][1],
                                   contact_information=res['data'][0][2])

def add_new_manufacturers(new_man: New_manufacturer):
    res = base_manager.execute("INSERT INTO manufacturers(name, contact_information)"
                               "VALUES (?,?) "
                               "RETURNING id", args=(new_man.name, new_man.contact_information, ))
    return New_ID(code=res['code'], id=res['data'][0][0])

def update_manufacturer(man_id: int, man: New_manufacturer):
    res = base_manager.execute("UPDATE manufacturers SET name = ?, contact_information = ?"
                               "WHERE id = ? ", args=(man.name, man.contact_information, man_id))
    return New_ID(code=res['code'], id=man_id)

def delete_manufacturer(man_id: int):
    res = base_manager.execute("DELETE FROM manufacturers WHERE id = ? ",
                               args=(man_id, ))
    return New_ID(code=res['code'], id=man_id)