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
from .OrderShema import (
    ApiOrdersDetailQueryPostRequest,
    ApiOrdersDetailQueryPostResponse,
    ApiOrdersSearchPostRequest,
    ApiOrdersSearchPostResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="GetOrderDetail post: /api/orders/detail/query">
@router.post(
    '/api/orders/detail/query',
    response_class=XTJsonResponse,
    response_model=ApiOrdersDetailQueryPostResponse,
    
)
async def GetOrderDetail(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiOrdersDetailQueryPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetOrderDetail
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiOrdersDetailQueryPostResponse()


# </editor-fold>


# <editor-fold desc="GetOrderList post: /api/orders/search">
@router.post(
    '/api/orders/search',
    response_class=XTJsonResponse,
    response_model=ApiOrdersSearchPostResponse,
    
)
async def GetOrderList(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiOrdersSearchPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetOrderList
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiOrdersSearchPostResponse()


# </editor-fold>
