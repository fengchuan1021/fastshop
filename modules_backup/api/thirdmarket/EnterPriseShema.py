#   timestamp: 2022-11-01T07:46:42+00:00

from __future__ import annotations
from typing import Literal


from pydantic import BaseModel


class ApiThirdmarketSettiktokkeyPostRequest(BaseModel):
    tiktok_appid: str
    tiktok_secret: str
    tiktok_shopid:str
    tiktok_token:str

