# generated timestamp: 2022-10-14T14:37:29+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from XTTOOLS import cache
from XTTOOLS import XTJsonResponse

from .__init__ import dependencies
from .BrandShema import (
    BackendProductAddbrandPostRequest,
    BackendProductAddbrandPostResponse,
    BackendProductBrandlistPostRequest,
    BackendProductBrandlistPostResponse,
    BackendProductDelbrandBrandIdPostResponse,
    BackendProductUpdatebrandPostRequest,
    BackendProductUpdatebrandPostResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="updatebrand post: /backend/product/updatebrand">
@router.post(
    '/backend/product/updatebrand',
    response_class=XTJsonResponse,
    response_model=BackendProductUpdatebrandPostResponse,
)
async def updatebrand(
    body: BackendProductUpdatebrandPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    updatebrand
    """

    await Service.brandService.updateByPk(db,body.brand_id,body)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductUpdatebrandPostResponse(status='success',msg='update brand successfully')


# </editor-fold>


# <editor-fold desc="getbrandlist post: /backend/product/brandlist">
@router.post(
    '/backend/product/brandlist',
    response_class=XTJsonResponse,
    response_model=BackendProductBrandlistPostResponse,
)
async def getbrandlist(
    body: BackendProductBrandlistPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getbrandlist
    """
    results,total=await Service.brandService.pagination(db,calcTotalNum=True,**body.dict())
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductBrandlistPostResponse(status='success',data=results,total=total,curpage=body.pagenum)


# </editor-fold>


# <editor-fold desc="delbrand post: /backend/product/delbrand/{brand_id}">
@router.post(
    '/backend/product/delbrand/{brand_id}',
    response_class=XTJsonResponse,
    response_model=BackendProductDelbrandBrandIdPostResponse,
)
async def delbrand(
    brand_id: str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    delbrand
    """
    await Service.brandService.deleteByPk(db,brand_id)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductDelbrandBrandIdPostResponse(status='success')


# </editor-fold>


# <editor-fold desc="addbrand post: /backend/product/addbrand">
@router.post(
    '/backend/product/addbrand',
    response_class=XTJsonResponse,
    response_model=BackendProductAddbrandPostResponse,
)
async def addbrand(
    body: BackendProductAddbrandPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    addbrand
    """
    await Service.brandService.create(db,body)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductAddbrandPostResponse(status='success')


# </editor-fold>
