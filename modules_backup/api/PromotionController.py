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
from .PromotionShema import (
    ApiPromotionActivityCreatePostRequest,
    ApiPromotionActivityCreatePostResponse,
    ApiPromotionActivityDeactivatePostRequest,
    ApiPromotionActivityDeactivatePostResponse,
    ApiPromotionActivityGetGetRequest,
    ApiPromotionActivityGetGetResponse,
    ApiPromotionActivityItemsAddorupdatePostRequest,
    ApiPromotionActivityItemsAddorupdatePostResponse,
    ApiPromotionActivityItemsRemovePostRequest,
    ApiPromotionActivityItemsRemovePostResponse,
    ApiPromotionActivityListPostRequest,
    ApiPromotionActivityListPostResponse,
    ApiPromotionActivityUpdatePostRequest,
    ApiPromotionActivityUpdatePostResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="AddPromotion post: /api/promotion/activity/create">
@router.post(
    '/api/promotion/activity/create',
    response_class=XTJsonResponse,
    response_model=ApiPromotionActivityCreatePostResponse,
    
)
async def AddPromotion(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    body: ApiPromotionActivityCreatePostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    AddPromotion
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiPromotionActivityCreatePostResponse()


# </editor-fold>


# <editor-fold desc="DeactivatePromotion post: /api/promotion/activity/deactivate">
@router.post(
    '/api/promotion/activity/deactivate',
    response_class=XTJsonResponse,
    response_model=ApiPromotionActivityDeactivatePostResponse,
    
)
async def DeactivatePromotion(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    body: ApiPromotionActivityDeactivatePostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    DeactivatePromotion
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiPromotionActivityDeactivatePostResponse()


# </editor-fold>


# <editor-fold desc="RemovePromotionItem post: /api/promotion/activity/items/remove">
@router.post(
    '/api/promotion/activity/items/remove',
    response_class=XTJsonResponse,
    response_model=ApiPromotionActivityItemsRemovePostResponse,
    
)
async def RemovePromotionItem(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    body: ApiPromotionActivityItemsRemovePostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    RemovePromotionItem
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiPromotionActivityItemsRemovePostResponse()


# </editor-fold>


# <editor-fold desc="GetPromotionDetails get: /api/promotion/activity/get">
@router.get(
    '/api/promotion/activity/get',
    response_class=XTJsonResponse,
    response_model=ApiPromotionActivityGetGetResponse,
    
)
async def GetPromotionDetails(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    body: ApiPromotionActivityGetGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetPromotionDetails
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiPromotionActivityGetGetResponse()


# </editor-fold>


# <editor-fold desc="AddUpdateDiscountItem post: /api/promotion/activity/items/addorupdate">
@router.post(
    '/api/promotion/activity/items/addorupdate',
    response_class=XTJsonResponse,
    response_model=ApiPromotionActivityItemsAddorupdatePostResponse,
    
)
async def AddUpdateDiscountItem(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    body: ApiPromotionActivityItemsAddorupdatePostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    AddUpdateDiscountItem
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiPromotionActivityItemsAddorupdatePostResponse()


# </editor-fold>


# <editor-fold desc="GetPromotionList post: /api/promotion/activity/list">
@router.post(
    '/api/promotion/activity/list',
    response_class=XTJsonResponse,
    response_model=ApiPromotionActivityListPostResponse,
    
)
async def GetPromotionList(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    body: ApiPromotionActivityListPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetPromotionList
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiPromotionActivityListPostResponse()


# </editor-fold>


# <editor-fold desc="UpdateBasicInformation post: /api/promotion/activity/update">
@router.post(
    '/api/promotion/activity/update',
    response_class=XTJsonResponse,
    response_model=ApiPromotionActivityUpdatePostResponse,
    
)
async def UpdateBasicInformation(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    body: ApiPromotionActivityUpdatePostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    UpdateBasicInformation
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiPromotionActivityUpdatePostResponse()


# </editor-fold>
