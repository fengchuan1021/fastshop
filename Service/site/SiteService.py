from sqlalchemy import select

from Service.base import CRUDBase
import Models
from typing import Union,Optional
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_

from XTTOOLS import cache


class SiteService(CRUDBase[Models.Site]):
    @cache
    async def findByDomainname(self,db:AsyncSession,domainname:str)->Models.Site:#type: ignore
        statment=select(Models.Site).where(Models.Site.domainname==domainname)
        return (await db.execute(statment)).scalar_one_or_none()#type: ignore