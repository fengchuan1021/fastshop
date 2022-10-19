#   timestamp: 2022-10-19T08:41:48+00:00

from __future__ import annotations
from typing import Literal


from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field




class FrontendProductbyvariantidVariantidGetResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Any
