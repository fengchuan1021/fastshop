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
from .WarehouseShema import (

    BackendShopWarehouselistPostResponse, BackendShopAddwarehousePostResponse, BackendShopAddwarehousePostRequest,
    BackendShopDelwarehouseDeleteResponse, BackendShopDelwarehouseDeleteRequest, BackendShopEditwarehousePostResponse,
    BackendShopEditwarehousePostRequest,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="warehouselist post: /backend/shop/warehouselist">
@router.post(
    '/backend/shop/warehouselist',
    response_class=XTJsonResponse,
    response_model=BackendShopWarehouselistPostResponse,
)
async def warehouselist(

    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    warehouselist
    """
    results=await Service.warehouseService.getList(db)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendShopWarehouselistPostResponse(status='success', msg='', data=results)


# </editor-fold>

# <editor-fold desc="addwarehouse post: /backend/shop/addwarehouse">
@router.post(
    '/backend/shop/addwarehouse',
    response_class=XTJsonResponse,
    response_model=BackendShopAddwarehousePostResponse,
)
async def addwarehouse(
    body: BackendShopAddwarehousePostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    addwarehouse
    """

    await Service.warehouseService.create(db,body)

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendShopAddwarehousePostResponse(status='success',msg='add warehouse success')


# </editor-fold>


# <editor-fold desc="delwarehouse delete: /backend/shop/delwarehouse">
@router.post(
    '/backend/shop/delwarehouse',
    response_class=XTJsonResponse,
    response_model=BackendShopDelwarehouseDeleteResponse,
)
async def delwarehouse(
    body: BackendShopDelwarehouseDeleteRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    delwarehouse
    """
    await Service.warehouseService.deleteByPk(db,body.warehouse_id)

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendShopDelwarehouseDeleteResponse(status='success')


# </editor-fold>

# <editor-fold desc="editwarehouse post: /backend/shop/editwarehouse">
@router.post(
    '/backend/shop/editwarehouse',
    response_class=XTJsonResponse,
    response_model=BackendShopEditwarehousePostResponse,
)
async def editwarehouse(
    body: BackendShopEditwarehousePostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    editwarehouse
    """
    await Service.warehouseService.updateByPk(db,body.warehouse_id,body)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendShopEditwarehousePostResponse(status='success')


# </editor-fold>
