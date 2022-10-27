import abc
from typing import Tuple,Dict

from sqlalchemy.ext.asyncio import AsyncSession


class PayMethod:

    @abc.abstractmethod
    async def getSession(self, db: AsyncSession,order_id:str) -> Dict:
        raise NotImplementedError

    @abc.abstractmethod
    async def refund(self, db: AsyncSession,order_id:str,money:float) -> Dict:
        raise NotImplementedError


