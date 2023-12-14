from typing import List
from fastapi import APIRouter
from Server.clients.models import (Basemodel_Clients, Basemodel_correct_client,
                                   Basemodel_NewClient, UpdateClient)
from Server.clients.resolvers import (get_clients, add_new_client,
                                      delete_current_user, update_client, get_client)
from Server.models.models import New_ID

router = APIRouter()


@router.get('/', tags=["clients"])
def router_clients() -> List[Basemodel_Clients]:
    return get_clients()

@router.get('/{client_id}', tags=["clients"])
def router_correct_client(client_id: int) -> Basemodel_correct_client:
    return get_client(client_id)

@router.post('/', tags=["clients"])
def router_new_client(new_client: Basemodel_NewClient) -> New_ID:
    return add_new_client(new_client)

@router.put('/{client_id}', tags=["clients"])
def router_update_client(client_id: int, new_client: UpdateClient) -> New_ID:
    return update_client(client_id, new_client)

@router.delete('/{client_id}', tags=["clients"])
def router_delete_client(id: int) -> New_ID:
    return delete_current_user(id)