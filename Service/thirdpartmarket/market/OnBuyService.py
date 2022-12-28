import datetime
import time
from typing import Dict, List, TYPE_CHECKING, cast, Any, Literal
from sqlalchemy.ext.asyncio import AsyncSession
from dateutil.parser import parse
import Models
import Service
import settings
from Service.thirdpartmarket.Shema import Shipinfo

if __name__ == '__main__':
    import onbuyutil
else:
    from . import onbuyutil
import aiohttp
from common import TokenException
from component.cache import cache
from urllib.parse import urlencode
import asyncio
from modules.merchant.product.onbuy.ProductShema import OnbuyCreateProductShema

from Service.thirdpartmarket import Market
class OnBuyService(Market):  # Market

    async def request(self, store: Models.Store, method: Literal["GET", "POST", "PUT"], url: str, params: Dict = None,
                      body: Dict = None, headers: Dict = None) -> Any:
        if not store.token_expiration or store.token_expiration - int(time.time()) < 120:
            await self.getToken(store)
        header = {'Authorization': store.token}
        if headers:
            header.update(headers)
        async with aiohttp.request(method, f'{settings.ONBUY_ENDPOINT}{url}', params=params, json=body,
                                   headers=header) as resp:  # type: ignore
            ret = await resp.json()
            return ret

    async def get(self, store: Models.Store, url: str, params: Dict = None) -> Any:
        ret = await self.request(store, 'GET', url, params)
        return ret

    async def post(self, store: Models.Store, url: str, body: Dict = None) -> Any:
        ret = await self.request(store, 'POST', url, body=body)
        return ret
    async def put(self, store: Models.Store, url: str, body: Dict = None) -> Any:
        ret = await self.request(store, 'PUT', url, body=body)
        return ret
    async def getBrands(self,db:AsyncSession,store:Models.Store,searchname:str)->Any:
        url='/v2/brands'
        ret=await self.get(store,url,{'filter[name]':searchname})
        return ret

    async def getToken(self, store: Models.Store) -> str:
        form = aiohttp.FormData()
        form.add_field('secret_key', store.appkey)
        form.add_field('consumer_key', store.appsecret)
        async with aiohttp.request("POST", f'{settings.ONBUY_ENDPOINT}/v2/auth/request-token', data=form) as resp:
            ret = await resp.json()
            token = ret["access_token"]
            store.token = token
            store.token_expiration = int(ret['expires_at'])
            print('tioken:', token)
            print('ret:', ret)
            return token
    async def shiPackage(self,db:AsyncSession,store:Models.Store,shipinfo:Shipinfo,order:Models.Order,ordershipmentitems:List[Models.OrderShipmentItem])->Any:
        '''发货'''

        url='/v2/orders/dispatch'
        body={
            "orders": [
                {
                    "order_id": shipinfo.order_id,
                    "products": [
                        {
                            "sku": "EXP-143-33S",
                            "quantity": 122
                        }
                    ],
                    "tracking": {
                       #"tracking_id": "bar",
                        "supplier_name":shipinfo.shipping_provider,
                        "number": shipinfo.track_number
                    }
                }
            ]
        }
        body['orders'][0]["products"] = [{"sku":item.sku,"quantity":item.qty} for item in ordershipmentitems]
        ret=await self.put(store,url,body)

    async def getCategories(self,db:AsyncSession, store: Models.Store) -> Any:
        offset=0
        results=[]
        async def _getCategories(store: Models.Store) -> Any:
            nonlocal offset,results
            url = '/v2/categories'
            params = {'offset': offset, 'limit': 100, "site_id": 2000}
            while 1:
                params['offset'] = offset
                offset += 100
                ret = await self.get(store, url, params=params)
                if ret['results']:
                    results+=ret['results']
                else:
                    break
                if len(ret['results']) < 100:
                    break
        tasks=[_getCategories(store) for i in range(20)]
        await asyncio.gather(*tasks)

        return results

    async def createProduct(self, db: AsyncSession, store: Models.Store, body: OnbuyCreateProductShema):  # type: ignore
        url = '/v2/products'
        ret = await self.post(store,url,body.dict(exclude_unset=True))
        return ret

    async def getProductList(self, db: AsyncSession, store: Models.Store) -> Any:

        url = "/v2/products"
        params = {"site_id": 2000, "limit": 100, 'offset': 0}
        while 1:
            ret = await self.get(store, url, params)
            print("ret::", ret)
            yield ret["results"]
            if len(ret["results"]) < 100:
                break

    async def getOrderList(self, db: AsyncSession, store: Models.Store, starttime: int) -> Any:
        url = '/v2/orders'
        offset = 0

        while 1:
            params = {"limit": 100, 'offset': offset, 'sort[modified]': 'desc', 'site_id': 2000}
            ret = await self.get(store, url, params)
            print('ret:', ret)
            yield ret['results']
            if not ret['results']:
                break
            update_at = ret['results'][-1]["updated_at"]
            offset += 100
            if datetime.datetime.fromisoformat(update_at).timestamp() <= starttime:
                break

    async def syncOrder(self, db: AsyncSession, merchant_id: int, store: Models.Store, starttime: int) -> Any:
        async for remoteOrders in self.getOrderList(db, store, starttime):
            if not remoteOrders:
                break
            needsync = {remoteOrder["order_id"]: remoteOrder for remoteOrder in remoteOrders}
            print('needSync:', needsync)
            needupdate = {}
            ourdbmodels = await Service.orderService.find(db, {'market_order_id__in': needsync.keys(),
                                                               "store_id": store.store_id})
            for model in ourdbmodels:
                tmstamp = model.market_updatetime.timestamp() if not isinstance(model.market_updatetime,  # type: ignore
                                                                                str) else parse(
                    model.market_updatetime).timestamp()  # type: ignore

                if tmstamp != parse(needsync[model.market_order_id]["updated_at"]).timestamp():
                    needupdate[model.order_id] = needsync[
                        model.market_order_id]  # wisshproduct_id 我们数据库主键 wish_id wish数据库主键
                del needsync[model.market_order_id]

            try:
                await onbuyutil.addOrders(db, needsync.values(), store, merchant_id)
            except TokenException as e:
                await db.rollback()
                store.status = 0
                store.status_msg = 'token expired'

    async def getOrderDetail(self, db: AsyncSession, store: Models.Store,market_order_id:str) -> Any:
        pass


    async def getProductDetail(self,db:AsyncSession,store:Models.Store,product_id:str)->Any:
        raise NotImplementedError

    async def deleteProduct(self,db:AsyncSession,store:Models.Store,sku:str)->Any:
        raise NotImplementedError
    async def getTrackingProviders(self,db:AsyncSession,store:Models.Store)->Any:
        url='/v2/orders/tracking-providers?site_id=2000&limit=100'
        ret=await self.get(store,url)
        print(len(ret['results']))
        print(ret)

    async def updateStock(self,db:AsyncSession,store:Models.Store,sku:str,num:int)->Any:
        url='/v2/listings/by-sku'
        body={'site_id':2000,'listings':[
            {
                "sku": sku,
                "stock": num
            }
        ]}
        ret =await self.put(store, url, body)
        return ret
    async def updatePrice(self,db:AsyncSession,store:Models.Store,sku:str,price:float)->Any:
        url='/v2/listings/by-sku'
        body={'site_id':2000,'listings':[
            {
                "sku": sku,
                "price":price
            }
        ]}
        ret =await self.put(store,url,body)
        return ret
    async def offlineProduct(self,db:AsyncSession,store:Models.Store,sku:str)->List:
        raise NotImplementedError

    async def onlineProduct(self,db:AsyncSession,store:Models.Store,sku:str)->List:
        raise NotImplementedError
if __name__ == '__main__':
    import asyncio
    from common import cmdlineApp, TokenException


    @cmdlineApp
    async def t(db: AsyncSession) -> None:
        onbuy = OnBuyService()
        store = await Service.storeService.findByPk(db, 5)
        #await onbuy.getCategories(db,store)
        await onbuy.getTrackingProviders(db,store)
        # await onbuy.getToken(store)
        # await onbuy.getBrands(db,99071137052361794)#type: ignore
        # await onbuy.getProductList(db,99071137052361794)#type: ignore
        # await onbuy.getOrderList(db,99071137052361794)#type: ignore
        # await onbuy.getAuthorizedStore(db,99071137052361794)#type: ignore


    t()
