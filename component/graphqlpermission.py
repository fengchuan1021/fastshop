from typing import List,Any,Dict
from sqlalchemy.ext.asyncio import AsyncSession

import Service
cache_dic:Dict[str,Any]={}
async def getAuthorizedColumns(db:AsyncSession,modelname:str,role:int,method:str='read')->Any:
    key=f'{modelname}_{role}_{method}'
    if key in cache_dic:
        return cache_dic[key]
    permission=await Service.graphpermissionService.findOne(db,filter={"model_name":modelname,"role_id":role})
    if not permission:
        if role==1:
            return ['*'],[]
        else:
            raise PermissionError(f"roleid:{role} not set the table {modelname} permission")
    columns=getattr(permission,f'{method}_columns')
    extra=getattr(permission,f'{method}_extra')
    result=columns.split(',') if columns else [],extra.split(',') if extra else []
    cache_dic[key]=result
    return result


