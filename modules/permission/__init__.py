from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

import Models
import settings
from common import PermissionException
from component.dbsession import get_webdbsession
from common.globalFunctions import get_token
from .. import dependencies as praentdependencies
from fastapi import Depends
from fastapi import Request


async def permission_check(request: Request,db: AsyncSession = Depends(get_webdbsession),token: settings.UserTokenData = Depends(get_token))->None:
    if 1 in token.userrole:
        pass
    else:
        raise PermissionException(msg="you dont have permission access this api")

from typing import List,Callable,Any
dependencies:List[Callable[...,Any]]=praentdependencies+[Depends(permission_check)]