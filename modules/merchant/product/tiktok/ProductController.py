# generated timestamp: 2022-12-16T05:24:55+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common import CommonResponse, XTJsonResponse, get_token
from component.cache import cache
from component.dbsession import get_webdbsession
from component.fastQL import fastAdd, fastDel, fastQuery

from .__init__ import dependencies
from .ProductShema import (
    TiktokCreateproductShema
)

router = APIRouter(dependencies=dependencies)
from fastapi import UploadFile, Form

# <editor-fold desc="uploadimg">
@router.post(
    '/merchant/product/tiktok/uploadimg',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
)
async def uploadimg(
file: UploadFile,
store_id:int,
img_scene:int=Form(),

    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    uploadimg
    """
    store, marketservice = await Service.thirdmarketService.getStoreandMarketService(db, token.merchant_id, store_id)
    ret=await Service.tiktokService.uploadImg(db,store, await file.read(),img_scene)

    return ret


# </editor-fold>


# <editor-fold desc="uploadfile">
@router.post(
    '/merchant/product/tiktok/uploadfile',

    response_class=XTJsonResponse,
    response_model=CommonResponse,
)
async def uploadfile(
        file: UploadFile,
        file_name: str,
store_id:int,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    uploadfile
    """
    store, marketservice = await Service.thirdmarketService.getStoreandMarketService(db, token.merchant_id, store_id)
    ret=await Service.tiktokService.uploadFile(db,store, await file.read(),file_name)

    # install pydantic plugin,press alt+enter auto complete the args.
    return ret


# </editor-fold>


# <editor-fold desc="createproduct">
@router.post(
    '/merchant/product/tiktok/{store_id}/createproduct',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
)
async def createproduct(
    store_id:int,
    body: TiktokCreateproductShema,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    createproduct
    """
    store, marketservice = await Service.thirdmarketService.getStoreandMarketService(db, token.merchant_id, store_id)
    ret = await Service.tiktokService.createProduct(db, store, body)
    # install pydantic plugin,press alt+enter auto complete the args.
    return ret


# </editor-fold>
