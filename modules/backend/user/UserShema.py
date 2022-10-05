#   timestamp: 2022-10-05T15:57:31+00:00

from __future__ import annotations
from typing import Literal, List

from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field



class BackendUserUserGetRequest(BaseModel):
    pagenum: Optional[int] = 1
    pagesize: Optional[int] = 20
    total: Optional[int] = 0
    filter: Optional[Dict[str, Any]] = None



class Data(BaseModel):
    id: int=None
    username: str
    email: str
    balance: float=0
    phone: str
    class Config:
        orm_mode = True

class BackendUserUserGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    total: Optional[int] = None
    data: Optional[List[Data]] = None

class BackendUserCreateuserPostRequest(BaseModel):
    username: str
    password: str
    phone: Optional[str] = None
    email: Optional[str] = None
    userrole: Optional[int]=0



class BackendUserCreateuserPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None