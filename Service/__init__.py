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
from .backend.PermissionService import PermissionService
from .payment.PaymentService import PaymentService
from .payment.paymethods.AdyenService import AdyenService
from .payment.paymethods.OnerwayService import OnerwayService
from .payment.paymethods.PaypalService import PaypalService
from .product.CategoryService import CategoryService
from .product.ProductService import VariantService,ProductService
from .search.ProductSearchService import ProductSearchService
from .site.SiteService import SiteService
from .site.VariantSiteService import VariantSiteService
from .thirdpartmarket.ThirdMarketService import ThirdMarketService
from .thirdpartmarket.market.TikTokService import TikTokService
from .thirdpartmarket.market.WishService import WishService
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
appService : CRUDBase[Models.App]
preAttrSpecificationService : CRUDBase[Models.PreAttrSpecification]
productAttributeService : CRUDBase[Models.ProductAttribute]
productSpecificationService : CRUDBase[Models.ProductSpecification]
brandService : CRUDBase[Models.Brand]
categoryService : CategoryService
productCategoryService : CRUDBase[Models.ProductCategory]
productService : ProductService
variantStatisService : CRUDBase[Models.VariantStatis]
variantService : VariantService
variantImageService : CRUDBase[Models.VariantImage]
productImgLogService : CRUDBase[Models.ProductImgLog]
variantSiteService : VariantSiteService
enterpriseService : CRUDBase[Models.Enterprise]
siteService : SiteService
warehouseService : CRUDBase[Models.Warehouse]
uploadService : UploadService
paymentService : PaymentService
adyenService : AdyenService
onerwayService : OnerwayService
paypalService : PaypalService
productSearchService : ProductSearchService
thirdMarketService : ThirdMarketService
tikTokService : TikTokService
wishService : WishService