s='''#   timestamp: 2022-10-03T14:33:15+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Gender(Enum):
    man = 'man'
    woman = 'woman'


class BackendPermissionRouteGetResponse(BaseModel):
    pass


class BackendPermissionSetrolepermissionPostResponse(BaseModel):
    pass


class BackendPermissionRolePostResponse(BaseModel):
    pass


class Status(Enum):
    success = 'success'
    failed = 'failed'


class Role(BaseModel):
    id: int
    role_name: str


class BackendPermissionRoleGetResponse(BaseModel):
    status: Status
    msg: Optional[str] = None
    roles: Optional[List[Role]] = None


'''
import re

enumarr = re.findall(r'(^class (\w+)\(Enum\)(.*?)^\n)',s, re.M | re.DOTALL)

if enumarr:
    enumdict = {}
    for item in enumarr:
        total, key, txt = item
        print('total',total)
        print(11111)
        print('key:',key)
        print(1111111)
        print('txt:',txt)
        print(1111111)
        values = re.findall(r'    (.*?) ', txt)
        if values:
            enumdict[key] = [total, "Literal[" + ','.join([v.__repr__() for v in values]) + "]"]
    print(enumdict)
    #for classname in enumdict:
    #    newbody = newbody.replace(enumdict[classname][0], '').replace(classname, enumdict[classname][1])