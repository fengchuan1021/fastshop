from typing import List,Callable,Any,Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from fastapi import Request
import settings
from common import PermissionException
from common.globalFunctions import get_token
async def permission_check(token: settings.UserTokenData = Depends(get_token))->None:
    if 2!=token.userrole:

        raise PermissionException(msg="you dont have permission access this api")

from typing import List,Callable,Any
dependencies:List[Callable[...,Any]]=[Depends(permission_check)]