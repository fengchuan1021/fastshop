# generated timestamp: 2022-10-29T02:15:04+00:00

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import settings
from component.dbsession import get_webdbsession
from common.globalFunctions import get_token
from common import XTJsonResponse

from .__init__ import dependencies
from .FulfillmentShema import (
    ApiFulfillmentDeliveryPostRequest,
    ApiFulfillmentDeliveryPostResponse,
    ApiFulfillmentDetailGetRequest,
    ApiFulfillmentDetailGetResponse,
    ApiFulfillmentOrderSplitConfirmPostRequest,
    ApiFulfillmentOrderSplitConfirmPostResponse,
    ApiFulfillmentOrderSplitVerifyPostRequest,
    ApiFulfillmentOrderSplitVerifyPostResponse,
    ApiFulfillmentPackagePickupConfigListGetRequest,
    ApiFulfillmentPackagePickupConfigListGetResponse,
    ApiFulfillmentPackageRemovePostRequest,
    ApiFulfillmentPackageRemovePostResponse,
    ApiFulfillmentPreCombinePkgConfirmPostRequest,
    ApiFulfillmentPreCombinePkgConfirmPostResponse,
    ApiFulfillmentPreCombinePkgListGetRequest,
    ApiFulfillmentPreCombinePkgListGetResponse,
    ApiFulfillmentRtsPostRequest,
    ApiFulfillmentRtsPostResponse,
    ApiFulfillmentSearchPostRequest,
    ApiFulfillmentSearchPostResponse,
    ApiFulfillmentShippingDocumentGetRequest,
    ApiFulfillmentShippingDocumentGetResponse,
    ApiFulfillmentShippingInfoGetRequest,
    ApiFulfillmentShippingInfoGetResponse,
    ApiFulfillmentShippingInfoUpdatePostRequest,
    ApiFulfillmentShippingInfoUpdatePostResponse,
    ApiFulfillmentUploadfilePostRequest,
    ApiFulfillmentUploadfilePostResponse,
    ApiFulfillmentUploadimagePostRequest,
    ApiFulfillmentUploadimagePostResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="ShipPackage post: /api/fulfillment/rts">
@router.post(
    '/api/fulfillment/rts',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentRtsPostResponse,
    
)
async def ShipPackage(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentRtsPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    ShipPackage
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentRtsPostResponse()


# </editor-fold>


# <editor-fold desc="SearchPreCombinePkg get: /api/fulfillment/pre_combine_pkg/list">
@router.get(
    '/api/fulfillment/pre_combine_pkg/list',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentPreCombinePkgListGetResponse,
    
)
async def SearchPreCombinePkg(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentPreCombinePkgListGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    SearchPreCombinePkg
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentPreCombinePkgListGetResponse()


# </editor-fold>


# <editor-fold desc="ConfirmOrderSplit post: /api/fulfillment/order_split/confirm">
@router.post(
    '/api/fulfillment/order_split/confirm',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentOrderSplitConfirmPostResponse,
    
)
async def ConfirmOrderSplit(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentOrderSplitConfirmPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    ConfirmOrderSplit
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentOrderSplitConfirmPostResponse()


# </editor-fold>


# <editor-fold desc="GetPackagePickupConfig get: /api/fulfillment/package_pickup_config/list">
@router.get(
    '/api/fulfillment/package_pickup_config/list',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentPackagePickupConfigListGetResponse,
    
)
async def GetPackagePickupConfig(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentPackagePickupConfigListGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetPackagePickupConfig
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentPackagePickupConfigListGetResponse()


# </editor-fold>


# <editor-fold desc="RemovePackageOrder post: /api/fulfillment/package/remove">
@router.post(
    '/api/fulfillment/package/remove',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentPackageRemovePostResponse,
    
)
async def RemovePackageOrder(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentPackageRemovePostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    RemovePackageOrder
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentPackageRemovePostResponse()


# </editor-fold>


# <editor-fold desc="GetPackageShippingInfo get: /api/fulfillment/shipping_info">
@router.get(
    '/api/fulfillment/shipping_info',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentShippingInfoGetResponse,
    
)
async def GetPackageShippingInfo(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentShippingInfoGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetPackageShippingInfo
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentShippingInfoGetResponse()


# </editor-fold>


# <editor-fold desc="VerifyOrderSplit post: /api/fulfillment/order_split/verify">
@router.post(
    '/api/fulfillment/order_split/verify',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentOrderSplitVerifyPostResponse,
    
)
async def VerifyOrderSplit(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentOrderSplitVerifyPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    VerifyOrderSplit
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentOrderSplitVerifyPostResponse()


# </editor-fold>


# <editor-fold desc="UpdatePackageShippingInfo post: /api/fulfillment/shipping_info/update">
@router.post(
    '/api/fulfillment/shipping_info/update',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentShippingInfoUpdatePostResponse,
    
)
async def UpdatePackageShippingInfo(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    body: ApiFulfillmentShippingInfoUpdatePostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    UpdatePackageShippingInfo
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentShippingInfoUpdatePostResponse()


# </editor-fold>


# <editor-fold desc="FulfillmentUploadFile post: /api/fulfillment/uploadfile">
@router.post(
    '/api/fulfillment/uploadfile',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentUploadfilePostResponse,
    
)
async def FulfillmentUploadFile(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    body: ApiFulfillmentUploadfilePostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    FulfillmentUploadFile
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentUploadfilePostResponse()


# </editor-fold>


# <editor-fold desc="UpdatePackageDeliveryStatus post: /api/fulfillment/delivery">
@router.post(
    '/api/fulfillment/delivery',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentDeliveryPostResponse,
    
)
async def UpdatePackageDeliveryStatus(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentDeliveryPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    UpdatePackageDeliveryStatus
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentDeliveryPostResponse()


# </editor-fold>


# <editor-fold desc="FulfillmentUploadImage post: /api/fulfillment/uploadimage">
@router.post(
    '/api/fulfillment/uploadimage',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentUploadimagePostResponse,
    
)
async def FulfillmentUploadImage(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentUploadimagePostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    FulfillmentUploadImage
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentUploadimagePostResponse()


# </editor-fold>


# <editor-fold desc="GetPackageShippingDocument get: /api/fulfillment/shipping_document">
@router.get(
    '/api/fulfillment/shipping_document',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentShippingDocumentGetResponse,
    
)
async def GetPackageShippingDocument(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentShippingDocumentGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetPackageShippingDocument
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentShippingDocumentGetResponse()


# </editor-fold>


# <editor-fold desc="GetPackageDetail get: /api/fulfillment/detail">
@router.get(
    '/api/fulfillment/detail',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentDetailGetResponse,
    
)
async def GetPackageDetail(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentDetailGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetPackageDetail
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentDetailGetResponse()


# </editor-fold>


# <editor-fold desc="ConfirmPrecombinePackage post: /api/fulfillment/pre_combine_pkg/confirm">
@router.post(
    '/api/fulfillment/pre_combine_pkg/confirm',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentPreCombinePkgConfirmPostResponse,
    
)
async def ConfirmPrecombinePackage(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentPreCombinePkgConfirmPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    ConfirmPrecombinePackage
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentPreCombinePkgConfirmPostResponse()


# </editor-fold>


# <editor-fold desc="SearchPackage post: /api/fulfillment/search">
@router.post(
    '/api/fulfillment/search',
    response_class=XTJsonResponse,
    response_model=ApiFulfillmentSearchPostResponse,
    
)
async def SearchPackage(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFulfillmentSearchPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    SearchPackage
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFulfillmentSearchPostResponse()


# </editor-fold>
