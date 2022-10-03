# generated timestamp: 2022-10-03T17:04:24+00:00

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
import UserRole
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
    BackendPermissionSetrolepermissionPostRequest,
    BackendPermissionSetrolepermissionPostResponse,Role
)
from imp import reload
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
    routes=await Service.permissionService.getroutelist()
    def tolist(tmp):
        if 'children' in tmp:
            tmp['children'] = list(tmp['children'].values())
            for item in tmp['children']:
                tolist(item)
    tolist(routes)
    print('routes:',routes)
    topmodel=BackendPermissionRouteGetResponse.parse_obj(routes)
    # install pydantic plugin,press alt+enter auto complete the args.
    return topmodel


# </editor-fold>


# <editor-fold desc="setrolepermission post: /backend/permission/setrolepermission">
@router.post(
    '/backend/permission/setrolepermission',
    response_class=XTJsonResponse,
    response_model=BackendPermissionSetrolepermissionPostResponse,
)
async def setrolepermission(
    body: BackendPermissionSetrolepermissionPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    setrolepermission
    """
    if body.role_id not in [i.value for i in UserRole.UserRole]:
        return {'status':'falied','msg':"user role not exists"}
    await Service.permissionService.setUserRolePermission(db,body.role_id,body.apis)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendPermissionSetrolepermissionPostResponse(status='success')


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
    for i in UserRole.UserRole:
        maxvalue=i.value
        if i.name==body.rolename:
            return {'status':'failed','msg':"role has exists"}
    newmaxvalue=maxvalue*2

    with open(os.path.join(settings.BASE_DIR,'UserRole.py'),'a',encoding='utf8') as f:
        f.write(f"    {body.rolename}={newmaxvalue}\n")
    reload(UserRole)

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendPermissionRolePostResponse(status='success')


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
    roles=[Role(role_name=r.name,id=r.value) for r in UserRole.UserRole]
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendPermissionRoleGetResponse(status='success',roles=roles)



# </editor-fold>
