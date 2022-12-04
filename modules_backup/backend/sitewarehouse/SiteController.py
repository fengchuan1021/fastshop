# generated timestamp: 2022-10-06T14:58:24+00:00

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
from .SiteShema import (
    BackendSiteAddsitePostRequest,
    BackendSiteAddsitePostResponse,
    BackendSiteSitelistPostRequest,
    BackendSiteSitelistPostResponse, BackendSiteDelsiteDeleteRequest, BackendSiteDelsiteDeleteResponse,
    BackendSiteEditsitePostRequest,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="addsite post: /backend/site/addsite">
@router.post(
    '/backend/site/addsite',
    response_class=XTJsonResponse,
    response_model=BackendSiteAddsitePostResponse,
)
async def addsite(
    body: BackendSiteAddsitePostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    addsite
    """
    await Service.siteService.create(db,body)
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendSiteAddsitePostResponse(status='success',msg='add site success')


# </editor-fold>


# <editor-fold desc="sitelist post: /backend/site/sitelist">
@router.post(
    '/backend/site/sitelist',
    response_class=XTJsonResponse,
    response_model=BackendSiteSitelistPostResponse,
)
async def sitelist(
    body: BackendSiteSitelistPostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    sitelist
    """
    results=await Service.siteService.find(db,**body.dict())
    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendSiteSitelistPostResponse(status='success', msg='', data=results)


# </editor-fold>



# <editor-fold desc="delsite delete: /backend/site/delsite">
@router.post(
    '/backend/site/delsite',
    response_class=XTJsonResponse,
    response_model=BackendSiteDelsiteDeleteResponse,
)
async def delsite(
    body: BackendSiteDelsiteDeleteRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    delsite
    """
    await Service.siteService.deleteByPk(db,body.site_id)

    # install pydantic plugin,press alt+enter auto complete the args.
    return BackendSiteDelsiteDeleteResponse(status='success')


# </editor-fold>

# <editor-fold desc="editsite post: /backend/site/editsite">
@router.post(
    '/backend/site/editsite',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
)
async def editsite(
    body: BackendSiteEditsitePostRequest,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    editsite
    """
    await Service.siteService.updateByPk(db, body.site_id, body)
    # install pydantic plugin,press alt+enter auto complete the args.
    return CommonResponse(status='success')


# </editor-fold>



# <editor-fold desc="getsupportlang post: /backend/site/getsupportlang">
@router.get(
    '/backend/site/getsupportlang',
    response_class=XTJsonResponse,
    response_model=CommonResponse,
)
async def getsupportlang(
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:


    return CommonResponse(status='success',data=[i.value for i in settings.SupportLang])


# </editor-fold>

