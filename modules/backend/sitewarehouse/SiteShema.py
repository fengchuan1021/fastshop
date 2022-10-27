#   timestamp: 2022-10-06T14:58:24+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
import settings


class BackendSiteAddsitePostRequest(BaseModel):
    site_name: str
    warehouse_id: str
    warehouse_name: str
    domainname:str
    lang:Literal[tuple([i.value for i in settings.SupportLang])]#type: ignore


class BackendSiteAddsitePostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None


class BackendSiteSitelistPostRequest(BaseModel):
    pagesize: Optional[int] = 20
    pagenum: Optional[int] = 1
    filter: Optional[Dict[str, Any]] = None



class Datum(BaseModel):
    site_name: str
    site_id: str
    warehouse_id: str
    warehouse_name: str
    domainname:str
    lang:str
    class Config:
        orm_mode = True

class BackendSiteSitelistPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Optional[List[Datum]] = None


class BackendSiteDelsiteDeleteRequest(BaseModel):
    site_id: str



class BackendSiteDelsiteDeleteResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None

class BackendSiteEditsitePostRequest(BaseModel):
    site_name: str
    warehouse_id: str
    warehouse_name: str
    site_id: str





