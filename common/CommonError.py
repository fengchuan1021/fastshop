from typing import Dict

from pydantic import BaseModel
from typing import TypeVar, Generic, Optional, List, Any, Literal
from .CommonResponse import CommonResponse
class Common500Response(BaseModel):
    status: Literal['validateerror', 'neterror','dberror','cache server error','tokenerror','unknownerr','notlogin','permissiondenied','userbanned','modelnotexists']
    msg: Optional[str] = None
    data:Optional[Any]

class TokenException(Exception):
    def __init__(self,msg:str):
        self.msg=msg
    def __repr__(self) -> str:
        return self.msg
    def __str__(self)->str:
        return self.msg

class PermissionException(Exception):
    def __init__(self,msg:str):
        self.msg=msg
    def __repr__(self) -> str:
        return self.msg
    def __str__(self)->str:
        return self.msg
class ResponseException(Exception):
    def __init__(self,response:Dict):
        if 'msg' not in response:
            response['msg']=''
        if 'status' not in response:
            response['status']='success'
        self.response=response
    def __repr__(self) -> str:
        return self.response['msg']
    def __str__(self)->str:
        return self.response['msg']