#   timestamp: 2022-10-06T14:58:24+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field







class Datum(BaseModel):
    company_id: Optional[str]
    compayn_name: Optional[str]
    warehouse_id: str
    warehouse_name: str
    class Config:
        orm_mode = True


class BackendShopWarehouselistPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Optional[List[Datum]] = None
class BackendShopAddwarehousePostRequest(BaseModel):
    warehouse_name: str
    warehouse_mark: Optional[str] = ''



class BackendShopAddwarehousePostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None