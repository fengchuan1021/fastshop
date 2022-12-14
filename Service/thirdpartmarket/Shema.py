from typing import Optional

from pydantic import BaseModel


class Shipinfo(BaseModel):
    package_id:Optional[str]='' #在第三方市场的package_id 由第三方市场提供
    order_id:Optional[str]='' #tiktok要求package_id,wish 要求order_id
    origin_country:Optional[str]='' #wish 要求国家代码
    track_number:str
    shipping_provider_id:str#tiktok要求快递代码
    shipping_provider:str  #wish要求快递名字
    ship_note:Optional[str]=''