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
from .ReverseShema import (
    ApiReverseOrderCancelPostRequest,
    ApiReverseOrderCancelPostResponse,
    ApiReverseReverseOrderListPostRequest,
    ApiReverseReverseOrderListPostResponse,
    ApiReverseReverseReasonListGetRequest,
    ApiReverseReverseReasonListGetResponse,
    ApiReverseReverseRequestConfirmPostRequest,
    ApiReverseReverseRequestConfirmPostResponse,
    ApiReverseReverseRequestRejectPostRequest,
    ApiReverseReverseRequestRejectPostResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="ConfirmReverseRequest post: /api/reverse/reverse_request/confirm">
@router.post(
    '/api/reverse/reverse_request/confirm',
    response_class=XTJsonResponse,
    response_model=ApiReverseReverseRequestConfirmPostResponse,
    
)
async def ConfirmReverseRequest(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiReverseReverseRequestConfirmPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    ConfirmReverseRequest
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiReverseReverseRequestConfirmPostResponse()


# </editor-fold>


# <editor-fold desc="GetReverseOrderList post: /api/reverse/reverse_order/list">
@router.post(
    '/api/reverse/reverse_order/list',
    response_class=XTJsonResponse,
    response_model=ApiReverseReverseOrderListPostResponse,
    
)
async def GetReverseOrderList(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiReverseReverseOrderListPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetReverseOrderList
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiReverseReverseOrderListPostResponse()


# </editor-fold>


# <editor-fold desc="CancelOrder post: /api/reverse/order/cancel">
@router.post(
    '/api/reverse/order/cancel',
    response_class=XTJsonResponse,
    response_model=ApiReverseOrderCancelPostResponse,
    
)
async def CancelOrder(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiReverseOrderCancelPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    CancelOrder
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiReverseOrderCancelPostResponse()


# </editor-fold>


# <editor-fold desc="GetRejectReasonList get: /api/reverse/reverse_reason/list">
@router.get(
    '/api/reverse/reverse_reason/list',
    response_class=XTJsonResponse,
    response_model=ApiReverseReverseReasonListGetResponse,
    
)
async def GetRejectReasonList(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    body: ApiReverseReverseReasonListGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetRejectReasonList
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiReverseReverseReasonListGetResponse()


# </editor-fold>


# <editor-fold desc="RejectReverseRequest post: /api/reverse/reverse_request/reject">
@router.post(
    '/api/reverse/reverse_request/reject',
    response_class=XTJsonResponse,
    response_model=ApiReverseReverseRequestRejectPostResponse,
    
)
async def RejectReverseRequest(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiReverseReverseRequestRejectPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    RejectReverseRequest
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiReverseReverseRequestRejectPostResponse()


# </editor-fold>
