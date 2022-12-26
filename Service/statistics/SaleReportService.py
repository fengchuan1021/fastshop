

from sqlalchemy import  text
from sqlalchemy.dialects.mysql import Insert
import Service
from Service.base import CRUDBase
import Models
from typing import Union, Optional, Any
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_

from component.cache import cache
from component.snowFlakeId import snowFlack


class SaleReportService(CRUDBase[Models.SaleReport]):

    async def onNewOrder(self,db:AsyncSession,order:Models.Order)->Any:

        data={'order_amount':order.base_grand_total,'order_count':1,'store_id':order.store_id,'date':str(order.market_createtime)[0:10],'salereport_id':snowFlack.getId(),
              'merchant_id':order.merchant_id,
              'store_name':order.store_name
              }

        if order.status=='AWAITING_SHIPMENT' or order.status=="REQUIRE_REVIEW":

            statment=Insert(Models.SaleReport).values(**data).on_duplicate_key_update(
                order_amount=text("order_amount+VALUES(order_amount)"),
                order_count=text("order_count+VALUES(order_count)"),
                total_paid=text("total_paid+VALUES(total_paid)"),
                order_paid=text("order_paid+VALUES(order_paid)"),
            )#type: ignore
        else:
            statment=Insert(Models.SaleReport).values(**data).on_duplicate_key_update(
                order_amount=text("order_amount+VALUES(order_amount)"),
                order_count=text("order_count+VALUES(order_count)"),
            )#type: ignore
        await (await db.connection()).execute(statment)
        await db.commit()
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
