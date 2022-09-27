#type: ignore
import asyncio
import datetime
from typing import Generator
import orjson
from dateutil import parser
import settings
import aiohttp
from component.cache import cache
class WishService():
    async def init(self)->None:
        self.baseurl = settings.WISH_BASEURL
        self.access_token = (await cache.get("wishtoken")).decode()
        if not self.access_token:
            self.session = aiohttp.ClientSession(base_url=self.baseurl)
            await self.getAccessToken()
        self.session = aiohttp.ClientSession(base_url=self.baseurl,headers={'authorization': f'Bearer {self.access_token}'})
        return self
    def __await__(self):
        return self.init().__await__()
    def __init__(self)->None:
        self.session=None

    async def getAccessToken(self)->None:
        url ="/api/v3/oauth/access_token"

        payload = {"client_id":settings.WISH_CLIENDID,"client_secret":settings.WISH_SECRET,"code":settings.WISH_CODE,"grant_type":"authorization_code","redirect_uri":settings.WISH_REDIRECT_URL}
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer REPLACE_BEARER_TOKEN"
        }
        print('payload',payload)
        async with self.session.post(url,json=payload,headers=headers) as resp:
            ret=await resp.json()
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

    async def getOrders(self,ordertype='WISH_EXPRESS'):
        url='/api/v3/orders'
        params={'states':'REQUIRE_REVIEW'}
        async with self.session.get(url,params=params) as resp:

            ret=await resp.json()
            print('ret:',ret)
    async def createProduct(self):
        url='/api/v3/products'
        async with self.session.post(url) as resp:
            ret=await resp.json()
if __name__ == '__main__':
    import asyncio
    async def test():
        wishService=await WishService()
        #await wishService.getCurrencyList()
        #await wishService.getBrandList()
        #await wishService.getOrders()
    asyncio.run(test())