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
from .store.StoreService import StoreService
from .store.VariantStoreService import VariantSiteService
from .thirdpartmarket.ThirdMarketService import ThirdMarketService
from .thirdpartmarket.market.OnBuyService import OnBuyService
from .thirdpartmarket.market.TikTokService import TikTokService
from .thirdpartmarket.market.WishService import WishService
from .user.UserService import UserService

def findModelByName(lowername:str)->Any:

    if tmp:=getattr(Models,lowername[0].upper()+lowername[1:],None):
        return tmp
    for name,value in Models.__dict__.items():

        if not 65<=ord(name[0])<=90:
            continue

        if name.lower()==lowername:
            return value
    raise Exception(f'not found {name}')
def __getattr__(name: str) -> Any:

    lowername=name.replace('Service','')
    for i in lowername:
        if not 97<=ord(i)<=122:
            raise Exception("service name should be all lowercase")
    for annotationname,classtype in thismodule.__annotations__.items():

        if annotationname==name:

            if isinstance(classtype,typing._GenericAlias) or issubclass(classtype,CRUDBase):#type: ignore
                tmpinstance = classtype(model:=findModelByName(lowername),model.__name__ in settings.cache_models)#type: ignore
            else:
                tmpinstance = classtype()
            setattr(thismodule, name, tmpinstance)
            return tmpinstance

    raise Exception(f'not found {name}')

roleService : CRUDBase[Models.Role]
userroleService : CRUDBase[Models.UserRole]
permissionService : PermissionService
graphpermissionService : CRUDBase[Models.Graphpermission]
roledisplayedmenuService : CRUDBase[Models.Roledisplayedmenu]
userService : UserService
appService : CRUDBase[Models.App]
preattrspecificationService : CRUDBase[Models.PreAttrSpecification]
productattributeService : CRUDBase[Models.ProductAttribute]
productspecificationService : CRUDBase[Models.ProductSpecification]
brandService : CRUDBase[Models.Brand]
categoryService : CategoryService
productcategoryService : CRUDBase[Models.ProductCategory]
productService : ProductService
variantService : VariantService
variantimageService : CRUDBase[Models.VariantImage]
variantstoreService : CRUDBase[Models.VariantStore]
marketService : CRUDBase[Models.Market]
merchantService : CRUDBase[Models.Merchant]
storeService : StoreService
warehouseService : CRUDBase[Models.Warehouse]
uploadService : UploadService
paymentService : PaymentService
adyenService : AdyenService
onerwayService : OnerwayService
paypalService : PaypalService
productsearchService : ProductSearchService
variantsiteService : VariantSiteService
thirdmarketService : ThirdMarketService
onbuyService : OnBuyService
tiktokService : TikTokService
wishService : WishService