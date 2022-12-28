from typing import Optional

from pydantic import BaseModel


class Shipinfo(BaseModel):
    package_id:Optional[str]='' #在第三方市场的package_id 由第三方市场提供
    order_id:Optional[str]='' #在xt 系统上的order_id
    origin_country:Optional[str]='' #wish 要求国家代码
    track_number:str
    warehouse_id:int
    shipping_provider_id:str#tiktok要求快递代码
    shipping_provider:str  #wish要求快递名字
    ship_note:Optional[str]=''
    total_weight:Optional[float]=0.0
    total_qty:Optional[int]=0
