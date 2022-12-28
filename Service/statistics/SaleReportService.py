

from sqlalchemy import  text
from sqlalchemy.dialects.mysql import insert
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
              'store_name':order.store_name,'total_paid':0,'order_paid':0,
              }

        if order.status=='AWAITING_SHIPMENT' or order.status=="REQUIRE_REVIEW":

            statment=insert(Models.SaleReport).values(**data).on_duplicate_key_update(
                order_amount=text("order_amount+VALUES(order_amount)"),
                order_count=text("order_count+VALUES(order_count)"),
                total_paid=text("total_paid+VALUES(total_paid)"),
                order_paid=text("order_paid+1"),
            )#type: ignore
        else:
            statment=insert(Models.SaleReport).values(**data).on_duplicate_key_update(
                order_amount=text("order_amount+VALUES(order_amount)"),
                order_count=text("order_count+VALUES(order_count)"),
            )#type: ignore
        await (await db.connection()).execute(statment)
        await db.commit()
    async def onUnpaidtoPaid(self,db:AsyncSession,order:Models.Order)->Any:

        data={'order_amount':order.base_grand_total,'order_count':1,'store_id':order.store_id,'date':str(order.market_createtime)[0:10],'salereport_id':snowFlack.getId(),
              'merchant_id':order.merchant_id,
              'store_name':order.store_name,'total_paid':1,'order_paid':1,
              }



        statment=insert(Models.SaleReport).values(**data).on_duplicate_key_update(
            total_paid=text("total_paid+VALUES(total_paid)"),
            order_paid=text("order_paid+1"),
        )
        await (await db.connection()).execute(statment)
        await db.commit()

