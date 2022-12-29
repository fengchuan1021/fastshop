import settings
import asyncio
import datetime,time
from typing import Generator, Any, List, Dict, TYPE_CHECKING, cast, Optional, Literal
import orjson
import pytz,os #type: ignore
from dateutil.parser import parse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request


from common.CurrencyRate import CurrencyRate
from component.fastQL import fastQuery
from modules.merchant.product.wish.ProductShema import WishCreateProduct
from sqlalchemy.orm import Load
#from sqlalchemy.orm.strategy_options import load_only
import math
import Models
import Service

import aiohttp

from Service.thirdpartmarket.Shema import Shipinfo
from common.CommonError import ResponseException, TokenException
from component.cache import cache
from Service.thirdpartmarket import Market

if __name__=='__main__':
    import wishutil
else:
    from . import wishutil


from component.snowFlakeId import snowFlack


class WishService(Market):
    async def request(self,store:Models.Store,method:Literal["GET","POST","PUT","DELETE"],url:str,params:Dict=None,body:Dict=None,headers:Dict=None)->Any:

        url = f'{settings.WISH_BASEURL}{url}'
        async with aiohttp.request(method,url,params=params,json=body,headers=headers) as resp:
            return resp.json()
    async def post(self,url:str,store:Models.Store,body:Dict=None,headers:Dict=None)->Any:
        tokenheader={'authorization': f'Bearer {store.token}'}
        if headers:
            tokenheader.update(headers)
        return await self.request(store,"POST",url,body=body,headers=tokenheader)

    async def put(self,url:str,store:Models.Store,body:Dict=None)->Any:
        tokenheader = {'authorization': f'Bearer {store.token}'}

        return await self.request(store, "PUT", url, body=body, headers=tokenheader)
    async def get(self,url: str, store:Models.Store, params: Dict = None) -> Any:
        return await self.request(store, "GET", url, params=params, headers={'authorization': f'Bearer {store.token}'})
    async def delete(self,url: str, store:Models.Store) -> Any:
        return await self.request(store, "DELETE", url,headers={'authorization': f'Bearer {store.token}'})

    def getAuthorizationUrl(self, shop_id: int) -> str:
        return settings.WISH_BASEURL + f"/v3/oauth/authorize?client_id={settings.WISH_CLIENTID}&state={shop_id}"

    def onAuthriaztionCallBack(self, request: Request) -> None:
        if shop_id := request.query_params.get('state', ''):
            pass
        else:
            pass
        # https://example.redirect.uri.com?code={authorization_code}
        pass
    async def refreshtoken(self,db:AsyncSession,store:Models.Store)->Any:
        url='/api/v3/oauth/refresh_token'
        params={"client_id": store.client_id, "client_secret": store.appsecret, "refresh_token": store.refreshtoken,
         "grant_type": "refresh_token"}
        async with aiohttp.ClientSession() as session:
            async with session.get(settings.WISH_BASEURL + url,params=params) as response:
                ret=await response.json()
                store.token=ret['data']['access_token']
                store.token_expiration=int(parse(ret['data']['expiry_time']).timestamp())
                store.refreshtoken=ret['data']['refresh_token']


    async def updateStock(self,db:AsyncSession,store:Models.Store,sku:str,num:int)->Any:
        variant=await Service.wishvariantService.findOne(db,{'sku':sku,'store_id':store.store_id})
        #variant=await fastQuery(db,'WishVariant{wish_id,WishProduct{wish_id}}')
        if variant:
            url=f'/api/v3/products/{variant.market_product_id}'
            body={"variations":[
                {
                    id:variant.market_variant_id,
                    "inventories":[
                        {"inventory":num,
                         "warehouse_id":variant.warehouse_id
                         }
                    ]
                }


            ]}
            ret=await self.put(url,store,body)
            return ret
    async def shiPackage(self,db:AsyncSession,store:Models.Store,shipinfo:Shipinfo,order:Models.Order,ordershipmentitems:List[Models.OrderShipmentItem])->Any:
        '''发货'''
        url=f'/api/v3/orders/{shipinfo.order_id}/tracking'
        body={'origin_country':shipinfo.origin_country,
              'shipping_provider':shipinfo.shipping_provider,
              'tracking_number':shipinfo.track_number,
              'ship_note':shipinfo.ship_note
              }
        ret=await self.put(url,store,body)
        return ret['data']

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





    async def createProduct(self,db:AsyncSession,store:Models.Store,body:WishCreateProduct):  # type: ignore
        url = '/api/v3/products'
        ret=await self.post(url,store,body.dict(exclude_unset=True))
        return ret

    async def getOrderDetail(self, db: AsyncSession, store:Models.Store,market_order_id:str,sem:Any=None) -> Any:
        url = f'/api/v3/orders/{market_order_id}'
        data=await self.get(url,store)
        return data
        # async with self.session.get(url) as resp:
        #     ret = await resp.json()
        #     return ret
    async def getOrderList(self,db:AsyncSession,store:Models.Store,starttime:int)->Any:
        url='/api/v3/orders'
        update_at_max=None
        params={'limit':500}
        while 1:
            if update_at_max:
                params['updated_at_max']=update_at_max
        #endstr=str(datetime.datetime.fromtimestamp(endtime, tz=datetime.timezone.utc))
        #endstr=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(starttime))
            #print('endstr',endstr)
            ret=await self.get(url,store,params)
            if ret['data']:
                update_at_max=ret['data'][-1]["updated_at"]
            else:
                break
            yield ret['data']
            if datetime.datetime.fromisoformat(update_at_max).timestamp()<=starttime:
                break
    async def syncOrder(self,db:AsyncSession,merchant_id:int,store:Models.Store,starttime:int)->Any:
        async for remoteOrders in self.getOrderList(db,store,starttime):
            #for remoteOrder in remoteOrders:
            needsync = {remoteOrder["id"]:remoteOrder for remoteOrder in remoteOrders}
            needupdate={}
            ourdbmodels=await Service.orderService.find(db,{"market_order_id__in":needsync.keys()},Load(Models.Order).load_only(Models.Order.market_order_id,Models.Order.market_updatetime))
            for model in ourdbmodels:
                if os.name=='nt':#for timezone bug in windows
                    if isinstance(model.market_updatetime,str):
                        tmstamp=parse(model.market_updatetime).replace(tzinfo=pytz.UTC).timestamp()
                    else:
                        tmstamp=model.market_updatetime.replace(tzinfo=pytz.UTC).timestamp()#type: ignore
                else:
                    tmstamp=model.market_updatetime.timestamp() if not isinstance(model.market_updatetime,str) else parse(model.market_updatetime).timestamp()#type: ignore
                if tmstamp!=parse(needsync[model.market_order_id]["updated_at"]).timestamp():
                    needupdate[model.order_id]=needsync[model.market_order_id] #wisshproduct_id 我们数据库主键 wish_id wish数据库主键
                del needsync[model.market_order_id]
            #sem = asyncio.Semaphore(100)#100并发量 wish有速度限制
            #new_task=[self.getOrderDetail(db,store,market_order_id,sem) for market_order_id in needsync]#:#add new product

            #result=await asyncio.gather(*new_task)
            try:
                await wishutil.addOrders(db,needsync.values(),store,merchant_id)
            except TokenException as e:
                await db.rollback()
                store.status=0
                store.status_msg='token expired'


            for ourdbid,market_order in needupdate.items():
                print('needupdate',market_order)

    async def getProductList(self, db: AsyncSession, store: Models.Store) ->Any:
        url = '/api/v3/products'
        LIMIT=500
        updated_at_max=None
        params={'limit': LIMIT}
        while 1:
            if updated_at_max:
                params['updated_at_max']=updated_at_max
            result = await self.get(url, store,params )
            print('productlist:',result)
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
            ourdbmodels=await Service.wishproductService.find(db,{"market_product_id__in":needsync.keys()},Load(Models.WishProduct).load_only(Models.WishProduct.market_product_id,Models.WishProduct.market_updatetime))
            for model in ourdbmodels:
                if os.name=='nt':#for timezone bug in windows
                    if isinstance(model.market_updatetime,str):
                        tmstamp=parse(model.market_updatetime).replace(tzinfo=pytz.UTC).timestamp()
                    else:
                        tmstamp=model.market_updatetime.replace(tzinfo=pytz.UTC).timestamp()#type: ignore
                else:
                    tmstamp=model.market_updatetime.timestamp() if not isinstance(model.market_updatetime,str) else parse(model.market_updatetime).timestamp()#type: ignore
                if tmstamp!=parse(needsync[model.market_product_id]).timestamp():
                    needupdate[model.wishproduct_id]=model.market_product_id #wisshproduct_id 我们数据库主键 wish_id wish数据库主键
                del needsync[model.market_product_id]
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
    async def getTickets(self,db:AsyncSession,store:Models.Store)->Any:
        url='/api/v3/tickets'
        ret=await self.get(url,store,{})
        return ret['data']
    async def getTicketDetail(self,db:AsyncSession,store:Models.Store,ticket_id:str)->Any:
        url=f'/api/v3/tickets/{ticket_id}'
        ret=await self.get(url,store,{})
        return ret['data']
    async def closeTicket(self,db:AsyncSession,store:Models.Store,ticket_id:str)->Any:
        url=f'/api/v3/tickets/{ticket_id}'
        print("????")
        ret=await self.put(url,store,{"state": "CLOSED"})
        return ret['data']
    async def replyTicket(self,db:AsyncSession,store:Models.Store,ticket_id:str,content:str)->Any:
        url=f'/api/v3/tickets/{ticket_id}/replies'

        ret=await self.post(url,store,{"message": content})
        if ret['code']!=0:
            raise ResponseException({'status':'failed','msg':ret['message']})
        return ret['data']


    async def deleteProduct(self,db:AsyncSession,store:Models.Store,sku:str)->Any:
        variant = await Service.wishvariantService.findOne(db, {'sku': sku, 'store_id': store.store_id})
        if variant:
            url=f'/api/v3/products/{variant.market_product_id}'
            await self.delete(url,store)

    async def setVariantStatus(self,db:AsyncSession,store:Models.Store,sku:str,status:Literal["ENABLED","DISABLED"])->Any:
        variant = await Service.wishvariantService.findOne(db, {'sku': sku, 'store_id': store.store_id})
        # variant=await fastQuery(db,'WishVariant{wish_id,WishProduct{wish_id}}')
        if variant:
            url = f'/api/v3/products/{variant.market_product_id}'
            body = {"variations": [
                {
                    id: variant.market_variant_id,
                    "status": status
                }

            ]}
            ret = await self.put(url, store, body)
            return ret
    async def offlineProduct(self,db:AsyncSession,store:Models.Store,sku:str)->Any:
        return await self.setVariantStatus(db,store,sku,"DISABLED")

    async def onlineProduct(self,db:AsyncSession,store:Models.Store,sku:str)->Any:
        return await self.setVariantStatus(db,store,sku,"ENABLED")

    async def updatePrice(self, db: AsyncSession, store: Models.Store, sku: str, price: float,price_currency_code:str="GBP") -> Any:
        variant = await Service.wishvariantService.findOne(db, {'sku': sku, 'store_id': store.store_id})
        RATE = await CurrencyRate(price_currency_code,"USD")
        if variant:
            url = f'/api/v3/products/{variant.market_product_id}'
            body = {"variations": [
                {
                    id: variant.market_variant_id,
                    "price": {"amount":round(price*RATE,2),"currency_code":"USD"}
                }

            ]}
            ret = await self.put(url, store, body)
            return ret
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

    async def test()->Any:
        wishService = WishService()
        async with getdbsession() as db:
            store = await Service.storeService.findByPk(db, 1)
            await Service.wishService.syncOrder(db,1,store,int(time.time())-3600*24*31)
            #await Service.wishService.backgroundsyncProduct(db, store)
        # await wishService.getCurrencyList()
        # await wishService.getBrandList()
        # await wishService.getOrders()


    asyncio.run(test())
