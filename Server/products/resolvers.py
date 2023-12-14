from Server.db_manager import base_manager
from Server.products.models import Basemodel_products, New_product, Update_product
from Server.models.models import New_ID


def get_products():
    res = base_manager.execute("SELECT P.id, P.product_name, P.description, "
                               "P.price, P.quantity_in_stock, M.id, CT.id, P.model, P.specifications "
                               "FROM products P "
                               "INNER JOIN manufacturers M ON P.manufacturer_id = M.id "
                               "INNER JOIN categories CT ON P.category_id = CT.id", many=True)
    products = []
    for p in res['data']:
        print()
        products.append(Basemodel_products(id=p[0], product_name=p[1], description=p[2],
                                           price=p[3], quantity_in_stock=p[4], manufacturer_id=p[5],
                                           category_id=p[6], model=p[7], specifications=p[8]))
    return products

def get_product(p_id: int):
    res = base_manager.execute("SELECT P.id, P.product_name, P.description, P.price, "
                               "P.quantity_in_stock, P.manufacturer_id, P.category_id, P.model, P.specifications "
                               "FROM products P WHERE id = ? ",
                               args=(p_id, ))
    print(res)
    return Basemodel_products(id=p_id, product_name=res['data'][0][1], description=res['data'][0][2],
                              price=res['data'][0][3], quantity_in_stock=res['data'][0][4],
                              manufacturer_id=res['data'][0][5], category_id=res['data'][0][6],
                              model=res['data'][0][7], specifications=res['data'][0][8])

def add_new_product(new_product: New_product):
    res = base_manager.execute("INSERT INTO products(product_name, description, price, "
                               "quantity_in_stock, manufacturer_id, category_id, model, specifications) "
                               "VALUES (?,?,?,?,?,?,?,?) "
                               "RETURNING id ", args=(new_product.product_name, new_product.description,
                                                                  new_product.price, new_product.quantity_in_stock,
                                                                  new_product.manufacturer_id, new_product.category_id,
                                                                  new_product.model, new_product.specifications))
    return New_ID(code=res['code'], id=res['data'][0][0])

def update_product(product_id: int, product: Update_product):
    res = base_manager.execute("UPDATE products SET product_name = ?, description = ?,"
                               "price = ?, quantity_in_stock = ?, model = ?, "
                               "specifications = ? WHERE id = ? ",
                               args=(product.product_name, product.description, product.price,
                               product.quantity_in_stock, product.model, product.specifications,
                               product_id))
    return New_ID(code=res['code'], id=product_id)

def delete_product(product_id: int):
    res = base_manager.execute("DELETE FROM products WHERE id = ? ",
                               args=(product_id, ))
    return New_ID(code=res['code'], id=product_id)