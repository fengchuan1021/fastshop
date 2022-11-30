# type: ignore
import asyncio
import datetime
from typing import Generator, Any, List, Dict, TYPE_CHECKING, cast
import orjson
from dateutil import parser
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request
from urllib.parse import urlencode

import Models
import Service
import settings
import aiohttp
from component.cache import cache
from Service.thirdpartmarket import Market
from component.dbsession import getdbsession


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

    async def getAccessToken(self, code: str) -> None:
        url = "/api/v3/oauth/access_token"

        payload = {"client_id": settings.WISH_CLIENTID, "client_secret": settings.WISH_SECRET, "code": code,
                   "grant_type": "authorization_code", "redirect_uri": settings.WISH_REDIRECT_URL}
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer REPLACE_BEARER_TOKEN"
        }
        print('payload', payload)
        async with self.session.post(url, json=payload, headers=headers) as resp:
            ret = await resp.json()
            return ret
            print("tokenfromwish:", ret)
            self.access_token = ret['data']['access_token']
            self.refresh_token = ret['data']['refresh_token']
            await cache.set("wishtoken", self.access_token, int(parser.parse(
                ret['data']['expiry_time']).timestamp() - 3600 * 12 - datetime.datetime.now().timestamp()))
            await cache.set('wishrefreshtoken', self.refresh_token)

    # some error
    async def getBrandList(self) -> None:
        url = "/api/v3/brands"
        params = {"limit": "100"}
        print(self.session.headers)
        async with self.session.get(url, params=params) as resp:
            ret = await resp.json()
            print(ret)

    async def getCurrencyList(self) -> None:
        url = '/api/v3/currencies'
        async with self.session.get(url) as resp:
            ret = await resp.json()
            print(ret)

    async def getOrders(self, ordertype='WISH_EXPRESS') -> None:  # type: ignore
        url = '/api/v3/orders'
        params = {'states': 'REQUIRE_REVIEW'}
        async with self.session.get(url, params=params) as resp:
            ret = await resp.json()
            print('ret:', ret)

    async def createProduct(self):  # type: ignore
        url = '/api/v3/products'
        async with self.session.post(url) as resp:
            ret = await resp.json()

    async def getOrderDetail(self, db: AsyncSession, merchant_id: str, order_id: str) -> Any:
        url = f'/api/v3/orders/{order_id}'
        async with self.session.get(url) as resp:
            ret = await resp.json()
            return ret

    async def get(self, db: AsyncSession, url: str, store: Models.Store, params: Dict = None) -> str:
        print('store:', store)
        if not params:
            params = {}
        async with aiohttp.ClientSession() as session:
            if params:
                finalurl = f'{settings.WISH_BASEURL}{url}?{urlencode(params)}'
            else:
                finalurl = settings.WISH_BASEURL + url
            async with session.get(finalurl, headers={'authorization': f'Bearer {store.token}'}) as response:
                print('????')

                return await response.json()

    async def getProductList(self, db: AsyncSession, store: Models.Store) -> List:
        url = '/api/v3/products'
        data = []
        while 1:
            result = await self.get(db, url, store, {'limit': 1000})
            data += result['data']
            if len(result['data']) < 1000:
                break
        return data
    async def importToXT(self,db:AsyncSession,merchant_id:int,store:Models.Store)->Any:
        datas=await self.getProductList(db,store)
        for data in datas:
            sku=data["parent_sku"]
            variant=await Service.variantService.findOne(db,{"sku":sku,'merchant_id':merchant_id})
            if variant: #db has a variant same sku
                variantstore=await Service.variantstoreService.findOne(db,{'merchant_id':merchant_id,'variant_id':variant.variant_id})
                if variantstore:#has in variant_store table
                    pass
                else:
                    variantstore=Models.VariantStore(variant_id=variant.variant_id,store_name='wish',price='0',
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


    # async def test():  # type: ignore
    #     wishService = WishService()
    #     async with getdbsession() as db:
    #         store = await Service.storeService.findByPk(db, 1)
    #         await Service.wishService.getProductList(db, store)
    #     # await wishService.getCurrencyList()
    #     # await wishService.getBrandList()
    #     # await wishService.getOrders()
    #
    #
    # asyncio.run(test())
