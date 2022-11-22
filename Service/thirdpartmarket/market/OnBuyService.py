import time
from typing import Dict, List, TYPE_CHECKING, cast, Any
from sqlalchemy.ext.asyncio import AsyncSession

import Models
import Service
import settings
import aiohttp
from component.cache import cache
from urllib.parse import urlencode
from Service.thirdpartmarket import Market
class OnBuyService(Market):
    def __init__(self)->None:
        self.session = aiohttp.ClientSession(base_url=settings.ONBUY_APIURL)

    async def getShop(self,db:AsyncSession,shop_id:str)->Models.Shop:
        shop = await Service.shopService.findByPk(db,shop_id)
        if not shop:
            raise Exception("shop info not found")
        return shop
    async def getToken(self,shop:Models.Shop=None)->str:

        if TYPE_CHECKING:
            shop=cast(Models.Shop,shop)
        tmp=await cache.get(f'onbuy_token:{shop.shop_id}',decodestr=True)
        print("token:",tmp)
        if tmp:
            return tmp
        form = aiohttp.FormData()
        form.add_field('secret_key',shop.appsecret )
        form.add_field('consumer_key',shop.appkey)
        print('key:',form.__dict__)
        async with self.session.post('/v2/auth/request-token',data=form) as resp:
            t=await resp.text()
            print('baseurl:',settings.ONBUY_APIURL)
            print('t:',t)
            data=await resp.json()
            token=data["access_token"]
            await cache.set(f'onbuy_token:{shop.shop_id}',token,int(data['expires_at'])-int(time.time()))
            return token
    async def buildurl(self,url:str,params:Dict={},shop:'Models.Shop'=None)->str:
        if TYPE_CHECKING:
            shop=cast(Models.Shop,shop)
        token=await self.getToken(shop)
        self.session.headers.update({'Authorization':token})
        return f'{url}?{urlencode(params)}'

    async def getBrands(self,db:AsyncSession,shop_id:str)->Any:
        url='/v2/brands'
        params={'filter[name]':'life','sort[name]':'desc','limit':5,'offset':0}
        shop= await self.getShop(db,shop_id)
        url=await self.buildurl(url,params,shop)
        async with self.session.get(url) as resp:
            data=await resp.json()
            print('brands:',data)




    async def createProduct(self,db:AsyncSession,merchantid:str,product_id:str)->Any:
        url='/api/products'
        pass
        # enterprisemodel = await self.getShop(db, merchantid)
        # url = self.buildurl(url, {}, enterprisemodel)
        #
        # #data productdata
        # data:Dict={}
        #
        # async with self.session.post(url,json=data) as resp:
        #     ret=await resp.json()

    async def deleteProduct(self,db:AsyncSession,shop_id:str,product_id:str)->Any:
        url='/2/listings/by-sku'

        shop= await self.getShop(db, shop_id)
        #
        skus=[1,2,3]
        url = await self.buildurl(url, {},shop)
        async with self.session.delete(url,json={"site_id":2000,"skus":skus}) as resp:
            result=await resp.json()
            print(result)



    async def getProductList(self,db:AsyncSession,shop_id:str)->List:#type: ignore
        url = "/v2/listings"
        shop= await self.getShop(db,shop_id)
        params={"site_id":2000}
        url=await self.buildurl(url,params,shop)
        async with self.session.get(url) as resp:
            json=await resp.json()
            print('josn:',json)


    async def getOrderList(self,db:AsyncSession,shop_id:str)->List:#type: ignore
        url = "/v2/orders"
        params={'site_id':2000,'filter[status]':'open','limit':20,'offset':0,'sort[created]':'desc'}
        shop = await self.getShop(db, shop_id)
        url=await self.buildurl(url,params,shop)
        async with self.session.get(url) as resp:
            data=await resp.json()
            print(data)
            return data


    async def getOrderDetail(self, db: AsyncSession, merchantid: str, order_id: str) -> Any:
        pass
if __name__=='__main__':
    import asyncio

    from component.dbsession import getdbsession
    async def t()->None:
        async with getdbsession() as db:
            onbuy=OnBuyService()
            #await onbuy.getBrands(db,99071137052361794)#type: ignore
            await onbuy.getProductList(db,99071137052361794)#type: ignore
            #await onbuy.getOrderList(db,99071137052361794)#type: ignore
            #await onbuy.getAuthorizedShop(db,99071137052361794)#type: ignore
    asyncio.run(t())





