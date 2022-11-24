#   timestamp: 2022-10-06T06:03:09+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field



class Filter(BaseModel):
    parent_id: Optional[str] = None


class BackendProductGetcategorylistGetRequest(BaseModel):
    pagesize: Optional[int] = 20
    pagenum: Optional[int] = 1
    filter: Optional[Filter] = None



class Datum(BaseModel):
    category_name: str
    category_id: str
    parent_name: str=''
    parent_id: str
    category_image: str
    class Config:
        orm_mode = True

class BackendProductGetcategorylistGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Optional[List[Datum]] = None
    curpage: Optional[int] = 1
    total: Optional[int] = 0



class Datum1(BaseModel):
    category_id: str
    category_name: str
    category_image: str
    children: Optional[List[Datum1]] = None


class BackendProductGetcategorytreeGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Optional[List[Datum1]] = None


class BackendProductDelcategoryPostRequest(BaseModel):
    category_id: str



class BackendProductDelcategoryPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None


class BackendProductAddcategoryPostRequest(BaseModel):
    category_name: str
    parent_id: str
    category_order: Optional[int] = 0
    parent_name:str=''


class BackendProductAddcategoryPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
