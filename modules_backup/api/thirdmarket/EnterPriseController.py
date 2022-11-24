# generated timestamp: 2022-11-01T07:46:42+00:00

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common import CommonResponse
from component.dbsession import get_webdbsession
from common.globalFunctions import get_token
from common import XTJsonResponse

from .__init__ import dependencies
from .EnterPriseShema import (
    ApiThirdmarketSettiktokkeyPostRequest,

)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="settiktokkey post: /api/thirdmarket/settiktokkey">
@router.post(
    '/api/thirdmarket/settiktokkey',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
    
)
async def settiktokkey(
    body: ApiThirdmarketSettiktokkeyPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    settiktokkey
    """
    print('3333')
    await Service.enterpriseService.updateByPk(db,token.enterprise_id,body)

    await db.commit()
    # install pydantic plugin,press alt+enter auto complete the args.
    return CommonResponse(status='success',msg='add tiktok appkey success')


# </editor-fold>
