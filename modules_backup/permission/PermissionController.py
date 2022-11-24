from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncSession
from component.dbsession import get_webdbsession
import Service
from component.cache import cache
from fastapi import APIRouter,Depends
from sqlalchemy.exc import IntegrityError
import settings
from typing import Dict,Any
from common import get_token, CommonResponse, XTJsonResponse, findModelByName
import Models
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
async def allmodel(
    modelname:str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    modelcolumns
    """
    model=findModelByName(modelname)
    data=[c.name for c in model.__table__.columns]

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

    # install pydantic plugin,press alt+enter auto complete the args.
    return CommonResponse()


# </editor-fold>