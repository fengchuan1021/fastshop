#   timestamp: 2022-10-19T08:41:48+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field
from pydantic.utils import GetterDict


# class MyVariantGetter(GetterDict):
#     def get(self, key: str, default: Any) -> Any:
#
#         if key=='data':
#             tmp=self._obj.Images
#             return tmp[0].image_url if tmp else ''
#
#         else:
#             return getattr(self._obj,key)
# class Product(BaseModel):
#     product_id:str


    # class Config:
    #     orm_mode = True
        #getter_dict = MyVariantGetter
