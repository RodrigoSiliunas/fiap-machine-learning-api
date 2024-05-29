from typing import Optional
from sqlmodel import SQLModel, Field


class Processing(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)
    name: str
    category: str
    subcategory: str
    quantity: int
    year: int

    __table_args__ = {'info': {'model_class': 'Processing'}}
