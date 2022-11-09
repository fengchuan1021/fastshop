# generated timestamp: 2022-10-19T08:41:48+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends,Request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from XTTOOLS import toBytesJson,toJson,cache,XTJsonResponse


from .__init__ import dependencies

from XTTOOLS import CommonResponse
router = APIRouter(dependencies=dependencies)


# <editor-fold desc="productbyvariantid get: /frontend/productbyvariantid/{variantid}">
@router.get(
    '/frontend/productbyvariantid/{variantid}',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
    striplang=True,

)
async def productbyvariantid(
    variantid: str,
    request:Request,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    productbyvariantid
    """
    data=await Service.productService.productdetailbyvariantid(db,variantid,request.state.siteinfo['lang'])
    if not data:
        return CommonResponse(status='failed', msg="cant find the product")
    # install pydantic plugin,press alt+enter auto complete the args.
    data=data.dict()
    data['specification']=[{"name":"colour","value":["blue",'red','black']},{"name":"size","value":["x","xxl","M"]}]
    return CommonResponse(status='success',data=data)


# </editor-fold>
