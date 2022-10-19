# generated timestamp: 2022-10-19T08:41:48+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token, toJson
from component.cache import cache
from component.xtjsonresponse import XTJsonResponse

from .__init__ import dependencies
from .ProductShema import FrontendProductbyvariantidVariantidGetResponse

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="productbyvariantid get: /frontend/productbyvariantid/{variantid}">
@router.get(
    '/frontend/productbyvariantid/{variantid}',
    response_class=XTJsonResponse,
    response_model=FrontendProductbyvariantidVariantidGetResponse,
)
async def productbyvariantid(
    variantid: str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    productbyvariantid
    """
    data=await Service.productService.productdetailbyvariantid(db,variantid)
    # install pydantic plugin,press alt+enter auto complete the args.

    return FrontendProductbyvariantidVariantidGetResponse(status='success',data=data)


# </editor-fold>
