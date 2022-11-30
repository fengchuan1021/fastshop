from typing import Any

from sqlalchemy import select

import Models
import Service
import settings
import os
import importlib
from pathlib import Path

from common.CommonError import ResponseException
from component.fastQL import fastQuery
from .__init__ import Market
from sqlalchemy.ext.asyncio import AsyncSession
from common import CommonResponse,toJson

import settings
from pathlib import Path
from .market.WishService import WishService
from .market.TikTokService import TikTokService
from .market.OnBuyService import OnBuyService
class ThirdMarketService():
    def __init__(self) -> None:
        self.markets = {'wish':WishService(),
                        'tiktok':TikTokService(),
                        'onbuy':OnBuyService()
                        }


    async def getMarket(self, marketname: str) -> Market:
        if marketname in self.markets:
            return self.markets[marketname]
        else:
            raise Exception(f"{marketname} not implement found")

    async def getStoreOnlineProducts(
        self, db: AsyncSession, merchant_id: int, store_id: int
    ) -> Any:
        # store = await Service.storeService.findByPk(
        #     db, store_id, {"merchant_id": merchant_id}
        # )
        store=await fastQuery(db,'store{market{market_name}}',{"store_id":store_id,"merchant_id": merchant_id},returnsingleobj=1)
        if not store:
            raise ResponseException({'status':"failed", 'msg':"store not found"})
        marketservice=await self.getMarket(store.Market.market_name)
        return await marketservice.getProductList(db,store)


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