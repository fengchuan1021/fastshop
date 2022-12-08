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
async def syncOrder()->None:
    async with getdbsession() as db:
        stores=await Service.storeService.find(db,{'status':1})
        for store in stores:
            await Service.thirdmarketService.syncOrder(db,store.merchant_id,store.store_id,1)


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs)->None:  # type: ignore
    sender.add_periodic_task(5*60, syncOrder.s(), name='active_banneduser')#5分钟同步一次订单

