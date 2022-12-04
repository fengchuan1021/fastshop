# generated timestamp: 2022-10-04T14:12:31+00:00

from __future__ import annotations

import os

from typing import Any, Dict

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
import Service
import settings

from component.dbsession import get_webdbsession
from common.globalFunctions import get_token
from common import XTJsonResponse

from .__init__ import dependencies
from .PermissionShema import (
    BackendPermissionPermissionlistGetResponse,
    BackendPermissionRoleGetResponse,
    BackendPermissionRoleIdDeleteResponse,
    BackendPermissionRolePostRequest,
    BackendPermissionRolePostResponse,
    BackendPermissionRouteGetResponse,
    BackendPermissionSetrolepermissionPostRequest,
    BackendPermissionSetrolepermissionPostResponse, Role, BackendPermissionPermissionlistGetRequest,
    BackendPermissionGetroledisplayedmenuGetResponse,
    BackendPermissionSetdisplayedmenuPostResponse, BackendPermissionSetdisplayedmenuPostRequest,
    BackendPermissionDelrolepermissionPermissionIdDeleteResponse
)
from imp import reload
router = APIRouter(dependencies=dependencies)


# <editor-fold desc="getroutelist get: /backend/permission/route/">
@router.get(
    '/backend/permission/route/',
    response_class=XTJsonResponse,
    response_model=BackendPermissionRouteGetResponse,
    response_model_exclude_unset=True
)
async def getroutelist(
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getroutelist
    """
    routes=await Service.permissionService.getroutelist()

    def tolist(tmp:Dict)->None:
        if 'children' in tmp:
            tmp['children'] = list(tmp['children'].values())
            for item in tmp['children']:
                tolist(item)
    tolist(routes)
    print('routes:',routes)
    return routes
    #topmodel=BackendPermissionRouteGetResponse.parse_obj(routes)
    # install pydantic plugin,press alt+enter auto complete the args.
    #return topmodel


# </editor-fold>


# <editor-fold desc="getrolepermissionlist get: /backend/permission/permissionlist">
@router.post(
    '/backend/permission/permissionlist',
    response_class=XTJsonResponse,
    response_model=BackendPermissionPermissionlistGetResponse,
)
async def getrolepermissionlist(
    body: BackendPermissionPermissionlistGetRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getrolepermissionlist
    """

    results,totalnum=await Service.permissionService.pagination(db,calcTotalNum=True,**body.dict())

    return BackendPermissionPermissionlistGetResponse(status='success', msg='',
                                                      data=results, total=totalnum, curpage=body.pagenum)


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
    allroles=await Service.roleService.find(db)
    if body.role_id not in [role.role_id for role in allroles]:
        return {'status':'falied','msg':"user role not exists"}
    await Service.permissionService.setUserRolePermission(db,body.role_id,body.apis)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendPermissionSetrolepermissionPostResponse(status='success')


# </editor-fold>


# <editor-fold desc="deleterole delete: /backend/permission/role/{id}">
@router.delete(
    '/backend/permission/role/{id}',
    response_class=XTJsonResponse,
    response_model=BackendPermissionRoleIdDeleteResponse,
)
async def deleterole(
    id: int,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    deleterole
    """
    await Service.roleService.deleteByPk(db,id)

    return {'status':'success'}




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
    model=await Service.roleService.create(db,body)
    await db.commit()

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendPermissionRolePostResponse(status='success',role={'id':model.role_id,'role_name':body.role_name})


# </editor-fold>





# <editor-fold desc="getroledisplayedmenu get: /backend/permission/getroledisplayedmenu">
@router.get(
    '/backend/permission/getroledisplayedmenu',
    response_class=XTJsonResponse,
    response_model=BackendPermissionGetroledisplayedmenuGetResponse,
)

async def getroledisplayedmenu(
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getroledisplayedmenu
    """
    result=await Service.permissionService.getroledisplayedmenu(db,token.userrole)
    return BackendPermissionGetroledisplayedmenuGetResponse(status='success',menus=[r.menu_path for r in result])


# </editor-fold>

# <editor-fold desc="admingetroledisplayedmenu get: /backend/permission/admingetroledisplayedmenu">
@router.get(
    '/backend/permission/admingetroledisplayedmenu',
    response_class=XTJsonResponse,
    response_model=BackendPermissionGetroledisplayedmenuGetResponse,
)

async def admingetroledisplayedmenu(
    role_id: int,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getroledisplayedmenu
    """
    result=await Service.permissionService.getroledisplayedmenu(db,role_id)
    return BackendPermissionGetroledisplayedmenuGetResponse(status='success',menus=[r.menu_path for r in result])


# </editor-fold>


# <editor-fold desc="setroledisplayedmenu post: /backend/permission/setdisplayedmenu">
@router.post(
    '/backend/permission/setdisplayedmenu',
    response_class=XTJsonResponse,
    response_model=BackendPermissionSetdisplayedmenuPostResponse,
)
async def setroledisplayedmenu(
    body: BackendPermissionSetdisplayedmenuPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    setroledisplayedmenu
    """
    await Service.permissionService.setRoleDisplayedMenu(db,body.role_id,body.menus)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendPermissionSetdisplayedmenuPostResponse(status='success')


# </editor-fold>


# <editor-fold desc="delerolepermission delete: /backend/permission/delrolepermission/{permission_id}">
@router.post(
    '/backend/permission/delrolepermission/{permission_id}',
    response_class=XTJsonResponse,
    response_model=BackendPermissionDelrolepermissionPermissionIdDeleteResponse,
)
async def delerolepermission(
    permission_id: str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    delerolepermission
    """
    await Service.permissionService.deleteByPk(db,permission_id)

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendPermissionDelrolepermissionPermissionIdDeleteResponse(status='success')


# </editor-fold>
