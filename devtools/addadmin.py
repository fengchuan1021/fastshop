
import asyncio
import Models
from component.dbsession import getdbsession
import Service
from component.snowFlakeId import snowFlack


async def adddefaultadmin()->None:
    async with getdbsession() as db:
        try:
            root = Models.User(username='root', password=Service.userService.get_password_hash('root'))
            root.user_id=snowFlack.getId()
            await Service.userService.create(db, root)  # type: ignore
            role=await Service.roleService.create(db,{"role_name":"root",'note':"super user"})
            await db.flush()
            await Service.userroleService.create(db,{"user_id":root.user_id,'role_id':role.role_id,'role_name':'root'})
            await db.commit()
        except Exception as e:
            print(e)
            await db.rollback()

def addroot()->None:
    import asyncio
    loop=asyncio.get_event_loop()
    loop.run_until_complete(adddefaultadmin())
if __name__ == '__main__':
    asyncio.run(adddefaultadmin())