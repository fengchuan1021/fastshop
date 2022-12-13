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
from Models import Order
import Service
import settings
import aiohttp
from urllib.parse import urlencode
from Service.thirdpartmarket import Market
from common.CommonError import ResponseException, TokenException
from component.fastQL import fastQuery
class AmazonService(Market):
    async def get(self,url:str,params:Dict,store:Models.Store)->Any:
        async with aiohttp.ClientSession() as sesssion:
            async with sesssion.get(url) as resp:
                return resp.json()
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
