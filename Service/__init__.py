import os
from typing import Any,TypeVar,TYPE_CHECKING
import Models
import sys

import settings

thismodule = sys.modules[__name__]
from .base import CRUDBase
ModelType = TypeVar("ModelType", bound=Models.Base)

from .UserService import UserService
from .product.ProductService import ProductDynamicService,ProductStaticService,ProductService
from .search.ProductSearchService import ProductSearchService
from .UploadService import UploadService
def getModelname(name:str)->str:
    return name[0].upper()+name[1:].replace('Service', '')

def __getattr__(name: str) -> Any:
    for annotationname,classtype in thismodule.__annotations__.items():
        if annotationname==name:
            if issubclass(classtype,CRUDBase):
                tmpinstance = classtype(getattr(Models, getModelname(name)))
            else:
                tmpinstance = classtype()
            setattr(thismodule, name, tmpinstance)
            return tmpinstance
    if hasattr(Models, getModelname(name)):
        model = getattr(Models, getModelname(name))
        tmpinstance = CRUDBase(model)
        setattr(thismodule, name, tmpinstance)
        return tmpinstance
    raise Exception(f'not found {name}')

userService : UserService
productStaticService : ProductStaticService
productDynamicService : ProductDynamicService
categoryService : CRUDBase[Models.Category]
productService : ProductService
productSearchService : ProductSearchService
uploadService:UploadService