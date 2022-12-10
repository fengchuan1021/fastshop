import time

if __name__=='__main__':
    import sys
    from pathlib import Path
    sys.path.insert(0,Path(__file__).parent.parent.__str__())

from sqlalchemy.ext.asyncio import AsyncSession

import Service
from celery_app import celery_app
import datetime

from common.globalFunctions import cmdlineApp
from sqlalchemy import update
import Models
from component.dbsession import getdbsession

# @celery_app.task
# @cmdlineApp
# async def active_banneduser()->None:# type: ignore
#     async with getdbsession() as dbsession:
#         pass
#         #statment=update(Models.User).where(Models.User.is_banned=='banned',Models.User.ban_enddate<datetime.datetime.now()).values({Models.User.is_banned:'normal'})
#         #await dbsession.execute(statment)
#         #await dbsession.close()

@celery_app.task
@cmdlineApp
async def syncOrder(db:AsyncSession)->None:

    stores=await Service.storeService.find(db,{'status':1})
    for store in stores:
        try:
            await Service.thirdmarketService.syncOrder(db,store.merchant_id,store.store_id,1)
            await db.commit()
        except Exception as e:
            await db.rollback() #可能有token过期异常 或其他异常必须rollback 才能继续


@celery_app.task
@cmdlineApp
async def refreshtoken(db:AsyncSession)->None:

    stores=await Service.storeService.find(db)
    tmnow=time.time()
    for store in stores:
        if (store.token_expiration-tmnow)<3600*24:#24小时内要到期得toKen 刷新下
            try:
                #await Service.thirdmarketService.refreshtoken(db,store.merchant_id,store.store_id)
                #await db.commit()
                pass #先不启用
            except Exception as e:
                await db.rollback() #可能有token过期异常 或其他异常必须rollback 才能继续

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs)->None:  # type: ignore
    sender.add_periodic_task(5*60, syncOrder.s(), name='syncOrder')#5分钟同步一次订单
    sender.add_periodic_task(12 * 3600, refreshtoken.s(), name='refreshtoken')  # 12小时检查一次快要到期的token 更新token
if __name__=='__main__':
    syncOrder()