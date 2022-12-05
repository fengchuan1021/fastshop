import abc
from typing import Tuple, Dict, List, Any

from sqlalchemy.ext.asyncio import AsyncSession
import Models

class Market:
    market_id:int
    market_name:str
    @abc.abstractmethod
    async def getProductList(self,db:AsyncSession,store:Models.Store)->List:
        raise NotImplementedError
    @abc.abstractmethod
    async def getProductDetail(self,db:AsyncSession,store:Models.Store,product_id:str)->Any:
        raise NotImplementedError
    @abc.abstractmethod
    async def deleteProduct(self,db:AsyncSession,enterprise_id:str,product_id:str)->List:
        raise NotImplementedError

    @abc.abstractmethod
    async def getOrderList(self,db:AsyncSession,store:Models.Store,starttime:int)->List:
        raise NotImplementedError

    # @abc.abstractmethod
    # async def getOrderDetail(self, db: AsyncSession, store:Models.Store, order_id: str,sem:Any)->Any:
    #     raise NotImplementedError