# generated timestamp: 2022-10-06T14:58:24+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from component.cache import cache
from component.xtjsonresponse import XTJsonResponse

from .__init__ import dependencies
from .ShopShema import (
    BackendShopAddshopPostRequest,
    BackendShopAddshopPostResponse,
    BackendShopShoplistPostRequest,
    BackendShopShoplistPostResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="addshop post: /backend/shop/addshop">
@router.post(
    '/backend/shop/addshop',
    response_class=XTJsonResponse,
    response_model=BackendShopAddshopPostResponse,
)
async def addshop(
    body: BackendShopAddshopPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    addshop
    """
    await Service.shopService.create(db,body)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendShopAddshopPostResponse(status='success',msg='add shop success')


# </editor-fold>


# <editor-fold desc="shoplist post: /backend/shop/shoplist">
@router.post(
    '/backend/shop/shoplist',
    response_class=XTJsonResponse,
    response_model=BackendShopShoplistPostResponse,
)
async def shoplist(
    body: BackendShopShoplistPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    shoplist
    """
    results=await Service.shopService.getList(db)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendShopShoplistPostResponse(status='success', msg='', data=results)


# </editor-fold>



