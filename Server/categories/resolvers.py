from Server.db_manager import base_manager
from Server.categories.models import Basemodel_categories, New_category
from Server.models.models import New_ID


def get_categories():
    res = base_manager.execute("SELECT CT.id, CT.name, CT.description "
                               "FROM categories CT ", many=True)
    categories = []
    for cat in res['data']:
        print()
        categories.append(Basemodel_categories(id=cat[0], name=cat[1], description=cat[2]))
    return categories

def gat_category(category_id: int):
    res = base_manager.execute("SELECT CT.id, CT.name, CT.description "
                               "FROM categories CT WHERE id = ? ",
                               args=(category_id, ))
    print(res)
    return Basemodel_categories(id=category_id, name=res['data'][0][1], description=res['data'][0][2])

def add_new_category(new_cat: New_category):
    res = base_manager.execute("INSERT INTO categories(name, description) "
                               "VALUES (?, ?) "
                               "RETURNING id", args=(new_cat.name, new_cat.description, ))
    return New_ID(code=res['code'], id=res['data'][0][0])

def update_category(category_id: int, category: New_category):
    res = base_manager.execute("UPDATE categories SET name = ?, description = ? WHERE id = ? ",
                               args=(category.name, category.description, category_id, ))
    return New_ID(code=res['code'], id=category_id)

def delete_category(category_id: int):
    res = base_manager.execute("DELETE FROM categories WHERE id = ?",
                               args=(category_id,))
    return New_ID(id=category_id, code=res['code'])