
# generated timestamp: 2022-11-29T09:01:02+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common import CommonResponse, XTJsonResponse, get_token
from component.cache import cache
from component.dbsession import get_webdbsession
from component.fastQL import fastAdd, fastDel, fastQuery

from .__init__ import dependencies
#from .ProductShema import MerchantOnlineproductStoreIdGetResponse

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="onlineproduct get: /merchant/onlineorders/{store_id}">
@router.get(
    "/merchant/onlineorders/{store_id}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def onlineorders(
    store_id: int,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    onlineorders
    """
    data=await Service.thirdmarketService.getStoreOnlineOrders(
        db, token.merchant_id, store_id
    )

    return {'status':'success','data':data}


# </editor-fold>


# <editor-fold desc="asynchalfyearorder get: /merchant/asynchalfyearorder/{store_id}">
@router.get(
    "/merchant/syncorder/{store_id}/{nmonth}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def asynchalfyearorder(
    store_id: int,
    nmonth:int=1,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    onlineorders
    """
    data=await Service.thirdmarketService.syncOrder(
        db, token.merchant_id, store_id,nmonth
    )

    return {'status':'success','data':'success'}


# </editor-fold>