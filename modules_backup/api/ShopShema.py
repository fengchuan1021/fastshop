#   timestamp: 2022-10-29T02:15:06+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field



class ShopListItem(BaseModel):
    shop_id: Optional[str] = Field(None, description='')
    shop_name: Optional[str] = Field(None, description='')
    region: Optional[str] = Field(
        None,
        description='The cross-border shop region (GB) is empty before it is approved, so if the following merchant statuses are <br>new create/reject/pending, the obtained region values are empty',
    )
    type: Optional[int] = Field(
        None, description='1: "CROSS BORDER"<br>2: "LOCAL TO LOCAL"'
    )


class Data(BaseModel):
    shop_list: Optional[List[ShopListItem]] = None


class ApiShopGetAuthorizedShopGetResponse(BaseModel):
    code: Optional[int] = Field(None, description='')
    message: Optional[str] = Field(None, description='')
    request_id: Optional[str] = Field(None, description='Request log')
    data: Optional[Data] = None
