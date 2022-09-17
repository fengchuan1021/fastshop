
import Broadcast
import Models
from sqlalchemy.ext.asyncio import AsyncSession
import settings
from elasticsearchclient import es

@Broadcast.AfterModelCreated(Models.Product,background=True)
async def upload2elastic(model:Models.Product,db: AsyncSession,token:settings.UserTokenData=None,reason:str='')->None:
    print('123')
    await es.index(index=f'product-{settings.MODE}',id=model.id,document=model.as_dict())

@Broadcast.AfterModelUpdated(Models.Product,background=True)
async def upload2elasticonupdate(model:Models.Product,db: AsyncSession,token:settings.UserTokenData=None,reason:str='')->None:
    await es.index(index=f'product-{settings.MODE}',id=model.id,document=model.as_dict())

