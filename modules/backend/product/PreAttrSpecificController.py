# generated timestamp: 2022-10-09T07:45:48+00:00

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
from .PreAttrSpecificShema import (
    BackendProductAddpreattrspecificPostRequest,
    BackendProductAddpreattrspecificPostResponse,
    BackendProductDelpreattrspecificPreattrspecificIdPostResponse,
    BackendProductPreattrspecificPostRequest,
    BackendProductPreattrspecificPostResponse,
    BackendProductUpdatepreattrspecificPostRequest,
    BackendProductUpdatepreattrspecificPostResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="delpreattrspecific post: /backend/product/delpreattrspecific/{preattrspecific_id}">
@router.post(
    '/backend/product/delpreattrspecific/{preattrspecific_id}',
    response_class=XTJsonResponse,
    response_model=BackendProductDelpreattrspecificPreattrspecificIdPostResponse,
)
async def delpreattrspecific(
    preattrspecific_id: str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    delpreattrspecific
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductDelpreattrspecificPreattrspecificIdPostResponse(status='success')


# </editor-fold>


# <editor-fold desc="getpreattrspecificlist post: /backend/product/preattrspecific">
@router.post(
    '/backend/product/preattrspecific',
    response_class=XTJsonResponse,
    response_model=BackendProductPreattrspecificPostResponse,
)
async def getpreattrspecificlist(
    body: BackendProductPreattrspecificPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getpreattrspecificlist
    """
    results,total=await Service.preAttrSpecificationService.pagination(db,**body.dict(),calcTotalNum=True)
    # install pydantic plugin,press alt+enter auto complete the args.

    return BackendProductPreattrspecificPostResponse(status='success', msg='', total=total, curpage=body.pagenum, data=results)


# </editor-fold>


# <editor-fold desc="updatepreattrspecific post: /backend/product/updatepreattrspecific">
@router.post(
    '/backend/product/updatepreattrspecific',
    response_class=XTJsonResponse,
    response_model=BackendProductUpdatepreattrspecificPostResponse,
)
async def updatepreattrspecific(
    body: BackendProductUpdatepreattrspecificPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    updatepreattrspecific
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductUpdatepreattrspecificPostResponse(status='success')


# </editor-fold>


# <editor-fold desc="addpreattrspecific post: /backend/product/addpreattrspecific">
@router.post(
    '/backend/product/addpreattrspecific',
    response_class=XTJsonResponse,
    response_model=BackendProductAddpreattrspecificPostResponse,
)
async def addpreattrspecific(
    body: BackendProductAddpreattrspecificPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    addpreattrspecific
    """
    body.value_en=body.value_en.strip(',')
    model=await Service.preAttrSpecificationService.create(db,body)
    await db.commit()
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductAddpreattrspecificPostResponse(status='success', data=model.dict())


# </editor-fold>
