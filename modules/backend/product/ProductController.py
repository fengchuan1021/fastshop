

# generated timestamp: 2022-09-21T05:46:37+00:00

from __future__ import annotations

from typing import Any, Dict, Literal

from fastapi import APIRouter, Depends, UploadFile,Request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import undefer_group

import Models
import Service
import settings
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from component.cache import cache
from component.xtjsonresponse import XTJsonResponse

from modules.backend import dependencies
from .ProductShema import BackendProductPrefetchproductidGetResponse, \
    BackendProductAddproductimgPostResponse, BackendProductAddproductPostResponse, BackendProductAddproductPostRequest, \
    BackendProductProductlistGetResponse, BackendProductProductlistGetRequest, \
    BackendProductPreviewproductbyvariantidVariantidGetResponse

router = APIRouter(dependencies=dependencies)#type: ignore
from component.snowFlakeId import snowFlack

# <editor-fold desc="addproduct post: /backend/product/addproduct">
@router.post(
    '/backend/product/addproduct',
    response_class=XTJsonResponse,
    response_model=BackendProductAddproductPostResponse,
)
async def addproduct(
    body: BackendProductAddproductPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    addproduct
    """
    await Service.productService.addproduct(db,body)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductAddproductPostResponse(status='success')#type :ignore


# </editor-fold>


# <editor-fold desc="addproductimg post: /backend/product/addproductimg">
@router.post(
    '/backend/product/addproductimg',
    response_class=XTJsonResponse,
    response_model=BackendProductAddproductimgPostResponse,
)
async def addproductimg(
    file: UploadFile,
    product_id: str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    addproductimg
    """
    data=await file.read()
    flag,fileurl=await Service.uploadService.uploadimg(data,'product')
    if not flag:
        return {'status':'falied','msg':'upload pic failed'}
    productimglog=Models.ProductImgLog(product_id=product_id,image_url=fileurl)#type: ignore
    db.add(productimglog)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductAddproductimgPostResponse(status='success',fileurl=fileurl)


# </editor-fold>


# <editor-fold desc="prefetchproductid get: /backend/product/prefetchproductid">
@router.get(
    '/backend/product/prefetchproductid',
    response_class=XTJsonResponse,
    response_model=BackendProductPrefetchproductidGetResponse,
)
async def prefetchproductid(
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    prefetchproductid
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductPrefetchproductidGetResponse(status='success', product_id=snowFlack.getId())


# </editor-fold>


# <editor-fold desc="productlist get: /backend/product/productlist">
@router.post(
    '/backend/product/productlist',
    response_class=XTJsonResponse,
    response_model=BackendProductProductlistGetResponse,
)
async def productlist(
    body: BackendProductProductlistGetRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    productlist
    """
    result,total=await Service.productService.pagination(db,options=[undefer_group('en')],calcTotalNum=True,**body.dict())
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductProductlistGetResponse(status='success',data=result)


# </editor-fold>

# <editor-fold desc="previewproductbyvariantid get: /backend/product/previewproductbyvariantid/{variantid}">
@router.get(
    '/backend/product/previewproductbyvariantid/{siteid}/{variantid}',
    response_class=XTJsonResponse,
    response_model=BackendProductPreviewproductbyvariantidVariantidGetResponse,
    striplang=True,
)
async def previewproductbyvariantid(
    variantid: str,
    siteid:str,
    request:Request,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    previewproductbyvariantid
    """
    site=await Service.siteService.findByPk(db,siteid)
    request.state.siteinfo={'lang':site.lang}#for language process
    data=await Service.productService.productdetailbyvariantid(db,variantid,site.lang)
    data=data.dict()

    data['specification']=[{"name":"colour","value":["blue",'red','black']},{"name":"size","value":["x","xxl","M"]}]
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendProductPreviewproductbyvariantidVariantidGetResponse(status='success',data=data)


# </editor-fold>
