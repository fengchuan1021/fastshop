
import asyncio
import base64
import datetime
import time
from typing import Generator, Dict, List, TYPE_CHECKING, cast, Any
import orjson
from dateutil import parser
from sqlalchemy.ext.asyncio import AsyncSession

from hashlib import sha256
import hmac

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

    async def getEnterprise(self,db:AsyncSession,enterprise_id:str)->Models.Enterprise:
        enterprise = await Service.enterpriseService.findByPk(db, enterprise_id)
        if not enterprise:
            raise Exception("enterprise info not found")
        return enterprise
    async def getToken(self,enterprise:Models.Enterprise=None)->str:

        if TYPE_CHECKING:
            enterprise=cast(Models.Enterprise,enterprise)
        tmp=await cache.get(f'onbuy_token:{enterprise.enterprise_id}',decodestr=True)
        print("token:",tmp)
        if tmp:
            return tmp
        form = aiohttp.FormData()
        form.add_field('secret_key',enterprise.onbuy_secret )
        form.add_field('consumer_key',enterprise.onbuy_key)
        print('key:',form.__dict__)
        async with self.session.post('/v2/auth/request-token',data=form) as resp:
            t=await resp.text()
            print('baseurl:',settings.ONBUY_APIURL)
            print('t:',t)
            data=await resp.json()
            token=data["access_token"]
            await cache.set(f'onbuy_token:{enterprise.enterprise_id}',token,int(data['expires_at'])-int(time.time()))
            return token
    async def buildurl(self,url:str,params:Dict={},enterprise:'Models.Enterprise'=None)->str:
        if TYPE_CHECKING:
            enterprise=cast(Models.Enterprise,enterprise)
        token=await self.getToken(enterprise)
        self.session.headers.update({'Authorization':token})
        return f'{url}?{urlencode(params)}'

    async def getBrands(self,db:AsyncSession,enterprise_id:str)->Any:
        url='/v2/brands'
        params={'filter[name]':'life','sort[name]':'desc','limit':5,'offset':0}
        enterprisemodel = await self.getEnterprise(db, enterprise_id)
        url=await self.buildurl(url,params,enterprisemodel)
        async with self.session.get(url) as resp:
            data=await resp.json()
            print('brands:',data)




    async def createProduct(self,db:AsyncSession,enterprise_id:str,product_id:str)->Any:
        url='/api/products'
        pass
        # enterprisemodel = await self.getEnterprise(db, enterprise_id)
        # url = self.buildurl(url, {}, enterprisemodel)
        #
        # #data productdata
        # data:Dict={}
        #
        # async with self.session.post(url,json=data) as resp:
        #     ret=await resp.json()

    async def deleteProduct(self,db:AsyncSession,enterprise_id:str,product_id:str)->Any:
        url='/api/products'
        pass
        # enterprisemodel = await self.getEnterprise(db, enterprise_id)
        #
        # url = self.buildurl(url, {"product_ids":[123,456]}, enterprisemodel)
        #
        #
        # async with self.session.delete(url) as resp:
        #     ret=await resp.json()


    async def getProductList(self,db:AsyncSession,enterprise_id:str)->List:#type: ignore
        url = "/api/products/search"
        pass
        # enterprisemodel=await self.getEnterprise(db,enterprise_id)
        # url=self.buildurl(url,{},enterprisemodel)
        # payload={'page_number':1,'page_size':100}
        # async with self.session.post(url,json=payload) as resp:#type: ignore
        #     ret=await resp.json()
        #     print(ret)
        #     return ret
    async def getOrderList(self,db:AsyncSession,enterprise_id:str)->List:#type: ignore
        url = "/api/orders/search"
        pass
        # enterprisemodel=await Service.enterpriseService.findByPk(db,enterprise_id)
        # url=self.buildurl(url,{},enterprisemodel)
        # async with self.session.post(url,json={'page_size':20}) as resp:
        #     ret=await resp.json()
        #     print(ret)
        #     return ret

    async def getOrderDetail(self, db: AsyncSession, enterprise_id: str, order_id: str) -> Any:
        pass
if __name__=='__main__':
    import asyncio
    import sys

    from common.dbsession import getdbsession
    async def t()->None:
        async with getdbsession() as db:
            onbuy=OnBuyService()
            await onbuy.getBrands(db,99071137052361794)#type: ignore
            #await onbuy.getProductList(db,99071137052361794)#type: ignore
            #await onbuy.getOrderList(db,99071137052361794)#type: ignore
            #await onbuy.getAuthorizedShop(db,99071137052361794)#type: ignore
    asyncio.run(t())





