from sqlalchemy import select

from Service.base import CRUDBase
import Models
from typing import Union,Optional
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_

from component.cache import cache


class ShopService(CRUDBase[Models.Shop]):
    @cache
    async def findByDomainname(self,db:AsyncSession,domainname:str)->Models.Shop:
        statment=select(Models.Shop).where(Models.Shop.domainname==domainname)
        return (await db.execute(statment)).scalar_one()