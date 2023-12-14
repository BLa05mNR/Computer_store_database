from Server.db_manager import base_manager
from Server.clients.models import (Basemodel_Clients, Basemodel_correct_client,
                                   Basemodel_NewClient, UpdateClient)
from Server.models.models import New_ID


def get_clients():
    res = base_manager.execute("SELECT C.id, C.name, C.full_name,"
                               " C.email, C.login, C.password "
                               "FROM clients C ", many=True)
    clients = []
    for client in res['data']:
        print()
        clients.append(Basemodel_Clients(id=client[0], name=client[1], full_name=client[2],
                                         email=client[3], login=client[4], password=client[5]))
    return clients

def get_client(client_id: int):
    res = base_manager.execute("SELECT C.id, C.name, C.full_name "
                               "FROM clients C WHERE id = ? ",
                               args=(client_id, ))
    print(res)
    return Basemodel_correct_client(id=client_id, name=res['data'][0][1], full_name=res['data'][0][2])

def add_new_client(new_user: Basemodel_NewClient):
    res = base_manager.execute("INSERT INTO clients(name, full_name, email, login, password) "
                               "VALUES (?, ?, ?, ?, ?) "
                               "RETURNING id", args=(new_user.name, new_user.full_name, new_user.email,
                                                     new_user.login, new_user.password))
    return New_ID(code=res['code'], id=res['data'][0][0])

def update_client(client_id: int, client: UpdateClient):
    res = base_manager.execute("UPDATE clients SET name = ?, full_name = ? WHERE id = ? ",
                               args=(client.name, client.full_name, client_id, ))
    return New_ID(code=res['code'], id=client_id)

def delete_current_user(client_id: int):
    res = base_manager.execute("DELETE FROM clients WHERE id = ?",
                               args=(client_id,))
    return New_ID(id=client_id, code=res['code'])