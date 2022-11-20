from typing import Literal, Optional, Any, Dict

from pydantic import BaseModel

class CommonQueryShema(BaseModel):
    pagesize: Optional[int] = 20
    pagenum: Optional[int] = 1
    filter: Optional[Dict] = None


class CommonResponse(BaseModel):
    status: Literal['success','failed']
    msg: Optional[str] = None
    data: Optional[Any]
    total:Optional[int]