from datetime import datetime

from Server.db_manager import base_manager
from Server.models.models import New_ID
from Server.orders.models import (Basemodel_orders, Basemodel_certain_order,
                                  Basemodel_New_order, Update_order)


def get_orders():
    res = base_manager.execute("SELECT O.id, C.id, O.date, O.status, O.address_delivery, O.method_payment "
                               "FROM orders O INNER JOIN clients C ON O.client_id = C.id", many=True)
    orders = []
    for order in res['data']:
        print()
        orders.append(Basemodel_orders(id=order[0], client_id=order[1],
                                       date=datetime.strptime(order[2],'%Y-%m-%d %H:%M:%S.%f'),
                                       status=order[3], address_delivery=order[4], method_payment=order[5]))
    return orders

def get_order(order_id: int):
    res = base_manager.execute("SELECT O.id, O.client_id, O.status "
                               "FROM orders O WHERE id = ? ",
                               args=(order_id, ))
    print(res)
    return Basemodel_certain_order(id=order_id, client_id=res['data'][0][1], status=res['data'][0][2])

def add_new_order(new_order: Basemodel_New_order):
    res = base_manager.execute("INSERT INTO orders(client_id, date, status, address_delivery, method_payment) "
                               "VALUES (?,?,?,?,?) "
                               "RETURNING id", args=(new_order.client_id, new_order.date, new_order.status,
                                                     new_order.address_delivery, new_order.method_payment))
    return New_ID(code=res['code'], id=res['data'][0][0])

def update_order(order_id: int, order: Update_order):
    res = base_manager.execute("UPDATE orders SET status = ? WHERE id = ? ",
                               args=(order.status, order_id))
    return New_ID(id=order_id, code=res['code'])

def delete_order(order_id: int):
    res = base_manager.execute("DELETE FROM orders WHERE id = ?",
                               args=(order_id,))
    return New_ID(code=res['code'], id=order_id)