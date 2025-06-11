# To declare a request body, you use Pydantic models with all their power and benefits.


from fastapi import FastAPI
from pydantic import BaseModel


class Todo(BaseModel):
    id:int
    item:str
    # name: str
    # description: str | None = None
    # price: float
    # tax: float | None = None