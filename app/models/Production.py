from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Production(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    year: int
    quantity: int
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")

    __table_args__ = {'info': {'model_class': 'Production'}}
