#dont modfiy this file!!! it generate from devtools/template/Service__init__.py.tpl
#dont modfiy this file!!! it generate from devtools/template/Service__init__.py.tpl
from typing import Any,TypeVar
import Models
import sys

import settings

thismodule = sys.modules[__name__]
from .base import CRUDBase
ModelType = TypeVar("ModelType", bound=Models.Base)

from .UploadService import UploadService
from Service.user.UserService import UserService
from .product.ProductService import ProductDynamicService,ProductStaticService,ProductService
from .search.ProductSearchService import ProductSearchService

def getModelname(name:str)->str:
    return name[0].upper()+name[1:].replace('Service', '')

def __getattr__(name: str) -> Any:
    for annotationname,classtype in thismodule.__annotations__.items():
        if annotationname==name:
            if issubclass(classtype,CRUDBase):
                tmpinstance = classtype(model:=getattr(Models, getModelname(name)),model.__name__ not in settings.not_cache_models)
            else:
                tmpinstance = classtype()
            setattr(thismodule, name, tmpinstance)
            return tmpinstance
    if hasattr(Models, getModelname(name)):
        model = getattr(Models, getModelname(name))
        tmpinstance = CRUDBase(model,model.__name__ not in settings.not_cache_models)
        setattr(thismodule, name, tmpinstance)
        return tmpinstance
    raise Exception(f'not found {name}')

userService : UserService
productDynamicService : ProductDynamicService
productStaticService : ProductStaticService
categoryService : CRUDBase[Models.Category]
uploadService : UploadService
productService : ProductService
productSearchService : ProductSearchService