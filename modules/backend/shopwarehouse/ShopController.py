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
    BackendShopShoplistPostResponse, BackendShopDelshopDeleteRequest, BackendShopDelshopDeleteResponse,
    BackendShopEditshopPostResponse, BackendShopEditshopPostRequest,
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



# <editor-fold desc="delshop delete: /backend/shop/delshop">
@router.post(
    '/backend/shop/delshop',
    response_class=XTJsonResponse,
    response_model=BackendShopDelshopDeleteResponse,
)
async def delshop(
    body: BackendShopDelshopDeleteRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    delshop
    """
    await Service.shopService.deleteByPk(db,body.shop_id)

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendShopDelshopDeleteResponse(status='success')


# </editor-fold>

# <editor-fold desc="editshop post: /backend/shop/editshop">
@router.post(
    '/backend/shop/editshop',
    response_class=XTJsonResponse,
    response_model=BackendShopEditshopPostResponse,
)
async def editshop(
    body: BackendShopEditshopPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    editshop
    """
    await Service.shopService.updateByPk(db, body.shop_id, body)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendShopEditshopPostResponse(status='success')


# </editor-fold>
