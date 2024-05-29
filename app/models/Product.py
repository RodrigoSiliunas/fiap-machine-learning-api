from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from app.models.Production import Production


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)
    name: str
    category: str

    __table_args__ = {'info': {'model_class': 'Product'}}
