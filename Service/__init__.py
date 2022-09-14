import os
from typing import Any,TypeVar,TYPE_CHECKING
import Models
import sys
from sqlalchemy.ext.asyncio import AsyncSession
import settings
import Broadcast
thismodule = sys.modules[__name__]
from .base import CRUDBase
ModelType = TypeVar("ModelType", bound=Models.Base)
from component.cache import cache
from .UserService import UserService
not_cache_models=[Models.User]
def getModelname(name):
    return name[0].upper()+name[1:].replace('Service', '')

def __getattr__(name: str) -> Any:
    if classType:=thismodule.__annotations__.get(name,None):
        model=getattr(Models, getModelname(name))

        @Broadcast.AfterModelUpdated(model,background=True)
        async def invalidmodelpkcache(model:Models.ModelType,db: AsyncSession,token:settings.UserTokenData,reason:str='')->None:
            key = f"{cache.get_prefix()}:modelcache:{model.__tablename__}:{model.id}"
            await cache.delete(key)

        tmpinstance = classType(model,model not in not_cache_models)
        setattr(thismodule, name, tmpinstance)
        return tmpinstance
    if hasattr(Models, getModelname(name)):
        model = getattr(Models, getModelname(name))

        @Broadcast.AfterModelUpdated(model,background=True)
        async def invalidmodelpkcache(model:Models.ModelType,db: AsyncSession,token:settings.UserTokenData,reason:str='')->None:
            key = f"{cache.get_prefix()}:modelcache:{model.__tablename__}:{model.id}"
            await cache.delete(key)

        tmpinstance = CRUDBase(model,model not in not_cache_models)

        setattr(thismodule, name, tmpinstance)
        return tmpinstance
    raise Exception(f'not found {name}')

userService : UserService
productService : CRUDBase[Models.Product]
categoryService : CRUDBase[Models.Category]