# generated timestamp: 2022-10-05T15:57:31+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from component.cache import cache
from component.xtjsonresponse import XTJsonResponse

from .__init__ import dependencies
from .UserShema import BackendUserUserGetRequest, BackendUserUserGetResponse, BackendUserCreateuserPostResponse, \
    BackendUserCreateuserPostRequest

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="getuserlist get: /backend/user/user/">
@router.post(
    '/backend/user/userlist/',
    response_class=XTJsonResponse,
    response_model=BackendUserUserGetResponse,
)
async def getuserlist(
    body: BackendUserUserGetRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getuserlist
    """
    results,count=await Service.userService.pagination(db,**body.dict())
    print(results[0].dict())
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendUserUserGetResponse(status='success', msg='', total=count, data=results)


# </editor-fold>

# <editor-fold desc="createuser post: /backend/user/createuser">
@router.post(
    '/backend/user/createuser',
    response_class=XTJsonResponse,
    response_model=BackendUserCreateuserPostResponse,
)
async def createuser(
    body: BackendUserCreateuserPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    createuser
    """
    body.password=Service.userService.get_password_hash(body.password)
    user=await Service.userService.create(db,body)

    # try:
    #     await db.commit()
    # except IntegrityError:
    #     await db.rollback()
    #     return {'status':'failed','msg':"user existed"}
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendUserCreateuserPostResponse(status='success',msg='add user success')


# </editor-fold>