import abc
from typing import Tuple, Dict, List

from sqlalchemy.ext.asyncio import AsyncSession


class Market:
    @abc.abstractmethod
    async def getProductList(self,db:AsyncSession,enterprise_id:str)->List:
        raise NotImplementedError

    @abc.abstractmethod
    async def getOrderList(self,db:AsyncSession,enterprise_id:str)->List:
        raise NotImplementedError