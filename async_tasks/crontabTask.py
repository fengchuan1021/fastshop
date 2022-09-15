
import settings
from celery_app import celery_app
import asyncio
import datetime
from common.dbsession import get_webdbsession
from async_tasks.sync2async import sync2async
from sqlalchemy import select,update
import Models
from common.dbsession import getdbsession
@celery_app.task
@sync2async
async def active_banneduser()->None:# type: ignore
    async with getdbsession() as dbsession:

        statment=update(Models.User).where(Models.User.is_banned=='banned',Models.User.ban_enddate<datetime.datetime.now()).values({Models.User.is_banned:'normal'})
        await dbsession.execute(statment)
        await dbsession.close()

@celery_app.task
def hello()->None:
    print('helloworld')
@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs)->None:  # type: ignore
    sender.add_periodic_task(10.0, hello.s(), name='active_banneduser')

