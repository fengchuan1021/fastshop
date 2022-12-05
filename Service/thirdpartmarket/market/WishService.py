import settings
import asyncio
import datetime
from typing import Generator, Any, List, Dict, TYPE_CHECKING, cast, Optional
import orjson
import pytz,os #type: ignore
from dateutil.parser import parse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request
from urllib.parse import urlencode

from sqlalchemy.orm import Load
#from sqlalchemy.orm.strategy_options import load_only
import math
import Models
import Service

import aiohttp

from common.CommonError import ResponseException
from component.cache import cache
from Service.thirdpartmarket import Market

if __name__=='__main__':
    import wishutil
else:
    from . import wishutil


from component.snowFlakeId import snowFlack


class WishService(Market):
    def __init__(self) -> None:
        pass
        # self.session = aiohttp.ClientSession(base_url=settings.WISH_BASEURL)

    def getAuthorizationUrl(self, shop_id: int) -> str:
        return settings.WISH_BASEURL + f"/v3/oauth/authorize?client_id={settings.WISH_CLIENTID}&state={shop_id}"

    def onAuthriaztionCallBack(self, request: Request) -> None:
        if shop_id := request.query_params.get('state', ''):
            pass
        else:
            pass
        # https://example.redirect.uri.com?code={authorization_code}
        pass

    # async def init(self)->'WishService':
    #     self.baseurl = settings.WISH_BASEURL
    #     self.access_token = (await cache.get("wishtoken")).decode()
    #     if not self.access_token:
    #         self.session = aiohttp.ClientSession(base_url=self.baseurl)
    #         await self.getAccessToken()
    #     self.session = aiohttp.ClientSession(base_url=self.baseurl,headers={'authorization': f'Bearer {self.access_token}'})
    #     return self
    async def post(self,url:str,store:Models.Store,body:Dict=None,headers:Dict=None)->Any:
        tokenheader={'authorization': f'Bearer {store.token}'}
        if headers:
            tokenheader.update(headers)
        async with aiohttp.ClientSession() as session:
            async with session.post(settings.WISH_BASEURL+url,json=body,headers=tokenheader) as resp:
                return await resp.json()
    async def get(self,url: str, store: Optional[Models.Store], params: Dict = None) -> Any:
        store=cast(Models.Store,store)
        if not params:
            params = {}
        async with aiohttp.ClientSession() as session:
            if params:
                finalurl = f'{settings.WISH_BASEURL}{url}?{urlencode(params)}'
            else:
                finalurl = settings.WISH_BASEURL + url
            async with session.get(finalurl, headers={'authorization': f'Bearer {store.token}'}) as response:

                return await response.json()
    async def getAccessToken(self, code: str) -> None:
        url = "/api/v3/oauth/access_token"

        payload = {"client_id": settings.WISH_CLIENTID, "client_secret": settings.WISH_SECRET, "code": code,
                   "grant_type": "authorization_code", "redirect_uri": settings.WISH_REDIRECT_URL}
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer REPLACE_BEARER_TOKEN"
        }
        print('payload', payload)
        #data=await  self.post(url,payload,headers)
        # async with self.session.post(url, json=payload, headers=headers) as resp:
        #     ret = await resp.json()
        #     return ret
        #     print("tokenfromwish:", ret)
        #     self.access_token = ret['data']['access_token']
        #     self.refresh_token = ret['data']['refresh_token']
        #     await cache.set("wishtoken", self.access_token, int(parser.parse(
        #         ret['data']['expiry_time']).timestamp() - 3600 * 12 - datetime.datetime.now().timestamp()))
        #     await cache.set('wishrefreshtoken', self.refresh_token)

    # some error
    async def getBrandList(self) -> None:
        url = "/api/v3/brands"
        params = {"limit": "100"}
        #print(self.session.headers)
        data=await self.get(url,None,params)
        # async with self.session.get(url, params=params) as resp:
        #     ret = await resp.json()
        #     print(ret)

    async def getCurrencyList(self) -> None:
        url = '/api/v3/currencies'
        data=await self.get(url,None)
        # async with self.session.get(url) as resp:
        #     ret = await resp.json()
        #     print(ret)

    async def getOrderList(self, db:AsyncSession,store:Models.Store) -> List:  # type: ignore
        url = '/api/v3/orders'
        params = {'states': 'REQUIRE_REVIEW'}
        data=await self.get(url,store,params)
        print("order:",data)

        return data['data']

    async def createProduct(self):  # type: ignore
        url = '/api/v3/products'
        async with self.session.post(url) as resp:
            ret = await resp.json()

    async def getOrderDetail(self, db: AsyncSession, store:Models.Store, order_id: str) -> Any:
        url = f'/api/v3/orders/{order_id}'
        data=await self.get(url,None)
        # async with self.session.get(url) as resp:
        #     ret = await resp.json()
        #     return ret



    async def getProductList(self, db: AsyncSession, store: Models.Store) ->Any:
        url = '/api/v3/products'
        LIMIT=500
        updated_at_max=None
        params={'limit': LIMIT}
        while 1:
            if updated_at_max:
                params['updated_at_max']=updated_at_max
            result = await self.get(url, store,params )
            data = result['data']#type: ignore
            if data:
                updated_at_max=data[-1]["updated_at"]
            yield data
            if len(result['data']) < LIMIT:#type: ignore
                break
    async def getProductDetail(self, db: AsyncSession, store: Models.Store, product_id: str,sem:Any=None)->Any:
        url=f'/api/v3/products/{product_id}'
        while 1:
            if sem:
                async with sem:
                    data=await self.get(url,store)
                    await asyncio.sleep(1)
            else:
                data = await self.get(url, store)
            if data['code']==1056:#频率限制
                print('overload')
                await asyncio.sleep(1)
            else:
                return data['data']
    async def fullsyncProduct(self,db:AsyncSession,store:Models.Store,merchant_id:int)->Any:
        url='/api/v3/products/bulk_get'
        data=await self.post(url,store)
        if data['code']==0:
            id=data['data']['id']
            while 1:
                await asyncio.sleep(7)
                statusdata=await self.get(f'/api/v3/products/bulk_get/{id}',store)
                if statusdata['data']['status']=="READY":
                    for url in statusdata['data']["file_urls"]:
                        async with aiohttp.ClientSession() as session:
                            async with session.get(url) as resp:
                                txt=await resp.text()
                                results=[orjson.loads(l) for l in txt.split('\n') if l]
                                await wishutil.addproducts(db,results,store.store_id,merchant_id)

                    break
                elif statusdata['data']['status']=="EXCEPTION":
                    raise ResponseException({'status':'failed','msg':"wish sync proudct failed"})

    async def incrementSync(self,db:AsyncSession,store:Models.Store,merchant_id:int)->Any:
        async for productSummarys in self.getProductList(db,store):
            needsync = {productSummary["id"]:productSummary['updated_at'] for productSummary in productSummarys}
            needupdate={}
            ourdbmodels=await Service.wishproductService.find(db,{"wish_id__in":needsync.keys()},Load(Models.WishProduct).load_only(Models.WishProduct.wish_id,Models.WishProduct.updated_at))
            for model in ourdbmodels:
                if os.name=='nt':#for timezone bug in windows
                    if isinstance(model.updated_at,str):
                        tmstamp=parse(model.updated_at).replace(tzinfo=pytz.UTC).timestamp()
                    else:
                        tmstamp=model.updated_at.replace(tzinfo=pytz.UTC).timestamp()#type: ignore
                else:
                    tmstamp=model.updated_at.timestamp() if not isinstance(model.updated_at,str) else parse(model.updated_at).timestamp()#type: ignore
                if tmstamp!=parse(needsync[model.wish_id]).timestamp():
                    needupdate[model.wishproduct_id]=model.wish_id #wisshproduct_id 我们数据库主键 wish_id wish数据库主键
                del needsync[model.wish_id]
            sem = asyncio.Semaphore(20)#35并发量 wish有速度限制
            newproducts_task=[self.getProductDetail(db,store,product_id,sem) for product_id in needsync]#:#add new product

            result=await asyncio.gather(*newproducts_task)
            await wishutil.addproducts(db,result,store.store_id,merchant_id)

            for ourdbid,product_id in needupdate.items():
                print('needupdate',product_id)

    async def syncProduct(self,db:AsyncSession,store:Models.Store,merchant_id:int)->Any:
        hassyncbefore=await Service.wishproductService.findOne(db,{"store_id":store.store_id})
        if not hassyncbefore:
            await self.fullsyncProduct(db,store,merchant_id)
        else:
            await self.incrementSync(db,store,merchant_id)

    async def importToXT(self,db:AsyncSession,merchant_id:int,store:Models.Store)->Any:
        datas=await self.getProductList(db,store)#type: ignore
        for data in datas:
            sku=data["parent_sku"]
            variant=await Service.variantService.findOne(db,{"sku":sku,'merchant_id':merchant_id})
            if variant: #db has a variant same sku
                variantstore=await Service.variantstoreService.findOne(db,{'merchant_id':merchant_id,'variant_id':variant.variant_id})
                if variantstore:#has in variant_store table
                    pass
                else:
                    variantstore=Models.VariantStore(variant_id=variant.variant_id,store_name='wish',price=0,
                                                     status="ONLINE",
                                                     market_variant_status=data["status"],
                                                     product_id=variant.product_id,
                                                     merchant_id=merchant_id,

                                                     )
                    db.add(variantstore)
            else:#没在xt上找到sku相同的产品
                product=Models.Product(sku=sku,
                                       title=data['name'],
                                       description=data["description"],
                                       )
                variant=Models.Variant()

            product=Models.Product()
            variant=Models.Variant()



if __name__ == '__main__':
    import asyncio

    import time,os
    from component.dbsession import getdbsession
    os.environ['TZ'] = 'Europe/London'
    #time.tzset()
    from ctypes import cdll
    cdll.msvcrt._tzset ()

    async def test():  # type: ignore
        wishService = WishService()
        async with getdbsession() as db:
            store = await Service.storeService.findByPk(db, 1)
            await Service.wishService.backgroundsyncProduct(db, store)
        # await wishService.getCurrencyList()
        # await wishService.getBrandList()
        # await wishService.getOrders()


    asyncio.run(test())
