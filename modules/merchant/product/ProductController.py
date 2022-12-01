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


# <editor-fold desc="onlineproduct get: /merchant/onlineproduct/{store_id}">
@router.get(
    "/merchant/onlineproducts/{store_id}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def onlineproduct(
    store_id: int,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    onlineproduct
    """
    data=await Service.thirdmarketService.getStoreOnlineProducts(
        db, token.merchant_id, store_id
    )

    return {'status':'success','data':data}


# </editor-fold>


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
