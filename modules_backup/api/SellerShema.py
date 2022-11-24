#   timestamp: 2022-10-29T02:15:05+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field



class Data(BaseModel):
    can_use_global_product: Optional[bool] = Field(None, description='')


class ApiSellerManageGlobalProductCheckGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data] = None


class ActiveShop(BaseModel):
    shop_id: Optional[int] = Field(None, description='')
    shop_region: Optional[str] = Field(None, description='')


class Data1(BaseModel):
    active_shops: Optional[List[ActiveShop]] = None


class ApiSellerGlobalActiveShopsGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data1] = None
