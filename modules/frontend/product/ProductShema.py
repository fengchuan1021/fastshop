#   timestamp: 2022-09-21T05:46:37+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, constr


class Testforxxx(BaseModel):
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    id: Optional[int] = None
    order_id: int
    product_id: int


class Fff(BaseModel):
    fff: str


class Gender(Enum):
    man = 'man'
    woman = 'woman'


class FrontendProductIdLangOutShema(BaseModel):
    productName: str
    productDescription: str
    brand: str
    price: float
