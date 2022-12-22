# generated timestamp: 2022-12-22T05:12:03+00:00

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
    MagentoProductShema,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="createproduct">
@router.post(
    '/merchant/product/magento/{store_id}/createproduct',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
)
async def createproduct(
    store_id: int,
    body: MagentoProductShema,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    createproduct
    """
    store, marketservice = await Service.thirdmarketService.getStoreandMarketService(db, token.merchant_id, store_id)
    ret = await Service.magentoService.createProduct(db, store, body)
    return {'status':'success'}


# </editor-fold>
