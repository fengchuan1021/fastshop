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
from .SellerShema import (
    ApiSellerGlobalActiveShopsGetResponse,
    ApiSellerManageGlobalProductCheckGetResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="CheckGlobalProductMode get: /api/seller/manage_global_product/check">
@router.get(
    '/api/seller/manage_global_product/check',
    response_class=XTJsonResponse,
    response_model=ApiSellerManageGlobalProductCheckGetResponse,
    
)
async def CheckGlobalProductMode(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    CheckGlobalProductMode
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiSellerManageGlobalProductCheckGetResponse()


# </editor-fold>


# <editor-fold desc="GetActiveShopList get: /api/seller/global/active_shops">
@router.get(
    '/api/seller/global/active_shops',
    response_class=XTJsonResponse,
    response_model=ApiSellerGlobalActiveShopsGetResponse,
    
)
async def GetActiveShopList(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetActiveShopList
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiSellerGlobalActiveShopsGetResponse()


# </editor-fold>
