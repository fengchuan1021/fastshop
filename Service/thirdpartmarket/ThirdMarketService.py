import time
from typing import Any

from sqlalchemy import select
import Models
import Service
import os
from common.CommonError import ResponseException
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
if __name__ == "__main__":
    from component.dbsession import getdbsession
    from common import cmdlineApp
    async def test() -> None:
        async with getdbsession() as db:
            t = ThirdMarketService()
            data=await t.getStoreOnlineProducts(db,1,1)
            print(data)
            #tiktok = await t.getMarket("tiktok")
            #r = await tiktok.getProductList()
    cmdlineApp(test)()