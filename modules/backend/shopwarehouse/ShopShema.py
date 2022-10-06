#   timestamp: 2022-10-06T14:58:24+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field



class BackendShopAddshopPostRequest(BaseModel):
    shop_name: str
    warehouse_id: str
    warehouse_name: str



class BackendShopAddshopPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None


class BackendShopShoplistPostRequest(BaseModel):
    pagesize: Optional[int] = 20
    pagenum: Optional[int] = 1
    filter: Optional[Dict[str, Any]] = None



class Datum(BaseModel):
    shop_name: str
    shop_id: str
    company_id: Optional[str]
    compayn_name: Optional[str]
    warehouse_id: str
    warehouse_name: str
    class Config:
        orm_mode = True

class BackendShopShoplistPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Optional[List[Datum]] = None



