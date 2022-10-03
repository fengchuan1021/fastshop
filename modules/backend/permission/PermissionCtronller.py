#   timestamp: 2022-10-03T14:41:27+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field



class BackendPermissionRolePostResponse(BaseModel):
    pass



class Role(BaseModel):
    id: int
    role_name: str


class BackendPermissionRoleGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    roles: Optional[List[Role]] = None
