

from sqlalchemy import select

import Service
from Service.base import CRUDBase
import Models
from typing import Union, Optional, Any
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_

from component.cache import cache


class SaleReportService(CRUDBase[Models.SaleReport]):

    async def onNewOrder(self,db:AsyncSession,order:Models.Order)->Any:
        newflag=False
        order_time=str(order.market_createtime)[0:10]
        model=await self.findOne(db,{'date':order_time,'store_id':order.store_id})
        if not model:
            model=Models.SaleReport(date=order_time,store_id=order.store_id,merchant_id=order.merchant_id)
            model.store_name = (await Service.storeService.findByPk(db, order.store_id)).store_name
            newflag=True

        model.order_amount+=order.base_grand_total
        model.order_count+=1
        if order.status=='AWAITING_SHIPMENT' or order.status=="REQUIRE_REVIEW":
            model.total_paid+=order.base_grand_total
            model.order_paid+=1

        if newflag:
            db.add(model)

    async def onUnpaidtoPaid(self,db:AsyncSession,order:Models.Order)->Any:
        newflag=False
        order_time=str(order.market_createtime)[0:10]
        model=await self.findOne(db,{'date':order_time,'store_id':order.store_id})
        if not model:
            model=Models.SaleReport(date=order_time,store_id=order.store_id,merchant_id=order.merchant_id)
            model.store_name = (await Service.storeService.findByPk(db, order.store_id)).store_name
            newflag=True


        model.total_paid+=order.grand_total
        model.order_paid+=1
        if newflag:
            db.add(model)
