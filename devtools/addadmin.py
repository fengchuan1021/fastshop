
import asyncio
import Models
from component.dbsession import getdbsession
import Service
from component.snowFlakeId import snowFlack


async def adddefaultadmin()->None:
    async with getdbsession() as db:
        try:
            root = Models.User(username='root', password=Service.userService.get_password_hash('root'),user_id=snowFlack.getId(),userrole=1)
            merchant=Models.User(username='merchant',password=Service.userService.get_password_hash('merchant'),user_id=snowFlack.getId(),userrole=2)
            #await Service.userService.create(db, root)  # type: ignore
            db.add(root)
            db.add(merchant)
            db.commit()
            merchantModel=Models.Merchant(user_id=merchant.user_id,merchant_name='unineed')
            db.add(merchantModel)
            #await Service.userService.create(db, merchant)  # type: ignore
            #role=await Service.roleService.create(db,{"role_name":"root",'note':"super user"})
            #merchantrole = await Service.roleService.create(db, {"role_name": "merchant", 'note': "merchant user"})
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