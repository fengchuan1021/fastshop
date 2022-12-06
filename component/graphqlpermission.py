from typing import List,Any,Dict
from sqlalchemy.ext.asyncio import AsyncSession

import Service
from common import PermissionException
from component.cache import cache
@cache
async def getAuthorizedColumns(db:AsyncSession,modelname:str,role:int,method:str='read')->Any:

    permission=await Service.graphpermissionService.findOne(db,filter={"model_name":modelname,"role_id":role})
    if not permission:
        if role==1:
            return ['*'],[]
        else:
            raise PermissionException(f"roleid:{role} not set the table {modelname} permission")#ResponseException({'status':'failed','msg':f"roleid:{role} not set the table {modelname} permission"})
    columns=getattr(permission,f'{method}_columns')
    extra=getattr(permission,f'{method}_extra')
    result=columns.split(',') if columns else [],extra.split(',') if extra else []
    return result


