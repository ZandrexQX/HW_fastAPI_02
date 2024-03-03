from sqlalchemy import INTEGER, ForeignKey, String, Float, Boolean, Column, Table, MetaData


metadata_db = MetaData()


user_table = Table(
    'Users',
    metadata_db,
    Column('id', INTEGER, primary_key=True),
    Column('name', String(32)),
    Column('surname', String(32)),
    Column('email', String(64)),
    Column('password', String(64))
)


product_table = Table(
    'Products',
    metadata_db,
    Column('id', INTEGER, primary_key=True),
    Column('title', String(32)),
    Column('description', String(1000), nullable=True),
    Column('price', Float)
)


order_table = Table(
    'Orders',
    metadata_db,
    Column('id', INTEGER, primary_key=True),
    Column('user_id', INTEGER, ForeignKey("Users.id")),
    Column('product_id', INTEGER, ForeignKey("Products.id")),
    Column('date', String(32)),
    Column('status', Boolean)
)
