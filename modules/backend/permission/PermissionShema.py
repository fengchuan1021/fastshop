#   timestamp: 2022-10-04T14:12:31+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, validator


class BackendPermissionRouteGetResponse(BaseModel):
    label:str
    key:Optional[str]
    children:Optional[List[BackendPermissionRouteGetResponse]]



class Datum(BaseModel):
    role_id: int
    role_name: str
    api_name: str
    class Config:
        orm_mode = True

class BackendPermissionPermissionlistGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Optional[List[Datum]] = None
    total: int
    curpage: int

class Filter(BaseModel):
    role_id: Optional[int] = None
    role_name: Optional[str] = None
    api_name: Optional[str] = None


class BackendPermissionPermissionlistGetRequest(BaseModel):
    filter: Optional[Filter] = None
    pagenum: Optional[int] = 1
    pagesize: Optional[int] = 30


class BackendPermissionSetrolepermissionPostRequest(BaseModel):
    role_id: int
    apis: List[str]



class BackendPermissionSetrolepermissionPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None



class BackendPermissionRoleIdDeleteResponse(BaseModel):
    status: Literal['failed','success']
    msg: Optional[str] = None


class BackendPermissionRolePostRequest(BaseModel):
    role_name: str

    @validator('role_name')
    def checkrole_name(cls,v):
        if not ('a'<= v[0].lower() >='Z'):
            raise ValueError('role name must start with string')
        return v


class Role(BaseModel):
    id: int
    role_name: str


class BackendPermissionRolePostResponse(BaseModel):
    status: Literal['failed','success']
    msg: Optional[str] = None
    role: Optional[Role] = None



class Role1(BaseModel):
    id: int
    role_name: str


class BackendPermissionRoleGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    roles: Optional[List[Role1]] = None






class BackendPermissionGetroledisplayedmenuGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    menus: Optional[List[str]] = None


class BackendPermissionSetdisplayedmenuPostRequest(BaseModel):
    role_id: int
    menus: List[str]



class BackendPermissionSetdisplayedmenuPostResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None

