#dont modfiy this file!!! it generate from devtools/template/Service__init__.py.tpl
#dont modfiy this file!!! it generate from devtools/template/Service__init__.py.tpl
import os
from typing import Any,TypeVar,TYPE_CHECKING
import Models
import sys

import settings
import typing
thismodule = sys.modules[__name__]
from .base import CRUDBase
ModelType = TypeVar("ModelType", bound=Models.Base)

from .UploadService import UploadService
from .WishService import WishService
from .backend.PermissionService import PermissionService
from .product.CategoryService import CategoryService
from .product.ProductService import VariantDynamicService,VariantStaticService,ProductService
from .search.ProductSearchService import ProductSearchService
from .user.UserService import UserService

def getModelname(name:str)->str:
    return name[0].upper()+name[1:].replace('Service', '')

def __getattr__(name: str) -> Any:
    for annotationname,classtype in thismodule.__annotations__.items():
        if annotationname==name:
            if isinstance(classtype,typing._GenericAlias) or issubclass(classtype,CRUDBase):#type: ignore
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

permissionService : PermissionService
roledisplayedmenuService : CRUDBase[Models.Roledisplayedmenu]
userService : UserService
preAttrSpecificationService : CRUDBase[Models.PreAttrSpecification]
productAttributeService : CRUDBase[Models.ProductAttribute]
productSpecificationService : CRUDBase[Models.ProductSpecification]
categoryService : CategoryService
productCategoryService : CRUDBase[Models.ProductCategory]
productService : ProductService
variantDynamicService : VariantDynamicService
variantStaticService : VariantStaticService
variantImageService : CRUDBase[Models.VariantImage]
shopService : CRUDBase[Models.Shop]
warehouseService : CRUDBase[Models.Warehouse]
uploadService : UploadService
wishService : WishService
productSearchService : ProductSearchService