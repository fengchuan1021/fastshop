import abc
from typing import Tuple, Dict, List, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

import Models
import Service
from Service.thirdpartmarket.Shema import Shipinfo
from common.CommonError import ResponseException
from component.fastQL import fastQuery


class Market:
    market_id:int
    market_name:str
    @abc.abstractmethod
    async def getProductList(self,db:AsyncSession,store:Models.Store)->List:
        raise NotImplementedError
    @abc.abstractmethod
    async def getProductDetail(self,db:AsyncSession,store:Models.Store,product_id:str)->Any:
        raise NotImplementedError
    @abc.abstractmethod
    async def deleteProduct(self,db:AsyncSession,enterprise_id:str,product_id:str)->List:
        raise NotImplementedError

    @abc.abstractmethod
    async def getOrderList(self,db:AsyncSession,store:Models.Store,starttime:int)->List:
        raise NotImplementedError
    async def addShipment(self,db:AsyncSession,store:Models.Store,shipinfo:Shipinfo)->Tuple[Models.Order,List[Models.OrderShipmentItem]]:
        order=await Service.orderService.findByPk(db,shipinfo.order_id,{'store_id':store.store_id},joinedload([Models.Order.ShipOrderAddress,Models.Order.OrderItem]))
        #order=await fastQuery(db,"order{OrderAddress}",{"order.order_id":shipinfo.order_id,"order_address.address_type":"SHIPPING"})
        if not order.ShipOrderAddress:
            raise ResponseException({'status': 'failed', 'msg': 'order not has a shipping address'})
        if not order:
            raise ResponseException({'status':'failed','msg':'order not found'})
        if order.status=='SHIPPED':
            raise ResponseException({'status':'failed','msg':'order has been shipped'})
        if order.status=='PENDING':
            raise ResponseException({'status':'failed','msg':'order not paid'})
        if order.status=='COMPLETE':
            raise ResponseException({'status':'failed','msg':'order has completed'})

        ordershipment=Models.OrderShipment()
        ordershipment.order_id=order.order_id
        ordershipment.total_weight=shipinfo.total_weight
        ordershipment.total_qty=shipinfo.total_qty

        ordershipment.shipping_address_id=order.ShipOrderAddress.shiporder_address_id
        ordershipment.track_number=shipinfo.track_number
        ordershipment.carrier_name=shipinfo.shipping_provider
        ordershipment.carrier_code=shipinfo.shipping_provider_id
        ordershipment.market_package_id=shipinfo.package_id
        ordershipment.market_order_id=order.market_order_id
        shipitemarr=[]
        for orderitem in order.OrderItem:
            shipitem=Models.OrderShipmentItem()
            shipitem.order_id=order.order_id
            shipitem.order_shipment_id=ordershipment.order_shipment_id
            shipitem.market_order_id=order.market_order_id
            shipitem.order_item_id=orderitem.order_item_id
            shipitem.product_id=orderitem.product_id
            shipitem.variant_id=orderitem.variant_id
            shipitem.qty=orderitem.qty_ordered
            shipitem.name=orderitem.variant_name
            shipitem.sku=orderitem.sku
            shipitem.warehouse_id=shipinfo.warehouse_id
            shipitemarr.append(shipitem)
        db.add(ordershipment)
        db.add_all(shipitemarr)
        return order,shipitemarr







    # @abc.abstractmethod
    # async def getOrderDetail(self, db: AsyncSession, store:Models.Store, order_id: str,sem:Any)->Any:
    #     raise NotImplementedError