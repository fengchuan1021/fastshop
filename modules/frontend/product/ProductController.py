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

from .__init__ import  dependencies
from .ProductShema import FrontendProductIdLangOutShema

router = APIRouter( dependencies=dependencies)


# <editor-fold desc="getproductdetailbyid get: /frontend/product/{id}/{lang}">
@router.get(
    '/frontend/product/{id}/{lang}',
    response_class=XTJsonResponse,
    response_model=FrontendProductIdLangOutShema,
)
async def getproductdetailbyid(
    id: str,
    lang: str = Literal['en','cn'],
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getproductdetailbyid
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return FrontendProductIdLangOutShema()


# </editor-fold>
