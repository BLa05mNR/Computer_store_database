import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from Server.db_manager import base_manager
from Server.settings import SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH
from routers import (clients_router, orders_router, departments_router,
                     categories_routers, staff_router, manufacturers_router,
                     products_router)

app = FastAPI(
    title='Computer_shop_server'
)

app.include_router(clients_router, prefix='/clients')
app.include_router(departments_router, prefix='/departments')
app.include_router(categories_routers, prefix='/categories')
app.include_router(staff_router, prefix='/staff')
app.include_router(orders_router, prefix='/orders')
app.include_router(products_router, prefix='/products')
app.include_router(manufacturers_router, prefix='/manufacturers')


@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH)
    uvicorn.run(app="start_server:app", host="127.0.0.1",  port=8000, reload=True)