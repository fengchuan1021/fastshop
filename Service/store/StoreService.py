from sqlalchemy import select

from Service.base import CRUDBase
import Models
from typing import Union,Optional
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_

from component.cache import cache


class StoreService(CRUDBase[Models.Store]):
    @cache
    async def findByDomainname(self,db:AsyncSession,domainname:str)->Models.Store:#type: ignore
        statment=select(Models.Store).where(Models.Store.domainname==domainname)
        return (await db.execute(statment)).scalar_one_or_none()#type: ignore