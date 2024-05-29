from typing import Optional
from sqlmodel import SQLModel, Field


class Importation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)
    country: str
    category: str
    weight: int
    value: int
    year: int

    __table_args__ = {'info': {'model_class': 'Importation'}}
