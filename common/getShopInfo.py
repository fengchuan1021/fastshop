from fastapi import Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import Models
from common.dbsession import get_webdbsession
import Service

async def getshopfinfo(request:Request,db: AsyncSession = Depends(get_webdbsession))->Models.Shop:#type: ignore
    domainname=request.headers.get('host')

    shop=await Service.shopService.findByDomainname(db,domainname)
    return shop