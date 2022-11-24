#   timestamp: 2022-10-09T07:45:48+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field







class BackendProductDelpreattrspecificPreattrspecificIdPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None



class Filter(BaseModel):
    name_en: Optional[str] = None
    name_en__contains: Optional[str] = None
    type: Optional[Literal['specification','attribute']] = None


class BackendProductPreattrspecificPostRequest(BaseModel):
    pagesize: Optional[int] = 20
    pagenum: Optional[int] = 1
    filter: Optional[Filter] = None



class Datum(BaseModel):
    preattrspecific_id: str
    name_en: str
    name_cn: str
    value_en: str
    value_cn: str
    type: str
    singlefield: int
    class Config:
        orm_mode = True

class BackendProductPreattrspecificPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    total: Optional[int] = None
    curpage: Optional[int] = None
    data: Optional[List[Datum]] = None



class BackendProductUpdatepreattrspecificPostRequest(BaseModel):
    name_en: str
    value_en: str
    type: Literal['specification','attribute']
    singlefield: int
    preattrspecific_id: str



class BackendProductUpdatepreattrspecificPostResponse(BaseModel):
    status: Literal['success','failed']
    data: Optional[Dict[str, Any]] = None
    msg: Optional[str] = None



class BackendProductAddpreattrspecificPostRequest(BaseModel):
    name_en: str
    value_en: Optional[str]=''
    type: Optional[Literal['specification','attribute']] = 'specification'
    singlefield: Optional[int] = 0



class BackendProductAddpreattrspecificPostResponse(BaseModel):
    status: Literal['success','failed']
    data: Optional[Dict[str, Any]] = None
    msg: Optional[str] = None
