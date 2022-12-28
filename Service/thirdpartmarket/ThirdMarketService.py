import time
from typing import Any, Tuple, List

from sqlalchemy import select
from sqlalchemy.orm import joinedload

import Models
import Service
import os

from Service.thirdpartmarket.Shema import Shipinfo
from common.CommonError import ResponseException, TokenException
from component.fastQL import fastQuery
from .__init__ import Market
from sqlalchemy.ext.asyncio import AsyncSession

from pathlib import Path
class ThirdMarketService():

    def __init__(self) -> None:
        self.markets = {}
        files = os.listdir(Path(__file__).parent.joinpath('market'))
        for f in files:
            if f.endswith('Service.py'):
                marketname=f[0:-10].lower()
                self.markets[marketname]=getattr(Service,marketname+'Service')
    async def init(self,db:AsyncSession)->None:
        marketmodels=await Service.marketService.find(db)
        for model in marketmodels:
            if model.market_name in self.markets:
                self.markets[model.market_id]=self.markets[model.market_name]#type: ignore
                setattr(self.markets[model.market_name],'market_name',model.market_name)
                setattr(self.markets[model.market_name], 'market_id', model.market_id)

    async def getMarket(self, marketname_or_id: str|int) -> Market:
        if isinstance(marketname_or_id,str):
            if (lowername:=marketname_or_id.lower()) in self.markets:
                return self.markets[lowername]
            else:
                raise Exception(f"{marketname_or_id} not implement found")
        else:
            return self.markets[marketname_or_id]#type: ignore

    async def getStoreandMarketService(self,db:AsyncSession,merchant_id:int,store_id:int)->Any:
        #store=await fastQuery(db,'store{market{market_name}}',{"store_id":store_id,"merchant_id": merchant_id},returnsingleobj=1)
        store=await Service.storeService.findOne(db,{"store_id":store_id,"merchant_id": merchant_id})
        if not store:
            raise ResponseException({'status':"failed", 'msg':"store not found"})
        return store,await self.getMarket(store.market_id)

    async def getStoreOnlineProducts(
        self, db: AsyncSession, merchant_id: int, store_id: int
    ) -> Any:
        # store = await Service.storeService.findByPk(
        #     db, store_id, {"merchant_id": merchant_id}
        # )
        store,marketservice=await self.getStoreandMarketService(db,merchant_id,store_id)
        tmp=marketservice.getProductList(db,store)
        return await tmp. __anext__()

    async def getStoreOnlineOrders(self,db:AsyncSession,merchant_id:int,store_id:int)->Any:

        store,marketservice=await self.getStoreandMarketService(db,merchant_id,store_id)
        endtime = int(time.time())
        starttime=endtime-3600*24
        tmp=marketservice.getOrderList(db,store,starttime)
        return await tmp.__anext__()
    async def getStoreOnlineProductDetail(self,db:AsyncSession,merchant_id:int,store_id:int,product_id:str)->Any:
        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        return await marketservice.getProductDetail(db,store,product_id)
    async def getStoreOnlineOrderDetail(self,db:AsyncSession,merchant_id:int,store_id:int,order_id:str)->Any:
        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        return await marketservice.getOrderDetail(db,store,order_id)
    async def syncOrder(self,db:AsyncSession,merchant_id:int,store_id:int,ndays:int=1)->Any:
        store,marketservice=await self.getStoreandMarketService(db,merchant_id,store_id)
        endtime = int(time.time())
        starttime=endtime-ndays*3600*24
        data=await marketservice.syncOrder(db,merchant_id,store,starttime)
    async def syncProduct(self,db:AsyncSession,merchant_id:int,store_id:int)->Any:
        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        await marketservice.syncProduct(db,store,merchant_id)
    async def getSelfAuthrizeUrl(self,db:AsyncSession,merchant_id:int,store_id:int)->str:
        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        return await marketservice.getSelfAuthrizeUrl(db,store)

    async def getStoreOnlinePackageDetail(self,db:AsyncSession,merchant_id:int,store_id:int,package_id:str)->Any:
        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        return await marketservice.getPackageDetail(db,store,package_id)
    async def getTickets(self,db:AsyncSession,merchant_id:int,store_id:int)->Any:
        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        return await marketservice.getTickets(db,store)
    async def getTicketDetail(self,db:AsyncSession,merchant_id:int,store_id:int,ticket_id:str)->Any:
        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        return await marketservice.getTicketDetail(db,store,ticket_id)
    async def closeTicket(self,db:AsyncSession,merchant_id:int,store_id:int,ticket_id:str)->Any:
        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        return await marketservice.closeTicket(db,store,ticket_id)
    async def replyTicket(self,db:AsyncSession,merchant_id:int,store_id:int,ticket_id:str,content:str)->Any:
        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        return await marketservice.replyTicket(db,store,ticket_id,content)
    async def refreshtoken(self,db:AsyncSession,merchant_id:int,store_id:int)->Any:
        store,marketservice=await self.getStoreandMarketService(db,merchant_id,store_id)
        try:
            ret=await marketservice.refreshtoken(db,store)
            return ret
        except TokenException as e:
            store.status = 0
            store.status_msg =e.msg
            return ResponseException({'status':'failed','msg':e.msg})
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
    async def shiPackage(self,db:AsyncSession,merchant_id:int,store_id:int,shipInfo:Shipinfo)->Any:

        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        order, ordershipmentitems = await self.addShipment(db, store,shipInfo)
        return await marketservice.shiPackage(db,store,shipInfo,order,ordershipmentitems)
    async def updateStock(self,db:AsyncSession,merchant_id:int,store_id:int,sku:str,num:int)->Any:
        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        return await marketservice.updateStock(db,store,sku,num)

    async def updatePrice(self,db:AsyncSession,merchant_id:int,store_id:int,sku:str,price:float)->Any:
        store, marketservice = await self.getStoreandMarketService(db, merchant_id, store_id)
        return await marketservice.updatePrice(db,store,sku,price)
if __name__ == "__main__":
    from component.dbsession import getdbsession
    from common import cmdlineApp


    @cmdlineApp
    async def test() -> None:
        async with getdbsession() as db:
            t = ThirdMarketService()
            data=await t.getStoreOnlineProducts(db,1,1)
            print(data)
            #tiktok = await t.getMarket("tiktok")
            #r = await tiktok.getProductList()
    test()