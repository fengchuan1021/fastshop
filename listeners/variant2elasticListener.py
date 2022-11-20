
import Broadcast
import Models
from sqlalchemy.ext.asyncio import AsyncSession
import settings
from elasticsearchclient import es
from common import cache
import Service

@Broadcast.AfterModelCreated(Models.Variant,background=True)
async def upload2elastic(model:Models.Variant,db: AsyncSession,token:settings.UserTokenData=None,reason:str='')->None:

    await es.index(index=f'product-{settings.MODE}',id=model.id,document=model.json())#type: ignore

@Broadcast.AfterModelUpdated(Models.Variant,background=True)
async def upload2elasticonupdate(model:Models.Variant,db: AsyncSession,token:settings.UserTokenData=None,reason:str='')->None:
    await es.index(index=f'product-{settings.MODE}',id=model.id,document=model.json())#type: ignore

@Broadcast.AfterModelDeleted(Models.Variant,background=True)
async def delproductines(model:Models.Variant,db:AsyncSession,token:settings.UserTokenData=None,reason:str='')->None:
    #delete from elasticsearch
    await es.delete(index=f'product-{settings.MODE}',id=model.id,ignore=404)#type: ignore



