#   timestamp: 2022-10-14T14:37:29+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field



class BackendProductUpdatebrandPostRequest(BaseModel):
    brand_en: str
    brand_id: str



class BackendProductUpdatebrandPostResponse(BaseModel):
    status: Literal['success','failed']
    data: Optional[Dict[str, Any]] = None
    msg: Optional[str] = None


class BackendProductBrandlistPostRequest(BaseModel):
    pagesize: Optional[int] = 20
    pagenum: Optional[int] = 1
    filter: Optional[Dict[str, Any]] = None



class Datum(BaseModel):
    brand_id: str
    brand_en: str
    class Config:
        orm_mode = True

class BackendProductBrandlistPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    total: Optional[int] = None
    curpage: Optional[int] = None
    data: Optional[List[Datum]] = None



class BackendProductDelbrandBrandIdPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None


class BackendProductAddbrandPostRequest(BaseModel):
    brand_en: str



class BackendProductAddbrandPostResponse(BaseModel):
    status: Literal['success','failed']
    data: Optional[Dict[str, Any]] = None
    msg: Optional[str] = None
