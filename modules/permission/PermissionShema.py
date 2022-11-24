#   timestamp: 2022-11-23T13:00:33+00:00

from __future__ import annotations
from typing import Literal


from pydantic import BaseModel
from typing import Optional

class PermissionSetrolemodelpermissionPostRequest(BaseModel):
    model_name: str
    role_id: int
    role_name: Optional[str] = None
    writable_columns: str
    readable_columns: str
    delete_permission: bool
    extra_filter: str
