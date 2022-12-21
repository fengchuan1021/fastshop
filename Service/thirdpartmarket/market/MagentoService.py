import os
import time
import random
from typing import Dict, List, TYPE_CHECKING, cast, Any
import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from hashlib import sha256
import hmac

from sqlalchemy.orm.strategy_options import load_only, Load

import Models
from Models import Order, Store
import Service
import settings
import aiohttp
from urllib.parse import urlencode
from Service.thirdpartmarket import Market
from common import cmdlineApp
from common.CommonError import ResponseException, TokenException
from component.fastQL import fastQuery
class MagentoService(Market):
    async def get(self,url:str,params:Dict,store:Store)->Any:
        url=f'{store.apiendpoint}{url}'
        if params:
            url=f'{url}?{urlencode(params)}'
        async with aiohttp.ClientSession(headers={'Authorization':f'Bearer {store.token}'}) as session:
            async with session.get(url) as resp:
                return await resp.json()
    async def getOrderList(self, db: AsyncSession, store: Models.Store, starttime: int = None) -> Any:
        url='/orders/v0/orders'
        cursor=None
        params={'MaxResultsPerPage':100}
        while 1:
            if cursor:
                params['NextToken']=cursor
            ret=await self.get(url,params,store)
            yield ret['list']#todo
            if 'NextToken' in ret and ret['NextToken']:
                cursor=ret['NextToken']
            else:
                break

    async def getProductList(self,db:AsyncSession,store:Models.Store)->Any:
        url='/V1/products-render-info'
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

        await Service.magentoService.getProductList(db,store)

    test()

