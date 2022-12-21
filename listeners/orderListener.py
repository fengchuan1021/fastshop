import orjson
from sqlalchemy.ext.asyncio import AsyncSession

import Broadcast
import Models
import Service
import settings
from sqlalchemy.orm import class_mapper
from sqlalchemy import inspect



@Broadcast.BeforeModelCreated(Models.Order)
async def revieworder(order:Models.Order,db:AsyncSession,token:settings.UserTokenData=None)->None:
    merchant_id=order.merchant_id
    reviewrules=await Service.revieworderruleService.find(db,{'merchant_id':merchant_id},order_by='priority asc')#优先级大的最后执行 覆盖优先级小的结果
    for reviewrule in reviewrules:
        flag=await Service.revieworderService.validRule(reviewrule,order)
        if flag:
            order.status=reviewrule.status

print(666666666666666666666)

@Broadcast.AfterModelUpdated(Models.Order,background=True)
async def statistics(order:Models.Order,db:AsyncSession,token:settings.UserTokenData=None)->None:
    print('after order changed!!')
    merchant_id=order.merchant_id
    store_id=order.store_id
    inspr = inspect(order)
    history=getattr(inspr.attrs,'status').history
    print(history.deleted)
    print(history.added)

if __name__ == '__main__':
    from common import cmdlineApp
    from typing import Any

    @cmdlineApp
    async def test(db:AsyncSession)->Any:
        model=await Service.orderService.findByPk(db,61821984346146)
        model.status="paidsddd"
        await db.commit()

    test()