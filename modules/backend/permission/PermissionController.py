# generated timestamp: 2022-10-03T15:11:26+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from UserRole import UserRole
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from component.cache import cache
from component.xtjsonresponse import XTJsonResponse

from .__init__ import dependencies
from .PermissionShema import (
    BackendPermissionRoleGetResponse,
    BackendPermissionRolePostRequest,
    BackendPermissionRolePostResponse,
    BackendPermissionRouteGetResponse,
    BackendPermissionSetrolepermissionPostResponse, Role,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="getroutelist get: /backend/permission/route/">
@router.get(
    '/backend/permission/route/',
    response_class=XTJsonResponse,
    response_model=BackendPermissionRouteGetResponse,
)
async def getroutelist(
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getroutelist
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendPermissionRouteGetResponse()


# </editor-fold>


# <editor-fold desc="setrolepermission post: /backend/permission/setrolepermission">
@router.post(
    '/backend/permission/setrolepermission',
    response_class=XTJsonResponse,
    response_model=BackendPermissionSetrolepermissionPostResponse,
)
async def setrolepermission(
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    setrolepermission
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendPermissionSetrolepermissionPostResponse()


# </editor-fold>


# <editor-fold desc="createrole post: /backend/permission/role/">
@router.post(
    '/backend/permission/role/',
    response_class=XTJsonResponse,
    response_model=BackendPermissionRolePostResponse,
)
async def createrole(
    body: BackendPermissionRolePostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    createrole
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendPermissionRolePostResponse()


# </editor-fold>


# <editor-fold desc="getrolelist get: /backend/permission/role/">
@router.get(
    '/backend/permission/role/',
    response_class=XTJsonResponse,
    response_model=BackendPermissionRoleGetResponse,
)
async def getrolelist(
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getrolelist
    """
    roles=[Role(role_name=r.name,id=r.value) for r in UserRole]
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendPermissionRoleGetResponse(status='success',roles=roles)



# </editor-fold>
