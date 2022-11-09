# generated timestamp: 2022-10-09T07:45:48+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends, Body
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import undefer

import Models
import Service
import settings
from common.CommonResponse import CommonResponse
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from component.cache import cache
from XTTOOLS import XTJsonResponse

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
    await Service.preAttrSpecificationService.deleteByPk(db,preattrspecific_id)

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
    body.value_en=body.value_en.strip(',')#type: ignore
    model=await Service.preAttrSpecificationService.create(db,body)

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductAddpreattrspecificPostResponse(status='success', data=model.dict())


# </editor-fold>


# <editor-fold desc="getpreattrspecific get: /backend/product/getpreattrspecific/{id}">
@router.get(
    '/backend/product/getpreattrspecific/{id}',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
    striplang=False,
)
async def getpreattrspecific(
    id: str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getpreattrspecific
    """

    statment=select(Models.PreAttrSpecification).options(undefer("*")).filter(Models.PreAttrSpecification.preattrspecific_id==id)
    data=(await db.execute(statment)).scalar_one_or_none()
    return CommonResponse(status='success',data=data)


# </editor-fold>


# <editor-fold desc="updateproducttranslate get: /backend/product/updateproducttranslate/{product_id}">
@router.post(
    '/backend/product/updatepreattrspecifictranslate/{id}',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
    striplang=False,
)
async def updateproducttranslate(
    id: str,
    body: dict = Body(...),
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    updatepreattrspecifictranslate
    """
    supportlang=[i.value for i in settings.SupportLang]
    #for translate permission only allow them update language columns,not price,sku,category and others.
    newdic={key:value for key,value in body.items() if key.rsplit('_',1)[-1] in supportlang}
    model=await Service.preAttrSpecificationService.findByPk(db,id)
    if not model:
        return {'status':'failed','msg':'product not found'}
    for key in newdic:
        setattr(model,key,newdic[key])
    await db.commit()

    return CommonResponse(status='success',msg='translate success')


# </editor-fold>
