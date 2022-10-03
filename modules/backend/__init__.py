import settings
from common.CommonError import PermissionException
from common.globalFunctions import get_token
from .. import dependencies as praentdependencies
from fastapi import Depends
from fastapi import Request
async def checkpermission(request: Request,token: settings.UserTokenData):
    print('111:', request.scope['endpoint'].__name__)
    pass


async def permission_check(request: Request,token: settings.UserTokenData = Depends(get_token))->None:
    if token.userrole==0:
        raise PermissionException(msg="customer and guest has no permission access admin panel")
    elif token.userrole==1:
        pass
    else:
        await checkpermission(request,token)

from typing import List,Callable,Any
dependencies:List[Callable[...,Any]]=praentdependencies+[Depends(permission_check)]