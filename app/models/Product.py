from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from app.models import Production


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category: str
    productions: List[Production] = Relationship(back_populates="product")

    __table_args__ = {'info': {'model_class': 'Product'}}
