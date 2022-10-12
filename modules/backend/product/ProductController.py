

# generated timestamp: 2022-09-21T05:46:37+00:00

from __future__ import annotations

from typing import Any, Dict, Literal

from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Models
import Service
import settings
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from component.cache import cache
from component.xtjsonresponse import XTJsonResponse

from modules.backend import dependencies
from .ProductShema import AddProductInShema, AddProductOutShema, BackendProductPrefetchproductidGetResponse, \
    BackendProductAddproductimgPostResponse

router = APIRouter(dependencies=dependencies)#type: ignore
from component.snowFlakeId import snowFlack
@router.post(
    '/backend/product/addproduct',
    response_class=XTJsonResponse,
    response_model=AddProductOutShema,
)
async def getproductdetailbyid(
    inShema:AddProductInShema,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getproductdetailbyid
    """
    print(inShema)
    await Service.productService.addproduct(inShema)

    # install pydantic plugin,press alt+enter auto complete the args.
    return AddProductOutShema(status='ok')

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
    productimglog=Models.ProductImgLog(product_id=product_id,image_url=fileurl)
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
