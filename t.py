import asyncio
import Service
from common.dbsession import getdbsession


async def test():
    db=await getdbsession()
    model=await Service.warehouseService.findByPk(db,81175036077016130)


    model.warehouse_name='12331244'

    await db.commit()
asyncio.run(test())