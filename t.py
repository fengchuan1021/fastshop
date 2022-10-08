import asyncio
import Service
from common.dbsession import getdbsession


async def test()->None:
    db=await getdbsession()
    model=await Service.warehouseService.findByPk(db,81175036077016130)


    model.warehouse_name='12331244d'

    await db.commit()
asyncio.run(test())
print('123')
print("helloworld")