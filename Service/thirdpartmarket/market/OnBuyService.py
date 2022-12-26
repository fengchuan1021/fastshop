import datetime
import time
from typing import Dict, List, TYPE_CHECKING, cast, Any, Literal
from sqlalchemy.ext.asyncio import AsyncSession
from dateutil.parser import parse
import Models
import Service
import settings
from . import onbuyutil
import aiohttp
from common import TokenException
from component.cache import cache
from urllib.parse import urlencode
#from Service.thirdpartmarket import Market
class OnBuyService():#Market

    async def request(self,store:Models.Store,method:Literal["GET","POST","PUT"],url:str,params:Dict=None,body:Dict=None,headers:Dict=None)->Any:
        if not store.token_expiration or store.token_expiration-int(time.time())<120:
            await self.getToken(store)
        header={'Authorization':store.token}
        if headers:
            header.update(headers)
        async with aiohttp.request(method, f'{settings.ONBUY_ENDPOINT}{url}', params=params,json=body, headers=header) as resp:#type: ignore
            ret = await resp.json()
            return ret
    async def get(self,store:Models.Store,url:str,params:Dict=None)->Any:
        ret=await self.request(store,'GET',url,params)
        return ret

    async def getToken(self,store:Models.Store)->str:
        form = aiohttp.FormData()
        form.add_field('secret_key',store.appkey )
        form.add_field('consumer_key',store.appsecret)
        async with aiohttp.request("POST",f'{settings.ONBUY_ENDPOINT}/v2/auth/request-token',data=form) as resp:
            ret=await resp.json()
            token=ret["access_token"]
            store.token=token
            store.token_expiration=int(ret['expires_at'])
            print('tioken:',token)
            print('ret:',ret)
            return token







    async def createProduct(self,db:AsyncSession,merchantid:str,product_id:str)->Any:
        url='/api/products'
        pass







    async def getProductList(self, db: AsyncSession, store: Models.Store) -> Any:

        url = "/v2/products"
        params={"site_id":2000,"limit":100,'offset':0}
        while 1:
            ret=await self.get(store,url,params)
            print("ret::",ret)
            yield ret["results"]
            if len(ret["results"])<100:
                break




    async def getOrderList(self,db:AsyncSession,store:Models.Store,starttime:int)->Any:
        url='/v2/orders'
        offset=0

        while 1:
            params = {"limit": 100, 'offset': offset, 'sort[modified]': 'desc','site_id':2000}
            ret=await self.get(store,url,params)
            print('ret:',ret)
            yield ret['results']
            if not ret['results']:
                break
            update_at=ret['results'][-1]["updated_at"]
            offset+=100
            if datetime.datetime.fromisoformat(update_at).timestamp()<=starttime:
                break

    async def syncOrder(self, db: AsyncSession, merchant_id: int, store: Models.Store, starttime: int) -> Any:
        async for remoteOrders in self.getOrderList(db,store,starttime):
            if not remoteOrders:
                break
            needsync={remoteOrder["order_id"]:remoteOrder for remoteOrder in remoteOrders}
            print('needSync:',needsync)
            needupdate={}
            ourdbmodels=await Service.orderService.find(db,{'market_order_number__in':needsync.keys(),"store_id":store.store_id})
            for model in ourdbmodels:
                tmstamp = model.market_updatetime.timestamp() if not isinstance(model.market_updatetime,#type: ignore
                                                                                str) else parse(
                    model.market_updatetime).timestamp()  # type: ignore

                if tmstamp!=parse(needsync[model.market_order_number]["updated_at"]).timestamp():
                    needupdate[model.order_id]=needsync[model.market_order_number] #wisshproduct_id 我们数据库主键 wish_id wish数据库主键
                del needsync[model.market_order_number]

            try:
                await onbuyutil.addOrders(db,needsync.values(),store,merchant_id)
            except TokenException as e:
                await db.rollback()
                store.status=0
                store.status_msg='token expired'



    async def getOrderDetail(self, db: AsyncSession, merchantid: str, order_id: str) -> Any:
        pass
if __name__=='__main__':
    import asyncio
    from common import cmdlineApp, TokenException


    @cmdlineApp
    async def t(db:AsyncSession)->None:
        onbuy=OnBuyService()
        store=await Service.storeService.findByPk(db,5)
        await onbuy.getToken(store)
        #await onbuy.getBrands(db,99071137052361794)#type: ignore
        #await onbuy.getProductList(db,99071137052361794)#type: ignore
        #await onbuy.getOrderList(db,99071137052361794)#type: ignore
        #await onbuy.getAuthorizedStore(db,99071137052361794)#type: ignore
    t()





