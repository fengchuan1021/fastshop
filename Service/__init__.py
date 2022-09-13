import os
from typing import Any,TypeVar,TYPE_CHECKING
import Models
import sys

import settings

thismodule = sys.modules[__name__]
from .base import CRUDBase
ModelType = TypeVar("ModelType", bound=Models.Base)

from .UserService import UserService
not_cache_models=[Models.User]
def getModelname(name):
    return name[0].upper()+name[1:].replace('Service', '')

def __getattr__(name: str) -> Any:
    if classType:=thismodule.__annotations__.get(name,None):
        model=getattr(Models, getModelname(name))
        tmpinstance = classType(model,model not in not_cache_models)
        setattr(thismodule, name, tmpinstance)
        return tmpinstance
    if hasattr(Models, getModelname(name)):
        model = getattr(Models, getModelname(name))
        tmpinstance = CRUDBase(model,model not in not_cache_models)
        setattr(thismodule, name, tmpinstance)
        return tmpinstance
    raise Exception(f'not found {name}')

userService : UserService
productService : CRUDBase[Models.Product]
categoryService : CRUDBase[Models.Category]