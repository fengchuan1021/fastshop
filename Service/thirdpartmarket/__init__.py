import abc
from typing import Tuple, Dict, List, Any

from sqlalchemy.ext.asyncio import AsyncSession


class Market:
    @abc.abstractmethod
    async def getProductList(self,db:AsyncSession,enterprise_id:str)->List:
        raise NotImplementedError
    @abc.abstractmethod
    async def deleteProduct(self,db:AsyncSession,enterprise_id:str,product_id:str)->List:
        raise NotImplementedError

    @abc.abstractmethod
    async def getOrderList(self,db:AsyncSession,enterprise_id:str)->List:
        raise NotImplementedError

    @abc.abstractmethod
    async def getOrderDetail(self,db:AsyncSession,enterprise_id:str,order_id:str)->Any:
        raise NotImplementedError