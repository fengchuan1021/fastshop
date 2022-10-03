#   timestamp: 2022-10-03T11:35:27+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional, Literal

from pydantic import BaseModel, constr, validator, Field


class FrontendUserRegisterPostInShema(BaseModel):
    username: Optional[constr(min_length=4, max_length=32)] = None
    password: str
    repassword: str=Field(...,exclude=True)
    phone: Optional[str] = None
    email: constr(min_length=4, max_length=32)
    @validator('repassword')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v




class User(BaseModel):
    username: str
    phone: str
    email: str
    class Config:
        orm_mode = True


class FrontendUserRegisterPostOutShema(BaseModel):
    status: Literal['failed','success']
    user: User


class FrontendUserLoginPostInShema(BaseModel):
    username: str
    password: str





class FrontendUserLoginPostOutShema(BaseModel):
    status: Literal['failed','success']
    token: Optional[str] = None
    refreshtoken: Optional[str] = None
    msg: Optional[str] = None
