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
from XTTOOLS import XTJsonResponse


from .__init__ import dependencies
from .WarehouseShema import (

    BackendSiteWarehouselistPostResponse, BackendSiteAddwarehousePostResponse, BackendSiteAddwarehousePostRequest,
    BackendSiteDelwarehouseDeleteResponse, BackendSiteDelwarehouseDeleteRequest, BackendSiteEditwarehousePostResponse,
    BackendSiteEditwarehousePostRequest,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="warehouselist post: /backend/site/warehouselist">
@router.post(
    '/backend/site/warehouselist',
    response_class=XTJsonResponse,
    response_model=BackendSiteWarehouselistPostResponse,
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
    return BackendSiteWarehouselistPostResponse(status='success', msg='', data=results)


# </editor-fold>

# <editor-fold desc="addwarehouse post: /backend/site/addwarehouse">
@router.post(
    '/backend/site/addwarehouse',
    response_class=XTJsonResponse,
    response_model=BackendSiteAddwarehousePostResponse,
)
async def addwarehouse(
    body: BackendSiteAddwarehousePostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    addwarehouse
    """

    await Service.warehouseService.create(db,body)

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendSiteAddwarehousePostResponse(status='success',msg='add warehouse success')


# </editor-fold>


# <editor-fold desc="delwarehouse delete: /backend/site/delwarehouse">
@router.post(
    '/backend/site/delwarehouse',
    response_class=XTJsonResponse,
    response_model=BackendSiteDelwarehouseDeleteResponse,
)
async def delwarehouse(
    body: BackendSiteDelwarehouseDeleteRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    delwarehouse
    """
    await Service.warehouseService.deleteByPk(db,body.warehouse_id)

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendSiteDelwarehouseDeleteResponse(status='success')


# </editor-fold>

# <editor-fold desc="editwarehouse post: /backend/site/editwarehouse">
@router.post(
    '/backend/site/editwarehouse',
    response_class=XTJsonResponse,
    response_model=BackendSiteEditwarehousePostResponse,
)
async def editwarehouse(
    body: BackendSiteEditwarehousePostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    editwarehouse
    """
    await Service.warehouseService.updateByPk(db,body.warehouse_id,body)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendSiteEditwarehousePostResponse(status='success')


# </editor-fold>
