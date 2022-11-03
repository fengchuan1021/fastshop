
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
class TikTokService(Market):
    def __init__(self)->None:
        self.session = aiohttp.ClientSession(base_url=settings.TIKTOK_APIURL)

    async def getEnterprise(self,db:AsyncSession,enterprise_id:str)->Models.Enterprise:
        enterprise = await Service.enterpriseService.findByPk(db, enterprise_id)
        if not enterprise:
            raise Exception("enterprise info not found")
        return enterprise

    def get_sign(self,data:str, key:str)->str:
        sign = hmac.new(key.encode('utf-8'), data.encode('utf-8'), digestmod=sha256).hexdigest()
        return sign

    def buildurl(self,url:str,params:Dict={},enterprise:'Models.Enterprise'=None)->str:
        if TYPE_CHECKING:
            enterprise=cast(Models.Enterprise,enterprise)
        params.update({'app_key':enterprise.tiktok_appid,'shop_id':enterprise.tiktok_shopid})
        params['timestamp']=str(int(time.time()))
        signstring:str = enterprise.tiktok_secret + url#type: ignore
        for key in sorted(params):
            signstring = signstring + key + params[key]
        signstring = signstring + enterprise.tiktok_secret#type: ignore
        sign=self.get_sign(signstring,enterprise.tiktok_secret)#type: ignore
        params['access_token']=enterprise.tiktok_token
        params['sign']=sign
        return f'{url}?{urlencode(params)}'

    async def getAuthorizedShop(self,db:AsyncSession,enterprise_id:str)->Any:
        url = "/api/shop/get_authorized_shop"
        enterprisemodel = await self.getEnterprise(db, enterprise_id)
        url = self.buildurl(url, {}, enterprisemodel)
        async with self.session.get(url) as resp:#type: ignore
            ret=await resp.json()
            print(ret)
            return ret
    async def getActiveShopList(self,db:AsyncSession,enterprise_id:str)->Any:
        url = "/api/seller/global/active_shops"
        enterprisemodel = await self.getEnterprise(db, enterprise_id)
        url = self.buildurl(url, {}, enterprisemodel)
        async with self.session.get(url) as resp:#type: ignore
            ret=await resp.json()
            print(ret)
            return ret
    async def createProduct(self,db:AsyncSession,enterprise_id:str,product_id:str)->Any:
        url='/api/products'
        enterprisemodel = await self.getEnterprise(db, enterprise_id)
        url = self.buildurl(url, {}, enterprisemodel)

        #data productdata
        data:Dict={}

        async with self.session.post(url,json=data) as resp:
            ret=await resp.json()

    async def deleteProduct(self,db:AsyncSession,enterprise_id:str,product_id:str)->Any:
        url='/api/products'
        enterprisemodel = await self.getEnterprise(db, enterprise_id)

        url = self.buildurl(url, {"product_ids":[123,456]}, enterprisemodel)


        async with self.session.delete(url) as resp:
            ret=await resp.json()


    async def getProductList(self,db:AsyncSession,enterprise_id:str)->List:
        url = "/api/products/search"
        enterprisemodel=await self.getEnterprise(db,enterprise_id)
        url=self.buildurl(url,{},enterprisemodel)
        payload={'page_number':1,'page_size':100}
        async with self.session.post(url,json=payload) as resp:#type: ignore
            ret=await resp.json()
            print(ret)
            return ret
    async def getOrderList(self,db:AsyncSession,enterprise_id:str)->List:
        url = "/api/orders/search"
        enterprisemodel=await Service.enterpriseService.findByPk(db,enterprise_id)
        url=self.buildurl(url,{},enterprisemodel)
        async with self.session.post(url,json={'page_size':20}) as resp:
            ret=await resp.json()
            print(ret)
            return ret
if __name__=='__main__':
    import asyncio
    import sys

    from common.dbsession import getdbsession
    async def t()->None:
        async with getdbsession() as db:
            tiktok=TikTokService()

            await tiktok.getProductList(db,99071137052361794)#type: ignore
            await tiktok.getOrderList(db,99071137052361794)#type: ignore
            await tiktok.getAuthorizedShop(db,99071137052361794)#type: ignore
    asyncio.run(t())





