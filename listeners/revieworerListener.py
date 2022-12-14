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
        scripts_params=orjson.loads(reviewrule.content)#type: ignore
        for script in scripts_params:
            func=getattr(Service.revieworderService,script['func'])
            flag=await func(script['data'])
            if not flag:
                break#有一个条件为假 跳过执行
        else:
            #全部条件为真 执行设置订单状态
            order.status=reviewrule.status

