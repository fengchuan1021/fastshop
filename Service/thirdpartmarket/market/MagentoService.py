import base64
import datetime
import os
import time
import random
from typing import Dict, List, TYPE_CHECKING, cast, Any, Literal
import orjson
import pytz
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
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

from common.CommonError import ResponseException, TokenException
from common.CurrencyRate import CurrencyRate
from component.fastQL import fastQuery
from modules.merchant.product.magento.ProductShema import MagentoProductShema


class MagentoService(Market):
    async def request(self,store:Store,method:Literal["GET","POST","PUT","DELETE"],url:str,params:Dict=None,body:Dict=None,headers:Dict=None)->Any:
        if not store.token_expiration or store.token_expiration-int(time.time())<300:
            await self.getAdminToken(store)
        url = f'{store.apiendpoint}{url}'
        async with aiohttp.request(method,url,params=params,json=body,headers=headers) as resp:
            return await resp.json()

    async def get(self,store:Store,url:str,params:Dict=None)->Any:
        return await self.request(store,"GET",url,params=params,headers={'Authorization':f'Bearer {store.token}','Content-Type':'application/json'})

    async def post(self,store:Store,url:str,body:Dict)->Any:
        return await self.request(store,"POST",url,body=body,headers={'Authorization':f'Bearer {store.token}','Content-Type':'application/json'})

    async def put(self,store:Store,url:str,body:Dict)->Any:
        return await self.request(store,"PUT",url,body=body,headers={'Authorization':f'Bearer {store.token}','Content-Type':'application/json'})
    async def delete(self,store:Store,url:str,body:Dict)->Any:
        return await self.request(store,"DELETE",url,body=body,headers={'Authorization':f'Bearer {store.token}','Content-Type':'application/json'})
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
    async def shiPackage(self,db:AsyncSession,store:Models.Store,shipinfo:Shipinfo,order:Models.Order,ordershipmentitems:List[Models.OrderShipmentItem])->Any:
        '''??????'''
        url=f'/rest/V1/order/{shipinfo.order_id}/ship'
        body={"tracks":[
            {
                "track_number":shipinfo.track_number,
                "carrier_code":shipinfo.shipping_provider,
                'title':shipinfo.shipping_provider
            }
        ]}
        ret=await self.post(store,url,body)
        return ret
    async def updateStock(self,db:AsyncSession,store:Models.Store,sku:str,num:int)->Any:
        product=await Service.magentoproductService.findOne(db,{'sku':sku,'store_id':store.store_id})
        if product:
            url=f'/rest/V1/products/{product.sku}/stockItems/1'
            body={"stockItem":{"qty":num, "is_in_stock": True}}
            ret=await self.put(store,url,body)
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
            ret=await self.get(store,url,{'searchCriteria[currentPage]':1,'searchCriteria[pageSize]':50,
                                    'searchCriteria[sortOrders][0][direction]':'desc',
                                    'searchCriteria[sortOrders][0][field]':'updated_at',
                                    })

            yield ret
            if not ret['items']:
                break
            else:
                update_at_max=ret['items'][-1]['updated_at']
                if datetime.datetime.fromtimestamp(update_at_max).timestamp()<=starttime:
                    break
    async def createProduct(self,db:AsyncSession,store:Models.Store,data:MagentoProductShema)->Any:
        url='/rest/V1/products'
        ret=await self.post(store,url,{"product":data.dict(exclude_unset=True)})
        print('ret:')
        print(ret)
        return ret
    async def getProductList(self,db:AsyncSession,store:Models.Store)->Any:
        url='/rest/V1/products'
        i=1
        while 1:
            ret=await self.get(store,url,{'storeId':store.shop_id,'currencyCode':store.currency_code,'searchCriteria[currentPage]':i,'searchCriteria[pageSize]':50})
            i+=1
            yield ret['items']
            if len(ret['items'])<50:
                break
    async def getCategories(self,db:AsyncSession,store:Store)->Any:
        url='/V1/categories'
        ret=await self.get(store,url)
        print(ret)
    async def updatePrice(self, db: AsyncSession, store: Models.Store, sku: str, price: float,
                          price_currency_code:str="GBP") -> Any:
        url=f'/rest/V1/products/{sku}'
        RATE = await CurrencyRate(price_currency_code, store.currency_code)
        body={
            'product':{
                   'sku':sku,
                    "price":round(price*RATE,2),
            }
        }
        ret=await self.put(store,url,body)
        print(f'{ret=}')
        return ret


    async def deleteProduct(self,db:AsyncSession,store:Models.Store,sku:str)->Any:
        url=f'/rest/V1/products/{sku}'
        body={'product':{'sku':sku}}
        await self.delete(store,url,body)
    async def offlineProduct(self,db:AsyncSession,store:Models.Store,sku:str)->Any:
        url = f'/rest/V1/products/{sku}'
        body = {'product': {'sku': sku,'status':2}}
        ret=await self.put(store, url, body)
        print(ret)
        return ret

    async def onlineProduct(self,db:AsyncSession,store:Models.Store,sku:str)->Any:
        url = f'/rest/V1/products/{sku}'
        body = {'product': {'sku': sku,'status':1}}
        ret=await self.put(store, url, body)
        print(ret)
        return ret

if __name__ == '__main__':
    from common import cmdlineApp
    @cmdlineApp
    async def test(db):#type: ignore
        store=await Service.storeService.findByPk(db,4)
        magento=MagentoService()
        ret=await magento.updatePrice(db, store, 'WSH12-32-Purple',66.66)
        #await magento.updateStock(db,store,'WSH12-32-Purple',999)
        #await Service.magentoService.getAdminToken(store)
        #await Service.magentoService.getProductList(db,store)

    test()

