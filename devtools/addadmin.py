
import asyncio
import Models
from component.dbsession import getdbsession
import Service
from component.snowFlakeId import snowFlack


async def adddefaultadmin()->None:
    async with getdbsession() as db:
        try:
            root = Models.User(username='root', password=Service.userService.get_password_hash('root'),user_id=snowFlack.getId())
            merchant=Models.User(username='merchant',password=Service.userService.get_password_hash('merchant'),user_id=snowFlack.getId())
            #await Service.userService.create(db, root)  # type: ignore
            db.add(root)
            db.add(merchant)
            #await Service.userService.create(db, merchant)  # type: ignore
            role=await Service.roleService.create(db,{"role_name":"root",'note':"super user"})
            merchantrole = await Service.roleService.create(db, {"role_name": "merchant", 'note': "merchant user"})
            await db.flush()
            await Service.userroleService.create(db,{"user_id":root.user_id,'role_id':role.role_id,'role_name':'root'})
            await Service.userroleService.create(db, {"user_id": merchant.user_id, 'role_id': merchantrole.role_id,
                                                      'role_name': '商家'})
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