
import Broadcast
import Models
from sqlalchemy.ext.asyncio import AsyncSession
import settings
from elasticsearchclient import es
from component.cache import cache
import Service

@Broadcast.AfterModelCreated(Models.VariantStatic,background=True)
async def upload2elastic(model:Models.VariantStatic,db: AsyncSession,token:settings.UserTokenData=None,reason:str='')->None:

    await es.index(index=f'product-{settings.MODE}',id=model.id,document=model.json())

@Broadcast.AfterModelUpdated(Models.VariantStatic,background=True)
async def upload2elasticonupdate(model:Models.VariantStatic,db: AsyncSession,token:settings.UserTokenData=None,reason:str='')->None:
    await es.index(index=f'product-{settings.MODE}',id=model.id,document=model.json())

@Broadcast.AfterModelDeleted(Models.VariantStatic,background=True)
async def delproductines(model:Models.VariantStatic,db:AsyncSession,token:settings.UserTokenData=None,reason:str='')->None:
    #delete from elasticsearch
    await es.delete(index=f'product-{settings.MODE}',id=model.id,ignore=404)#type: ignore



