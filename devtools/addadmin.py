
import asyncio
import Models
from common.dbsession import getdbsession
import Service

async def adddefaultadmin()->None:
    async with getdbsession() as db:
        try:
            root = Models.User(username='root', password=Service.userService.get_password_hash('root'), userrole=1)
            await Service.userService.create(db,root)#type: ignore

            await db.commit()
        except Exception as e:
            await db.rollback()

def addroot()->None:
    import asyncio
    loop=asyncio.get_event_loop()
    loop.run_until_complete(adddefaultadmin())
if __name__ == '__main__':
    asyncio.run(adddefaultadmin())