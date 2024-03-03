from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(..., title="Name", max_length=32)
    surname: str = Field(..., title="Surame", max_length=32)
    email: str = Field(..., title="Email", max_length=64)
    password: str = Field(..., title="Password", max_length=64)


class User(UserIn):
    id: int


class Product(BaseModel):
    id: int
    title: str = Field(..., title="Title", max_length=32)
    description: str = Field(default=None, title="Description", max_length=1000)
    price: float = Field(..., title="Price", gt=0, le=100000)


class ProductIn(BaseModel):
    title: str = Field(..., title="Title", max_length=32)
    description: str = Field(default=None, title="Description", max_length=1000)
    price: float = Field(..., title="Price", gt=0, le=100000)


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    date: str = Field(..., title="Date Order")
    status: bool = Field(..., title="Status Order")


class Order(OrderIn):
    id: int
