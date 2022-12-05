import time
import random
from typing import Dict, List, TYPE_CHECKING, cast, Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from hashlib import sha256
import hmac

from sqlalchemy.orm.strategy_options import load_only, Load

import Models
from Models import Order
import Service
import settings
import aiohttp
from urllib.parse import urlencode
from Service.thirdpartmarket import Market
from common.CommonError import ResponseException
from component.fastQL import fastQuery


class TikTokService(Market):
    def __init__(self)->None:
        pass


    def get_sign(self,data:str, key:str)->str:
        sign = hmac.new(key.encode('utf-8'), data.encode('utf-8'), digestmod=sha256).hexdigest()
        return sign
    async def getSelfAuthrizeUrl(self,db:AsyncSession,store:Models.Store)->Any:
        return f'https://auth.tiktok-shops.com/oauth/authorize?app_key={store.appkey}&state={random.randint(100,999999)}'
    def buildurl(self,url:str,params:Dict,store:'Models.Store')->str:
        params.update({'app_key':store.appkey,'shop_id':store.shop_id})#type: ignore
        params['timestamp']=str(int(time.time()))#type: ignore
        signstring:str = store.appsecret + url#type: ignore
        for key in sorted(params):#type: ignore
            signstring = signstring + key + params[key]#type: ignore
        signstring = signstring + store.appsecret#type: ignore
        sign=self.get_sign(signstring,store.appsecret)#type: ignore
        params['access_token']=store.token#type: ignore
        params['sign']=sign#type: ignore
        return f'{url}?{urlencode(params)}'#type: ignore

    async def getAuthorizedStore(self,db:AsyncSession,store:Models.Store)->Any:
        url = "/api/store/get_authorized_store"
        return await self.get(url,{},store)

    async def getActiveStoreList(self,db:AsyncSession,store:Models.Store)->Any:
        url = "/api/seller/global/active_stores"
        return await self.get(url,{},store)


    async def createProduct(self,db:AsyncSession,store:Models.Store,product_id:str)->Any:
        url='/api/products'
        url = self.buildurl(url, {}, store)

        #data productdata
        data:Dict={}
        await self.post(url,{},data,store)
        # async with self.session.post(url,json=data) as resp:
        #     ret=await resp.json()

    async def deleteProduct(self,db:AsyncSession,store_id:str,product_id:str)->Any:
        url='/api/products'
        #await self.delete
        # merchantmodel = await self.getStore(db, store_id)
        #
        # url = self.buildurl(url, {"product_ids":[123,456]}, merchantmodel)
        #
        #
        # async with self.session.delete(url) as resp:
        #     ret=await resp.json()

    async def get(self,url:str,params:Dict,store:Models.Store)->Any:
        url=self.buildurl(url,params,store)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await  resp.json()
    async def post(self,url:str,params:Dict,body:Dict,store:Models.Store)->Any:
        if not params:
            params={}

        url=self.buildurl(url,params,store)

        async with aiohttp.ClientSession() as session:
            async with session.post(settings.TIKTOK_APIURL+url,json=body) as resp:

                return await resp.json()

    async def getProductList(self,db:AsyncSession,store:Models.Store)->List:#type ignore
        url = "/api/products/search"

        data=await self.post(url,{},{'page_number':1,'page_size':100},store)

        return data
    async def syncOrder(self,db:AsyncSession,store:Models.Store,starttime:int,endtime:int)->Any:
        #orderssummory=await self.getOrderList(db,store,starttime,endtime)


        async for ordersummory in self.getOrderList(db,store,starttime,endtime):#有分页限制一页最多50个
            needsync={order["order_id"]:order["update_time"] for order in ordersummory} #假设这些订单都需要同步
            #从数据库中查找 如果找到并且update_time 相同则不需要同步
            filter={'market_id':self.market_id,'market_order_number__in':[order["order_id"] for order in ordersummory]}
            ourdb_orders=await Service.orderService.find(db,filter,Load(Models.Order).load_only(Models.Order.market_order_number,Order.market_updatetime))
            for ourdborder in ourdb_orders:
                if ourdborder.market_updatetime==needsync[ourdborder.market_order_number]:
                    del needsync[ourdborder.market_order_number]

            orders=await self.getOrderDetail2(db,store,[titikorder_id for titikorder_id in needsync])
            arr:List[Any]=[]
            for tiktok_order in orders:
                order=Order()
                order.market_id=self.market_id
                order.market_name=self.market_name
                order.market_id=store.merchant_id
                order.merchant_name=''
                order.status="PENDING" #tode
                order.order_currency_code=tiktok_order['payment_info']['currentcy'].strip()
                order.market_order_number=tiktok_order['order_id']
                db.add(order)
                await db.commit()





            #await Service.orderService.find(db,{'market_order_number__in',[order["order_id"] for order in ordersummory],'market_id':})

    async def getOrderList(self,db:AsyncSession,store:Models.Store,starttime:int=None,endtime:int=None)->Any:
        url = "/api/orders/search"

        data:List[Any]=[]
        cursor=None
        body={'page_size':50,'create_time_from':starttime,'create_time_to':endtime}
        while 1:
            if cursor:
                body['cursor']=cursor
            ret=await self.post(url,{},body,store)
            if ret['code']==0:
                yield ret['data']["order_list"]
                cursor=ret['data']["next_cursor"]
                if not ret["data"]["more"]:
                    break
            else:
                raise Exception(f"tiktok error {ret['message']}")



    async def getOrderDetail2(self, db: AsyncSession, store:Models.Store,order_ids:List[str]) -> Any:
        url='/api/orders/detail/query'
        ret=await self.post(url,{},{},store)#order_ids

        if ret['code']!=0:
            raise ResponseException({'status':'failed','msg':ret['message']})
        return ret['data']["order_list"]

if __name__=='__main__':
    import asyncio

    from component.dbsession import getdbsession
    async def t()->None:
        async with getdbsession() as db:
            tiktok=TikTokService()#type: ignore

            await tiktok.getProductList(db,99071137052361794)#type: ignore
            await tiktok.getOrderList(db,99071137052361794)#type: ignore
            await tiktok.getAuthorizedStore(db,99071137052361794)#type: ignore
    asyncio.run(t())





