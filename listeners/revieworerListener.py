import orjson
from sqlalchemy.ext.asyncio import AsyncSession

import Broadcast
import Models
import Service
import settings


@Broadcast.BeforeModelCreated(Models.Order)
async def revieworder(order:Models.Order,db:AsyncSession,token:settings.UserTokenData=None)->None:
    merchant_id=order.merchant_id
    reviewrules=await Service.revieworderruleService.find(db,{'merchant_id':merchant_id},order_by='priority asc')#优先级大的最后执行 覆盖优先级小的结果
    for reviewrule in reviewrules:
        flag=await Service.revieworderService.validRule(reviewrule,order)
        if flag:
            order.status=reviewrule.status

