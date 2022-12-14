
# generated timestamp: 2022-11-29T09:01:02+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from Service.thirdpartmarket.Shema import Shipinfo
from common import CommonResponse, XTJsonResponse, get_token
from component.cache import cache
from component.dbsession import get_webdbsession
from component.fastQL import fastAdd, fastDel, fastQuery

from .__init__ import dependencies
#from .ProductShema import MerchantOnlineproductStoreIdGetResponse

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="onlineproduct">
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


# <editor-fold desc="asynchalfyearorder">
@router.get(
    "/merchant/syncorder/{store_id}/{ndays}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def asynchalfyearorder(
    store_id: int,
    ndays:int=1,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    onlineorders
    """
    data=await Service.thirdmarketService.syncOrder(
        db, token.merchant_id, store_id,ndays
    )

    return {'status':'success','data':'success'}


# </editor-fold>


# <editor-fold desc="onlineorderdetail">
@router.get(
    "/merchant/onlineorderdetail/{store_id}/{order_id}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def onlineorderdetail(
    store_id:int,
    order_id: str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    wishonlineproductdetail
    """
    data=await Service.thirdmarketService.getStoreOnlineOrderDetail(
        db, token.merchant_id, store_id,order_id
    )

    return {'status':'success','data':data}


# </editor-fold>


# <editor-fold desc="onlineorderdetail">
@router.get(
    "/merchant/onlinepackagedetail/{store_id}/{package_id}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def onlinepackagedeital(
    store_id:int,
    package_id: str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    wishonlineproductdetail
    """
    data=await Service.thirdmarketService.getStoreOnlinePackageDetail(
        db, token.merchant_id, store_id,package_id
    )

    return {'status':'success','data':data}


# </editor-fold>



# <editor-fold desc="shippackage">
@router.post(
    "/merchant/order/shippackage",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def shippackage(
    store_id:int,
    shipinfo:Shipinfo,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    wishonlineproductdetail
    """
    data=await Service.thirdmarketService.shiPackage(
        db, token.merchant_id, store_id,shipinfo
    )

    return {'status':'success','data':data}


# </editor-fold>



# <editor-fold desc="revieworderrules">
@router.get(
    "/merchant/order/revieworderrules",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def revieworderrules(
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    wishonlineproductdetail
    """
    data=await Service.revieworderService.getRules()

    return {'status':'success','data':data}


# </editor-fold>