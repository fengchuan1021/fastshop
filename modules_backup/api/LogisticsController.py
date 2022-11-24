# generated timestamp: 2022-10-29T02:15:05+00:00

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import settings
from component.dbsession import get_webdbsession
from common.globalFunctions import get_token
from common import XTJsonResponse

from .__init__ import dependencies
from .LogisticsShema import (
    ApiLogisticsGetSubscribedDeliveryoptionsPostRequest,
    ApiLogisticsGetSubscribedDeliveryoptionsPostResponse,
    ApiLogisticsGetWarehouseListGetResponse,
    ApiLogisticsShipGetGetRequest,
    ApiLogisticsShipGetGetResponse,
    ApiLogisticsShippingDocumentGetRequest,
    ApiLogisticsShippingDocumentGetResponse,
    ApiLogisticsShippingProvidersGetResponse,
    ApiLogisticsTrackingPostRequest,
    ApiLogisticsTrackingPostResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="GetShippingDocument get: /api/logistics/shipping_document">
@router.get(
    '/api/logistics/shipping_document',
    response_class=XTJsonResponse,
    response_model=ApiLogisticsShippingDocumentGetResponse,
    
)
async def GetShippingDocument(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiLogisticsShippingDocumentGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetShippingDocument
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiLogisticsShippingDocumentGetResponse()


# </editor-fold>


# <editor-fold desc="GetSubscribedDeliveryOptions post: /api/logistics/get_subscribed_deliveryoptions">
@router.post(
    '/api/logistics/get_subscribed_deliveryoptions',
    response_class=XTJsonResponse,
    response_model=ApiLogisticsGetSubscribedDeliveryoptionsPostResponse,
    
)
async def GetSubscribedDeliveryOptions(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiLogisticsGetSubscribedDeliveryoptionsPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetSubscribedDeliveryOptions
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiLogisticsGetSubscribedDeliveryoptionsPostResponse()


# </editor-fold>


# <editor-fold desc="GetShippingInfo get: /api/logistics/ship/get">
@router.get(
    '/api/logistics/ship/get',
    response_class=XTJsonResponse,
    response_model=ApiLogisticsShipGetGetResponse,
    
)
async def GetShippingInfo(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiLogisticsShipGetGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetShippingInfo
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiLogisticsShipGetGetResponse()


# </editor-fold>


# <editor-fold desc="GetWarehouseList get: /api/logistics/get_warehouse_list">
@router.get(
    '/api/logistics/get_warehouse_list',
    response_class=XTJsonResponse,
    response_model=ApiLogisticsGetWarehouseListGetResponse,
    
)
async def GetWarehouseList(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetWarehouseList
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiLogisticsGetWarehouseListGetResponse()


# </editor-fold>


# <editor-fold desc="GetShippingProvider get: /api/logistics/shipping_providers">
@router.get(
    '/api/logistics/shipping_providers',
    response_class=XTJsonResponse,
    response_model=ApiLogisticsShippingProvidersGetResponse,
    
)
async def GetShippingProvider(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetShippingProvider
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiLogisticsShippingProvidersGetResponse()


# </editor-fold>


# <editor-fold desc="UpdateShippingInfo post: /api/logistics/tracking">
@router.post(
    '/api/logistics/tracking',
    response_class=XTJsonResponse,
    response_model=ApiLogisticsTrackingPostResponse,
    
)
async def UpdateShippingInfo(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiLogisticsTrackingPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    UpdateShippingInfo
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiLogisticsTrackingPostResponse()


# </editor-fold>
