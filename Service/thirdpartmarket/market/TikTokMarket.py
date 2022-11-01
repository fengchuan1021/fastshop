
import asyncio
import base64
import datetime
import time
from typing import Generator, Dict
import orjson
from dateutil import parser
from sqlalchemy.ext.asyncio import AsyncSession

from hashlib import sha256
import hmac
import Service
import settings
import aiohttp
from component.cache import cache
from urllib.parse import urlencode
class TikTokMarket():
    def __init__(self,db:AsyncSession,enterprise_id:str):
        self.session=None
        self.enterprise=None
        self.token=''
        self.secret=''
        self.db=db
        self.enterprise_id=enterprise_id
        self.BASE_URL = settings.TIKTOK_APIURL
    async def init(self)->'TikTokMarket':
        enterprise = await Service.enterpriseService.findByPk(self.db, self.enterprise_id)
        if not enterprise:
            raise Exception("enterprise info not found")
        self.token= enterprise.tiktok_token# 'access_token':
        self.secret=enterprise.tiktok_secret
        self.commonparams={'app_key':enterprise.tiktok_appid,
                           'shop_id':enterprise.tiktok_shopid
                           }

        self.session = aiohttp.ClientSession(base_url=self.BASE_URL)#type: ignore
        return self
    def __await__(self):#type: ignore
        return self.init().__await__()#type: ignore

    def get_sign(self,data:str, key:str)->str:
        # key = key.encode('utf-8')
        # message = data.encode('utf-8')
        sign = hmac.new(key.encode('utf-8'), data.encode('utf-8'), digestmod=sha256).hexdigest()
        return sign

    def buildurl(self,url:str,params:Dict={})->str:
        params.update(self.commonparams)
        params['timestamp']=str(int(time.time()))
        signstring = self.secret + url
        for key in sorted(params):
            signstring = signstring + key + params[key]
        signstring = signstring + self.secret
        sign=self.get_sign(signstring,self.secret)
        params['access_token']=self.token
        params['sign']=sign
        return f'{url}?{urlencode(params)}'

    async def getProductList(self)->None:
        url = "/api/products/search"
        url=self.buildurl(url,{})
        payload={'page_number':1,'page_size':100}
        async with self.session.post(url,json=payload) as resp:#type: ignore
            ret=await resp.json()

            print(ret)

if __name__=='__main__':
    import asyncio
    from common.dbsession import getdbsession
    async def t()->None:
        async with getdbsession() as db:
            tiktok=await TikTokMarket(db,99071137052361794)#type: ignore
            await tiktok.getProductList()
    asyncio.run(t())





