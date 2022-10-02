

# generated timestamp: 2022-09-21T05:46:37+00:00

from __future__ import annotations

from typing import Any, Dict, Literal

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from component.cache import cache
from component.xtjsonresponse import XTJsonResponse

from modules.backend import dependencies
from .ProductShema import AddProductInShema,AddProductOutShema

router = APIRouter(dependencies=dependencies)#type: ignore

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
