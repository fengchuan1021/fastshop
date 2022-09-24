#type: ignore
import asyncio
import datetime
from typing import Generator
import orjson
from dateutil import parser
import settings
import aiohttp
from component.cache import cache
# class WishService():
#     async def init(self)->None:
#         self.baseurl = settings.WISH_BASEURL
#         self.access_token=await cache.get("wishtoken")
#         if not self.access_token:
#             await self.getAccessToken()
#         self.session = aiohttp.ClientSession(base_url=self.baseurl,headers={'authorization': f'Bearer {self.access_token}'})
#     def __await__(self):
#         return self.init().__await__()
#     def __int__(self)->None:
#         try:
#             loop=asyncio.get_running_loop()
#         except Exception as e:
#             loop=asyncio.new_event_loop()
#             asyncio.set_event_loop(loop)
#         loop.run_until_complete(self.init())
#     async def getAccessToken(self)->None:
#         url ="/api/v3/oauth/access_token"
#
#         payload = {"client_id":settings.WISH_CLIENDID,"client_secret":settings.WISH_CLIENDID,"code":settings.WISH_CODE,"grant_type":"authorization_code","redirect_uri":settings.WISH_REDIRECT_URL}
#         headers = {
#             'content-type': "application/json",
#             'authorization': "Bearer REPLACE_BEARER_TOKEN"
#         }
#
#         async with self.session.post(url,json=payload,headers=headers) as resp:
#             ret=await resp.json()
#             self.access_token=ret['access_token']
#             cache.set("wishtoken",ret['access_token'],parser.parse(ret['expiry_time']).timestamp()-3600*12-datetime.datetime.now().timestamp())
#             cache.set('wishrefreshtoken',ret["refresh_token"])
#
#     async def getBrandList(self)->None:
#         url ="/api/v3/brands"
#         params={"limit": "500"}
#         async with self.session.get(url,data=params) as resp:
#             ret=resp.json()
#             print(ret)
#     async def getCurrencyList(self)->None:
#         url='/api/v3/currencies'
#         async with self.session.get(url) as resp:
#             ret=resp.json()
#             print(ret)
