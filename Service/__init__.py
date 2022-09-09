import os
from typing import Any,TypeVar,TYPE_CHECKING
import Models
import sys

import settings

thismodule = sys.modules[__name__]
from .base import CRUDBase
ModelType = TypeVar("ModelType", bound=Models.Base)

from .UserService import UserService

def getModelname(name):
    return name[0].upper()+name[1:].replace('Service', '')

def __getattr__(name: str) -> Any:
    if classType:=thismodule.__annotations__.get(name,None):
        tmpinstance = classType(getattr(Models, getModelname(name)))
        setattr(thismodule, name, tmpinstance)
        return tmpinstance
    if hasattr(Models, getModelname(name)):
        model = getattr(Models, getModelname(name))
        tmpinstance = CRUDBase(model)
        setattr(thismodule, name, tmpinstance)
        return tmpinstance
    raise Exception(f'not found {name}')

userService : UserService
productService : CRUDBase[Models.Product]
categoryService : CRUDBase[Models.Category]