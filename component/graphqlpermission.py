from typing import List,Any
from sqlalchemy.ext.asyncio import AsyncSession

import Service
from cachetools import cached, LRUCache, TTLCache
from cachetools.keys import hashkey
@cached(cache={}, key=lambda db,modelname,role,method: f"{modelname}_{role}_{method}")#type: ignore
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

