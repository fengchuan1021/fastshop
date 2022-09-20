import json

import Broadcast
import Models
from sqlalchemy.ext.asyncio import AsyncSession
import settings
from common.globalFunctions import toJson
from elasticsearchclient import es
from component.cache import cache
import Service

@Broadcast.AfterModelDeleted('*',background=True)
async def defmodelcachefromredis(model:Models.ProductStatic,db:AsyncSession,token:settings.UserTokenData=None,reason:str='')->None:

    cachekey=f"{cache.get_prefix()}:modelcache:{model.__tablename__}:{model.id}" #associated service base.py 'getpkcachename'.dont change.
    await cache.delete(cachekey)



@Broadcast.AfterModelUpdated('*',background=True)
async def resetcache(model:Models.ProductStatic,db:AsyncSession,token:settings.UserTokenData=None)->None:
    print('modelname:',model.__class__.__name__)
    service=Service.getInstanceForModel(model)
    if service.usecache:
        cachekey = f"{cache.get_prefix()}:modelcache:{model.__tablename__}:{model.id}"
        await cache.set(cachekey,model.json())