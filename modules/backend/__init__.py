from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

import Models
import settings
from common.CommonError import PermissionException
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from .. import dependencies as praentdependencies
from fastapi import Depends
from fastapi import Request
from component.cache import cache
async def checkpermission(db: AsyncSession,request: Request,token: settings.UserTokenData)->None:
    api_name=f"{request.scope['endpoint'].__module__.replace('modules.','')}.{request.scope['endpoint'].__name__}"
    flag=await cache.hget(f"xtadmin:rolepermission{token.userrole}",api_name)
    if flag:
        if int(flag):
            pass
        else:
            raise PermissionException(msg="you dont have permission access this api")
    else:
        roleid=token.userrole
        j=0
        while roleid:
            j+=1
            i = 1 << j
            if roleid & i :
                sql=select(Models.Permission).filter(Models.Permission.role_id==i).filter(Models.Permission.api_name==api_name)
                haspermission=(await db.execute(sql)).scalar_one_or_none()
                if haspermission:
                    await cache.hset(f"xtadmin:rolepermission{token.userrole}",api_name,1,3600*24)
                    return
                roleid=roleid -i

        await cache.hset(f"xtadmin:rolepermission{token.userrole}",api_name,0,3600*24)
        raise PermissionException(msg="you dont have permission access this api")





async def permission_check(request: Request,db: AsyncSession = Depends(get_webdbsession),token: settings.UserTokenData = Depends(get_token))->None:
    if token.userrole==0:
        raise PermissionException(msg="customer and guest has no permission access admin panel")
    elif token.userrole==1:
        pass
    else:
        await checkpermission(db,request,token)

from typing import List,Callable,Any
dependencies:List[Callable[...,Any]]=praentdependencies+[Depends(permission_check)]