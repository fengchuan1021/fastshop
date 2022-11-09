# generated timestamp: 2022-10-03T10:52:05+00:00

from __future__ import annotations

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common.dbsession import get_webdbsession
from common.globalFunctions import get_token
from XTTOOLS import cache
from XTTOOLS import XTJsonResponse

from .__init__ import dependencies
from .UserShema import (
    FrontendUserLoginPostInShema,
    FrontendUserLoginPostOutShema,
    FrontendUserRegisterPostInShema,
    FrontendUserRegisterPostOutShema,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="register post: /frontend/user/register">
@router.post(
    '/frontend/user/register',
    response_class=XTJsonResponse,
    response_model=FrontendUserRegisterPostOutShema,
)
async def register(
    body: FrontendUserRegisterPostInShema,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    register
    """
    print('body:',body)
    for i in ['email','phone','username']:
        if i:
            user=await Service.userService.getUserByPhoneOrUsernameOrEmail(db,getattr(body,i))
        if user:
            return {'status':'failed','msg':f"{i} has been registered"}

    body.password=Service.userService.get_password_hash(body.password)
    newuser=await Service.userService.create(db,body)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        return {'status':'failed','msg':"email has been registered"}
    # install pydantic plugin,press alt+enter auto complete the args.
    return FrontendUserRegisterPostOutShema(status='success', user=newuser)


# </editor-fold>


# <editor-fold desc="login post: /frontend/user/login">
@router.post(
    '/frontend/user/login',
    response_class=XTJsonResponse,
    response_model=FrontendUserLoginPostOutShema,
)
async def login(
    body: FrontendUserLoginPostInShema,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    login
    """

    user=await Service.userService.authenticate(db,body.username,body.password)
    if not user:
        return {'status':'failed','msg':"username or password not valid"}
    enterprisemodel = await Service.enterpriseService.findOne(db, {'user_id':user.user_id})#type: ignore
    dic={'enterprise_id':enterprisemodel.enterprise_id} if enterprisemodel else {}
    newtoken=await Service.userService.create_access_token(user,extra_data=dic)#type: ignore
    refreshtoken=await Service.userService.create_refresh_token(user)#type: ignore
    # install pydantic plugin,press alt+enter auto complete the args.
    return FrontendUserLoginPostOutShema(status='success',token=newtoken,refreshtoken=refreshtoken)


# </editor-fold>
