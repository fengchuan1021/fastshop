import base64
import datetime
import os
import time
import random
from typing import Dict, List, TYPE_CHECKING, cast, Any
import asyncio

import orjson
import pytz
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from hashlib import sha256
import hmac

from sqlalchemy.orm.strategy_options import load_only, Load
from dateutil.parser import parse
import Models
from Models import Order, Store
import Service
import settings
import aiohttp
from urllib.parse import urlencode
from Service.thirdpartmarket import Market
from Service.thirdpartmarket.Shema import Shipinfo
from Service.thirdpartmarket.market import magentoutil
from common import cmdlineApp
from common.CommonError import ResponseException, TokenException
from component.fastQL import fastQuery
from modules.merchant.product.magento.ProductShema import MagentoProductShema


class MagentoService(Market):
    async def get(self,url:str,params:Dict,store:Store)->Any:
        if not store.token_expiration or store.token_expiration-int(time.time())<300:
            await self.getAdminToken(store)
        url=f'{store.apiendpoint}{url}'
        if params:
            url=f'{url}?{urlencode(params)}'
        async with aiohttp.ClientSession(headers={'Authorization':f'Bearer {store.token}','Content-Type':'application/json'}) as session:
            async with session.get(url) as resp:
                return await resp.json()
    async def post(self,url:str,body:Dict,store:Store)->Any:
        if not store.token_expiration or store.token_expiration-int(time.time())<300:
            await self.getAdminToken(store)
        url=f'{store.apiendpoint}{url}'

        async with aiohttp.ClientSession(headers={'Authorization':f'Bearer {store.token}','Content-Type':'application/json'}) as session:
            async with session.post(url,json=body) as resp:
                return resp.json()
    async def put(self,url:str,body:Dict,store:Store)->Any:
        if not store.token_expiration or store.token_expiration-int(time.time())<300:
            await self.getAdminToken(store)
        url=f'{store.apiendpoint}{url}'
        async with aiohttp.ClientSession(headers={'Authorization':f'Bearer {store.token}','Content-Type':'application/json'}) as session:
            async with session.put(url,json=body) as resp:
                return resp.json()
    async def getAdminToken(self,store:Models.Store)->Any:
        url='/rest/V1/integration/admin/token'
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{store.apiendpoint}{url}',json={"username": store.appkey,"password": store.appsecret}) as resp:
                token=(await resp.text()).strip('"')
                payload = base64.b64decode(token.split('.')[1])
                expiration=orjson.loads(payload)["exp"]
                store.token_expiration=expiration
                store.token=token


    async def syncProduct(self,db:AsyncSession,store:Models.Store,merchant_id:int)->Any:
        async for products in self.getProductList(db,store):
            needsync = {product["id"]: product for product in products}
            needupdate={}
            ourdbmodls=await Service.magentoproductService.find(db,{"magento_id__in":needsync.keys()})
            for model in ourdbmodls:
                timestamp=model.market_updated_at.timestamp() if not isinstance(model.market_updatetime,str) else parse(model.market_updated_at).timestamp()#type: ignore
                if timestamp!=parse(needsync[model.magento_id]['updated_at']).timestamp():
                    needupdate[model.magentoproduct_id] = model.magento_id
                del needsync[model.magento_id]
            if needsync:
                await magentoutil.addproducts(db,needsync.values(),store.store_id,merchant_id)#type: ignore

            print('needupdate:',needupdate )
    async def shiPackage(self,db:AsyncSession,store:Models.Store,shipinfo:Shipinfo)->Any:
        '''发货'''
        url=f'/rest/V1/order/{shipinfo.order_id}/ship'
        body={"tracks":[
            {
                "track_number":shipinfo.track_number,
                "carrier_code":shipinfo.shipping_provider,
                'title':shipinfo.shipping_provider
            }
        ]}
        ret=await self.post(url,body,store)
        return ret
    async def updateStock(self,db:AsyncSession,store:Models.Store,sku:str,num:int)->Any:
        product=await Service.magentoproductService.findOne(db,{'sku':sku,'store_id':store.store_id})
        if product:
            url=f'/rest/V1/products/{product.sku}/stockItems/1'
            body={"stockItem":{"qty":num, "is_in_stock": True}}
            ret=await self.put(url,body,store)
            print(ret)
    async def getOrderList(self,db:AsyncSession,store:Models.Store,starttime:int)->Any:
        url='/rest/V1/orders'
        update_at_max=None
        params:Dict={}
        while 1:
            if update_at_max:
                params['searchCriteria[filterGroups][0][filters][0][field]']='updated_at'
                params['searchCriteria[filterGroups][0][filters][0][value]']=update_at_max
                params['searchCriteria[filterGroups][0][filters][0][conditionType]']='lt'
            ret=await self.get(url,{'searchCriteria[currentPage]':1,'searchCriteria[pageSize]':50,
                                    'searchCriteria[sortOrders][0][direction]':'desc',
                                    'searchCriteria[sortOrders][0][field]':'updated_at',
                                    },store)

            yield ret
            if not ret['items']:
                break
            else:
                update_at_max=ret['items'][-1]['updated_at']
                if datetime.datetime.fromtimestamp(update_at_max).timestamp()<=starttime:
                    break
    async def createProduct(self,db:AsyncSession,store:Models.Store,data:MagentoProductShema)->Any:
        url='/rest/V1/products'
        ret=await self.post(url,data.dict(exclude_unset=True),store)
        return ret
    async def getProductList(self,db:AsyncSession,store:Models.Store)->Any:
        url='/rest/V1/products'
        i=1
        while 1:
            ret=await self.get(url,{'storeId':store.shop_id,'currencyCode':store.currency_code,'searchCriteria[currentPage]':i,'searchCriteria[pageSize]':50},store)
            i+=1
            yield ret['items']
            if len(ret['items'])<50:
                break
    async def getCategories(self,db:AsyncSession,store:Store)->Any:
        url='/V1/categories'
        ret=await self.get(url,{},store)
        print(ret)
if __name__ == '__main__':
    @cmdlineApp
    async def test(db):#type: ignore
        store=await Service.storeService.findByPk(db,4)
        await Service.magentoService.getAdminToken(store)
        #await Service.magentoService.getProductList(db,store)

    test()

