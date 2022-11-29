#   timestamp: 2022-11-23T13:00:33+00:00

from __future__ import annotations
from typing import Literal


from pydantic import BaseModel
from typing import Optional,List

class PermissionSetrolemodelpermissionPostRequest(BaseModel):
    model_name: str
    role_id: int
    role_name: Optional[str] = None

    read_columns: List[str]
    writa_columns: List[str]
    update_columns: List[str]
    delete_columns: Optional[Literal['Y',"N"]]='N'

    read_extra: List[str]
    writa_extra: List[str]
    update_extra: List[str]
    delete_extra: List[str]
