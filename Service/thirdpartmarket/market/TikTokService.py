import time
from typing import Dict, List, TYPE_CHECKING, cast, Any
from sqlalchemy.ext.asyncio import AsyncSession

from hashlib import sha256
import hmac

import Models
import Service
import settings
import aiohttp
from urllib.parse import urlencode
from Service.thirdpartmarket import Market
class TikTokService(Market):
    def __init__(self)->None:
        self.session = aiohttp.ClientSession(base_url=settings.TIKTOK_APIURL)

    async def getStore(self,db:AsyncSession,store_id:str)->Models.Store:
        store = await Service.storeService.findByPk(db, store_id)
        if not store:
            raise Exception("merchant info not found")
        return store

    def get_sign(self,data:str, key:str)->str:
        sign = hmac.new(key.encode('utf-8'), data.encode('utf-8'), digestmod=sha256).hexdigest()
        return sign

    def buildurl(self,url:str,params:Dict=None,store:'Models.Store'=None)->str:
        if TYPE_CHECKING:
            store=cast(Models.Store,store)
        params.update({'app_key':store.appid,'store_id':store.appkey})#type: ignore
        params['timestamp']=str(int(time.time()))#type: ignore
        signstring:str = merchant.tiktok_secret + url#type: ignore
        for key in sorted(params):#type: ignore
            signstring = signstring + key + params[key]#type: ignore
        signstring = signstring + merchant.tiktok_secret#type: ignore
        sign=self.get_sign(signstring,merchant.tiktok_secret)#type: ignore
        params['access_token']=store.token#type: ignore
        params['sign']=sign#type: ignore
        return f'{url}?{urlencode(params)}'#type: ignore

    async def getAuthorizedStore(self,db:AsyncSession,store_id:str)->Any:
        url = "/api/store/get_authorized_store"
        merchantmodel = await self.getStore(db, store_id)
        url = self.buildurl(url, {}, merchantmodel)
        async with self.session.get(url) as resp:#type: ignore
            ret=await resp.json()
            print(ret)
            return ret
    async def getActiveStoreList(self,db:AsyncSession,store_id:str)->Any:
        url = "/api/seller/global/active_stores"
        merchantmodel = await self.getStore(db, store_id)
        url = self.buildurl(url, {}, merchantmodel)
        async with self.session.get(url) as resp:#type: ignore
            ret=await resp.json()
            print(ret)
            return ret
    async def createProduct(self,db:AsyncSession,store_id:str,product_id:str)->Any:
        url='/api/products'
        merchantmodel = await self.getStore(db, store_id)
        url = self.buildurl(url, {}, merchantmodel)

        #data productdata
        data:Dict={}

        async with self.session.post(url,json=data) as resp:
            ret=await resp.json()

    async def deleteProduct(self,db:AsyncSession,store_id:str,product_id:str)->Any:
        url='/api/products'
        merchantmodel = await self.getStore(db, store_id)

        url = self.buildurl(url, {"product_ids":[123,456]}, merchantmodel)


        async with self.session.delete(url) as resp:
            ret=await resp.json()


    async def getProductList(self,db:AsyncSession,store_id:str)->List:
        url = "/api/products/search"
        merchantmodel=await self.getStore(db,store_id)
        url=self.buildurl(url,{},merchantmodel)
        payload={'page_number':1,'page_size':100}
        async with self.session.post(url,json=payload) as resp:#type: ignore
            ret=await resp.json()
            print(ret)
            return ret
    async def getOrderList(self,db:AsyncSession,store_id:str)->List:
        url = "/api/orders/search"
        merchantmodel=await Service.storeService.findByPk(db,store_id)
        url=self.buildurl(url,{},merchantmodel)
        async with self.session.post(url,json={'page_size':20}) as resp:
            ret=await resp.json()
            print(ret)
            return ret

    async def getOrderDetail(self, db: AsyncSession, store_id: str, order_id: str) -> Any:
        url='/api/orders/detail/query'
        merchantmodel = await Service.storeService.findByPk(db, store_id)
        url = self.buildurl(url, {}, merchantmodel)
        async with self.session.post(url,json={'order_id_list':[order_id]}) as resp:
            ret=await resp.json()
            return ret


if __name__=='__main__':
    import asyncio

    from component.dbsession import getdbsession
    async def t()->None:
        async with getdbsession() as db:
            tiktok=TikTokService()

            await tiktok.getProductList(db,99071137052361794)#type: ignore
            await tiktok.getOrderList(db,99071137052361794)#type: ignore
            await tiktok.getAuthorizedStore(db,99071137052361794)#type: ignore
    asyncio.run(t())





