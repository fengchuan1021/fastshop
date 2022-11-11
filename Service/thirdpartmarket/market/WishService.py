
import asyncio
import datetime
from typing import Generator, Any
import orjson
from dateutil import parser
from sqlalchemy.ext.asyncio import AsyncSession

import settings
import aiohttp
from XTTOOLS import cache
from Service.thirdpartmarket import Market
class WishService(Market):
    def __init__(self)->None:
        self.session = aiohttp.ClientSession(base_url=settings.WISH_BASEURL)
    def getPermissionUrl(self)->str:
        return settings.WISH_BASEURL+f"/v3/oauth/authorize?client_id={settings.WISH_CLIENTID}"
    # async def init(self)->'WishService':
    #     self.baseurl = settings.WISH_BASEURL
    #     self.access_token = (await cache.get("wishtoken")).decode()
    #     if not self.access_token:
    #         self.session = aiohttp.ClientSession(base_url=self.baseurl)
    #         await self.getAccessToken()
    #     self.session = aiohttp.ClientSession(base_url=self.baseurl,headers={'authorization': f'Bearer {self.access_token}'})
    #     return self

    async def getAccessToken(self,code:str)->None:
        url ="/api/v3/oauth/access_token"

        payload = {"client_id":settings.WISH_CLIENTID,"client_secret":settings.WISH_SECRET,"code":code,"grant_type":"authorization_code","redirect_uri":settings.WISH_REDIRECT_URL}
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer REPLACE_BEARER_TOKEN"
        }
        print('payload',payload)
        async with self.session.post(url,json=payload,headers=headers) as resp:
            ret=await resp.json()
            return ret
            print("tokenfromwish:",ret)
            self.access_token=ret['data']['access_token']
            self.refresh_token=ret['data']['refresh_token']
            await cache.set("wishtoken",self.access_token,int(parser.parse(ret['data']['expiry_time']).timestamp()-3600*12-datetime.datetime.now().timestamp()))
            await cache.set('wishrefreshtoken',self.refresh_token)

    #some error
    async def getBrandList(self)->None:
        url ="/api/v3/brands"
        params={"limit": "100"}
        print(self.session.headers)
        async with self.session.get(url,params=params) as resp:
            ret=await resp.json()
            print(ret)
    async def getCurrencyList(self)->None:
        url='/api/v3/currencies'
        async with self.session.get(url) as resp:
            ret=await resp.json()
            print(ret)

    async def getOrders(self,ordertype='WISH_EXPRESS')->None:#type: ignore
        url='/api/v3/orders'
        params={'states':'REQUIRE_REVIEW'}
        async with self.session.get(url,params=params) as resp:

            ret=await resp.json()
            print('ret:',ret)
    async def createProduct(self):#type: ignore
        url='/api/v3/products'
        async with self.session.post(url) as resp:
            ret=await resp.json()

    async def getOrderDetail(self,db:AsyncSession,enterprise_id:str,order_id:str)->Any:
        url=f'/api/v3/orders/{order_id}'
        async with self.session.get(url) as resp:
            ret=await resp.json()
            return ret
if __name__ == '__main__':
    import asyncio
    async def test():#type: ignore
        wishService=WishService()
        await wishService.getAccessToken()
        #await wishService.getCurrencyList()
        #await wishService.getBrandList()
        #await wishService.getOrders()
    asyncio.run(test())