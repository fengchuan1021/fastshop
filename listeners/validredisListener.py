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
async def defmodelcachefromredis(model:Models.Variant,db:AsyncSession,token:settings.UserTokenData=None,reason:str='')->None:

    cachekey=f"{cache.get_prefix()}:modelcache:{model.__tablename__}:{model.id}" #associated service base.py 'getpkcachename'.dont change.
    await cache.delete(cachekey)



@Broadcast.AfterModelUpdated('*',background=True)
async def resetcache(model:Models.Variant,db:AsyncSession,token:settings.UserTokenData=None)->None:
    tmpname=model.__class__.__name__
    servciename=tmpname[0].lower()+tmpname[1:]+'Service'
    tmpservice=getattr(Service,servciename)
    if tmpservice.usecache:
        cachekey = f"{cache.get_prefix()}:modelcache:{model.__tablename__}:{model.id}"
        await cache.set(cachekey,model.json())