from typing import Literal, Optional, Any

from pydantic import BaseModel


class CommonResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Optional[Any]