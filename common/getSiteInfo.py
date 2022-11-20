from fastapi import Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import Models
from component.dbsession import get_webdbsession
import Service

async def getSiteInfo(request:Request,db: AsyncSession = Depends(get_webdbsession))->Models.Site:#type: ignore
    domainname=request.headers.get('host')
    site=await Service.siteService.findByDomainname(db,domainname)
    return site