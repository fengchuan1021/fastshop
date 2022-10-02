import settings
from common.CommonError import PermissionException
from common.globalFunctions import get_token
from .. import dependencies as praentdependencies
from fastapi import Depends
from fastapi import Request
async def permission_check(request: Request,token: settings.UserTokenData = Depends(get_token))->None:
    if token.userrole==0:
        print("why??")
        raise PermissionException(msg="customer and guest has no permission access admin panel")
    print(request.scope['endpoint'].__name__)
from typing import List,Callable,Any
dependencies:List[Callable[...,Any]]=praentdependencies+[Depends(permission_check)]