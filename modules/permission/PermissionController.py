from __future__ import annotations

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from component.dbsession import get_webdbsession
import Service
from component.cache import cache
from fastapi import APIRouter, Depends, Body
from sqlalchemy.exc import IntegrityError
import settings
from typing import Dict, Any, List
from common import get_token, CommonResponse, XTJsonResponse, findModelByName
from common import CommonError
import Models
import UserRole
from imp import reload
import os
from .__init__ import dependencies
router = APIRouter(dependencies=dependencies)


# <editor-fold desc="allmodel get: /permission/allmodel">
@router.get(
    '/permission/allmodel',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
)
async def allmodel(
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    allmodel
    """
    models=[]
    for name,class_ in Models.__dict__.items():
        if ord('A')<=ord(name[0])<=ord('Z'):
            try:
                if issubclass(class_,Models.Base):
                    models.append(name)
            except Exception as e:
                pass

    # install pydantic plugin,press alt+enter auto complete the args.
    return CommonResponse(status='success',data=models)


# </editor-fold>


# <editor-fold desc="modelcolumns get: /permission/modelcolumns">
@router.get(
    '/permission/modelcolumns/{modelname}',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
)
async def modelcolumns(
    modelname:str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    modelcolumns
    """
    model=findModelByName(modelname)
    data=[c.name for c in model.__table__.columns]#type: ignore

    # install pydantic plugin,press alt+enter auto complete the args.
    return CommonResponse(status='success',data=data)


# </editor-fold>

# <editor-fold desc="setrolemodelpermission post: /permission/setrolemodelpermission">
from .PermissionShema import PermissionSetrolemodelpermissionPostRequest
@router.post(
    '/permission/setrolemodelpermission',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
)
async def setrolemodelpermission(
    body: PermissionSetrolemodelpermissionPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    setrolemodelpermission
    """
    if not body.role_name:
        body.role_name=UserRole.UserRole(body.role_id).name

    body.read_columns = ','.join(body.read_columns)#type: ignore
    body.write_columns = ','.join(body.write_columns)#type: ignore
    body.update_columns = ','.join(body.update_columns)#type: ignore
    body.delete_columns = ','.join(body.delete_columns)#type: ignore

    body.read_extra = ','.join(body.read_columns)#type: ignore
    body.write_extra = ','.join(body.write_columns)#type: ignore
    body.update_extra = ','.join(body.update_columns)#type: ignore
    body.delete_extra = ','.join(body.delete_columns)#type: ignore

    await Service.graphpermissionService.create(db,body)
    await db.commit()
    return {'status':'success'}


# </editor-fold>


# <editor-fold desc="getrolelist get: /backend/permission/role/">
@router.get(
    '/permission/rolelist',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
)
async def getrolelist(
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    getrolelist
    """
    roles=[{'role_name':r.name,'role_id':r.value} for r in UserRole.UserRole]
    #roles=await Service.roleService.getList(db)
    return CommonResponse(status='success',data=roles)



# </editor-fold>

# <editor-fold desc="createrole post: /backend/permission/role/">
@router.post(
    '/permission/createrole',
    response_class=XTJsonResponse,

)
async def createrole(
    body:Dict= Body(...),
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    createrole
    """
    if 'role_name' not in body:
        return CommonResponse(status='failed',msg='role_name not provided')

    for i in UserRole.UserRole:
        maxvalue=i.value
        if i.name==body['role_name']:
            return {'status':'failed','msg':"role has exists"}
    newmaxvalue=maxvalue+1

    with open(os.path.join(settings.BASE_DIR,'UserRole.py'),'a',encoding='utf8') as f:
        f.write(f"    {body['role_name']}={newmaxvalue}\n")
    reload(UserRole)

    # install pydantic plugin,press alt+enter auto complete the args.
    return {'status':'success','role':{'id':newmaxvalue,'role_name':body['role_name']}}


# </editor-fold>


# <editor-fold desc="getroutelist get: /permission/routes">
@router.get(
    '/permission/routes',
    response_class=XTJsonResponse,

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


# </editor-fold>



# <editor-fold desc="setrolepermission post: /backend/permission/setrolepermission">
@router.post(
    '/permission/setrolepermission',
    response_class=XTJsonResponse,

)
async def setrolepermission(
    body: Dict=Body(...),
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    setrolepermission
    """
    if 'role_id' not in body:
        return {'status':'failed','msg':'role_id not provided'}
    if 'apis' not in body:
        return {'status':'failed','msg':'apis not provided'}

    if body['role_id'] not in [i.value for i in UserRole.UserRole]:
        return {'status':'falied','msg':"user role not exists"}
    await Service.permissionService.setUserRolePermission(db,body['role_id'],body['apis'])
    # install pydantic plugin,press alt+enter auto complete the args.
    return {'status':'success'}


# </editor-fold>


# <editor-fold desc="deleterole delete: /backend/permission/role/{id}">
@router.delete(
    '/permission/role/{id}',
    response_class=XTJsonResponse,

)
async def deleterole(
    id: int,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    deleterole
    """
    todel=''
    for r in UserRole.UserRole:
        if r.value==id:
            todel='    '+r.name
            break
    if todel:
        with open(os.path.join(settings.BASE_DIR,'UserRole.py'),'r',encoding='utf8') as f:
            content=[l for l in f.readlines() if not l.startswith(todel)]
        with open(os.path.join(settings.BASE_DIR, 'UserRole.py'), 'w', encoding='utf8') as f:
            f.write(''.join(content))
            reload(UserRole)
            return {'status':'success'}
    else:
        return {'status': 'success','msg':'role not found'}
    await Service.roleService.deleteByPk(db,id)

    return {'status':'success'}




# </editor-fold>


# <editor-fold desc="admingetroledisplayedmenu get: /backend/permission/admingetroledisplayedmenu">
@router.get(
    '/backend/permission/admingetroledisplayedmenu',
    response_class=XTJsonResponse,
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
    return {'status':'success','data':[r.menu_path for r in result]}


# </editor-fold>


# <editor-fold desc="setroledisplayedmenu post: /backend/permission/setdisplayedmenu">
class BackendPermissionSetdisplayedmenuPostRequest(BaseModel):
    role_id: int
    menus: List[str]
@router.post(
    '/permission/setdisplayedmenu',
    response_class=XTJsonResponse,
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
    return {'status':'success'}


# </editor-fold>


# <editor-fold desc="delerolepermission delete: /backend/permission/delrolepermission/{permission_id}">
# @router.post(
#     '/backend/permission/delrolepermission/{permission_id}',
#     response_class=XTJsonResponse,
#
# )
# async def delerolepermission(
#     permission_id: str,
#     db: AsyncSession = Depends(get_webdbsession),
#     token: settings.UserTokenData = Depends(get_token),
# ) -> Any:
#     """
#     delerolepermission
#     """
#     await Service.permissionService.deleteByPk(db,permission_id)
#
#     # install pydantic plugin,press alt+enter auto complete the args.
#     return {'status':'success'}


# </editor-fold>
