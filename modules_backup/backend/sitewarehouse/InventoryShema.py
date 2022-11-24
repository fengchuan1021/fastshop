#   timestamp: 2022-10-16T06:11:02+00:00

from __future__ import annotations
from typing import Literal, List

from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field



# class BackendSitewarehouseGetproductsitestockdetailProductIdGetRequest(BaseModel):
#     pass
#
# class VariantImage(BaseModel):
#     image_url:str
#     class Config:
#         orm_mode = True
# class VariantSite(BaseModel):
#     variant_site_id:str
#     site_id:str
#     site_name:str
#     price:float
#     qty:int
#     status:str
#     class Config:
#         orm_mode = True
# from pydantic.utils import GetterDict
#
# class MyVariantGetter(GetterDict):
#     def get(self, key: str, default: Any) -> Any:
#
#         if key=='image':
#             tmp=self._obj.Images
#             return tmp[0].image_url if tmp else ''
#         elif key=='sites':
#             dic={}
#             for site in self._obj.Sites:
#                 dic[site.site_id]=site
#             return dic
#         else:
#             return getattr(self._obj,key)
class VariantSite(BaseModel):
    variant_id:str
    name_en:str
    image:str
    sku:str
    variant_site_id:Optional[str]
    site_id:Optional[str]
    site_name:Optional[str]
    price:Optional[float]
    status:Optional[str]
    qty:Optional[int]
    warehouse_name:Optional[str]
    warehouse_id:Optional[str]

    class Config:
        orm_mode = True
        #getter_dict = MyVariantGetter

class BackendSitewarehouseGetproductsitestockdetailProductIdGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Optional[List[VariantSite]] = None

class BackendSiteSetvariantsitestatusPostRequest(BaseModel):
    status: Literal['ONLINE','OFFLINE']
    price: Optional[float] = None
    qty: Optional[int] = None
    variant_id: str
    site_id: str
    site_name:Optional[str]
    warehouse_name:Optional[str]=None
    warehouse_id: Optional[str] = None
    product_id:Optional[str]=None

class BackendSiteSetvariantsitestatusPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None