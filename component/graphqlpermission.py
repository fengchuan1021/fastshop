from typing import List,Any
from sqlalchemy.ext.asyncio import AsyncSession
from component.cache import cache
import Service
@cache
async def getAuthorizedColumns(db:AsyncSession,modelname:str,role:int,method:str='read')->Any:
    permission=await Service.graphpermissionService.findOne(db,filter={"model_name":modelname,"role_id":role})
    if not permission:
        if role==1:
            return ['*'],[]
        else:
            raise PermissionError(f"roleid:{role} not set the table {modelname} permission")
    columns=getattr(permission,f'{method}_columns')
    extra=getattr(permission,f'{method}_extra')
    return columns.split(',') if columns else [],extra.split(',') if extra else []

