import databases
import sqlalchemy
from fastapi import FastAPI
from typing import List
from HW_fastAPI_02.tables import user_table, product_table, order_table, metadata_db
from HW_fastAPI_02.models import User, UserIn, Product, ProductIn, Order, OrderIn

DATABASE_URL = "sqlite:///my_db.db"

database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(DATABASE_URL,
                                  connect_args={"check_same_thread": False})
metadata_db.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# Users
@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = user_table.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@app.get("/users/", response_model=List[User])
async def read_users():
    query = user_table.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_users(user_id: int):
    query = user_table.select().where(user_table.c.id == user_id)
    return await database.fetch_one(query)


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = user_table.update().where(user_table.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = user_table.delete().where(user_table.c.id == user_id)
    await database.execute(query)
    return {"message": 'User deleted'}


# Products
@app.post("/products/", response_model=Product)
async def create_product(product: ProductIn):
    query = product_table.insert().values(**product.dict())
    last_record_id = await database.execute(query)
    return {**product.dict(), "id": last_record_id}


@app.get("/products/", response_model=List[Product])
async def read_products():
    query = product_table.select()
    return await database.fetch_all(query)


@app.get("/products/{product_id}", response_model=Product)
async def read_products(product_id: int):
    query = product_table.select().where(product_table.c.id == product_id)
    return await database.fetch_one(query)


@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = product_table.update().where(product_table.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = product_table.delete().where(product_table.c.id == product_id)
    await database.execute(query)
    return {"message": 'Product deleted'}


#Order
@app.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    query = order_table.insert().values(**order.dict())
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


@app.get("/orders/", response_model=List[Order])
async def read_orders():
    query = order_table.select()
    return await database.fetch_all(query)


@app.get("/orders/{order_id}", response_model=Order)
async def read_orders(order_id: int):
    query = order_table.select().where(order_table.c.id == order_id)
    return await database.fetch_one(query)


@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = order_table.update().where(order_table.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = order_table.delete().where(order_table.c.id == order_id)
    await database.execute(query)
    return {"message": 'Order deleted'}
