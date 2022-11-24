# generated timestamp: 2022-10-06T06:03:09+00:00

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from Models.product.Category import Category
from component.dbsession import get_webdbsession
from common.globalFunctions import get_token
from component.cache import cache
from common import XTJsonResponse,CommonQueryShema

from .__init__ import dependencies
from .CategoryShema import (
    BackendProductAddcategoryPostRequest,
    BackendProductAddcategoryPostResponse,
    BackendProductDelcategoryPostRequest,
    BackendProductDelcategoryPostResponse,

    BackendProductGetcategorylistGetResponse,
    BackendProductGetcategorytreeGetResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="getcategorylist get: /backend/product/getcategorylist">
@router.post(
    '/backend/product/getcategorylist',
    response_class=XTJsonResponse,
    response_model=BackendProductGetcategorylistGetResponse,
)
async def getcategorylist(
    body: CommonQueryShema,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),

) -> Any:
    """
    getcategorylist
    """
    result,total=await Service.categoryService.pagination(db,**body.dict())

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductGetcategorylistGetResponse(status='success',data=result,total=total,curpage=body.pagenum)


# </editor-fold>


# <editor-fold desc="getcategorytree get: /backend/product/getcategorytree">
@router.get(
    '/backend/product/getcategorytree',
    response_class=XTJsonResponse,
    response_model=BackendProductGetcategorytreeGetResponse,
)
@cache(key='xt:admin:categorytree')
async def getcategorytree(
    db: AsyncSession = Depends(get_webdbsession),
    #token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getcategorytree
    """
    dic=await Service.categoryService.getCategoryTree(db)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductGetcategorytreeGetResponse(status='success', msg='', data=dic)


# </editor-fold>


# <editor-fold desc="delcategory post: /backend/product/delcategory">
@router.post(
    '/backend/product/delcategory',
    response_class=XTJsonResponse,
    response_model=BackendProductDelcategoryPostResponse,
)
async def delcategory(
    body: BackendProductDelcategoryPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    delcategory
    """
    await Service.categoryService.deleteByPk(db,body.category_id)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductDelcategoryPostResponse(status='success', msg='delete success')


# </editor-fold>


# <editor-fold desc="addcategory post: /backend/product/addcategory">
@router.post(
    '/backend/product/addcategory',
    response_class=XTJsonResponse,
    response_model=BackendProductAddcategoryPostResponse,
)
async def addcategory(
    body: BackendProductAddcategoryPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    addcategory
    """
    statment=select(Category).filter(Category.id==body.parent_id)
    parent=(await db.execute(statment)).scalar_one_or_none()
    if parent:
        body.parent_name=parent.category_name
    await Service.categoryService.create(db,body)

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductAddcategoryPostResponse(status='success', msg='add category success')


# </editor-fold>
