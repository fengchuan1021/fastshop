#   timestamp: 2022-10-03T15:11:26+00:00

from __future__ import annotations
from typing import Literal, Dict, Any

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, validator


class BackendPermissionRouteGetResponse(BaseModel):
    label:str
    children:Optional[List[BackendPermissionRouteGetResponse| str]]


class BackendPermissionSetrolepermissionPostRequest(BaseModel):
    role_id: int
    apis: List[str]


class BackendPermissionSetrolepermissionPostResponse(BaseModel):
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
    id:int
    role_name:str
class BackendPermissionRolePostResponse(BaseModel):
    status: Literal['failed','success']
    msg: Optional[str] = None
    role:Optional[Role]


class Role(BaseModel):
    id: int
    role_name: str


class BackendPermissionRoleGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    roles: Optional[List[Role]] = None
