from typing import Optional
from sqlmodel import SQLModel, Field


class Commercialization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")
    quantity: int
    year: int

    __table_args__ = {'info': {'model_class': 'Commercialization'}}
