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

# <editor-fold desc="syncProduct get: /merchant/syncProduct/{store_id}">
@router.get(
    "/merchant/syncProduct/{store_id}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def syncProduct(
    store_id: int,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    onlineproduct
    """
    await Service.thirdmarketService.syncProduct(
        db, token.merchant_id, store_id
    )

    return {'status':'success'}


# </editor-fold>





# <editor-fold desc="onlineproductdetail get: /merchant/onlineproductdetail/{store_id}/product_id">
@router.get(
    "/merchant/onlineproductdetail/{store_id}/{product_id}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def wishonlineproductdetail(
    store_id:int,
    product_id: str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    wishonlineproductdetail
    """
    data=await Service.thirdmarketService.getStoreOnlineProductDetail(
        db, token.merchant_id, store_id,product_id
    )

    return {'status':'success','data':data}


# </editor-fold>
