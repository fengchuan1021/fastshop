import json

import Broadcast
import Models
from sqlalchemy.ext.asyncio import AsyncSession
import settings

from elasticsearchclient import es
from common import toJson
from component.cache import cache
import Service

@Broadcast.AfterModelDeleted('*',background=True)
async def defmodelcachefromredis(model:Models.Variant,db:AsyncSession,token:settings.UserTokenData=None,reason:str='')->None:
    if service:=getattr(Service,model.__class__.__name__.lower()+"Service",None):
        if service.usecache:
            cachekey=f"{cache.get_prefix()}:modelcache:{model.__tablename__}:{model.id}" #associated service base.py 'getpkcachename'.dont change.
            await cache.delete(cachekey)



@Broadcast.AfterModelUpdated('*',background=True)
async def resetcache(model:Models.Variant,db:AsyncSession,token:settings.UserTokenData=None)->None:
    tmpname=model.__class__.__name__
    servciename=tmpname.lower()+'Service'
    tmpservice=getattr(Service,servciename)
    if tmpservice.usecache:
        cachekey = f"{cache.get_prefix()}:modelcache:{model.__tablename__}:{model.id}"
        await cache.set(cachekey,model.json())

@Broadcast.AfterModelUpdated(Models.Category,background=True)
async def delcategorytree(model:Models.Category,db:AsyncSession,token:settings.UserTokenData=None)->None:
    #todo delete the store's all category cache
    #await cache.delete('xt:admin:categorytree')
    pass