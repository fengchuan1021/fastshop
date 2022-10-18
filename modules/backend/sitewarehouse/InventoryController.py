# generated timestamp: 2022-10-16T06:11:02+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from component.cache import cache
from component.xtjsonresponse import XTJsonResponse

from .__init__ import dependencies
from .InventoryShema import (

    BackendSitewarehouseGetproductsitestockdetailProductIdGetResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="getproductsitestockdetail get: /backend/sitewarehouse/getproductsitestockdetail/{product_id}">
@router.get(
    '/backend/sitewarehouse/getproductsitestockdetail/{product_id}',
    response_class=XTJsonResponse,
    response_model=BackendSitewarehouseGetproductsitestockdetailProductIdGetResponse,
)
async def getproductsitestockdetail(
    product_id: str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getproductsitestockdetail
    """
    data=await Service.variantSiteService.getproductsitestockdetail(db,product_id)
    print('dat:',data)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendSitewarehouseGetproductsitestockdetailProductIdGetResponse(status='success',data=data)


# </editor-fold>
