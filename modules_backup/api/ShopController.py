# generated timestamp: 2022-10-29T02:15:06+00:00

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import settings
from component.dbsession import get_webdbsession
from common.globalFunctions import get_token
from common import XTJsonResponse

from .__init__ import dependencies
from .ShopShema import ApiShopGetAuthorizedShopGetResponse

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="GetAuthorizedShop get: /api/shop/get_authorized_shop">
@router.get(
    '/api/shop/get_authorized_shop',
    response_class=XTJsonResponse,
    response_model=ApiShopGetAuthorizedShopGetResponse,
    
)
async def GetAuthorizedShop(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetAuthorizedShop
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiShopGetAuthorizedShopGetResponse()


# </editor-fold>
