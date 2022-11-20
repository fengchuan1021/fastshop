
from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common import CommonResponse
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from common import cache
from common import XTJsonResponse

from .__init__ import dependencies


router = APIRouter(dependencies=dependencies)

from .EnterPriseShema import BindEnterpriseInShema
# <editor-fold desc="addsite post: /backend/site/addsite">
@router.post(
    '/admin/enterprise/bindenterprise',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
)
async def bindenterprise(
    body: BindEnterpriseInShema,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    addsite
    """

    await Service.enterpriseService.create(db,body)
    # install pydantic plugin,press alt+enter auto complete the args.
    return CommonResponse(status='success',msg='bind enterprise success')


# </editor-fold>