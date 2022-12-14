#dont modfiy this file!!! it generate from devtools/template/Service__init__.py.tpl
#dont modfiy this file!!! it generate from devtools/template/Service__init__.py.tpl
import os
from typing import Any,TypeVar,TYPE_CHECKING
import Models
import sys
from common import findModelByName
import settings
import typing
thismodule = sys.modules[__name__]
from .base import CRUDBase
ModelType = TypeVar("ModelType", bound=Models.Base)

from .UploadService import UploadService
from .backend.PermissionService import PermissionService
from .order.ReviewOrderService import ReviewOrderService
from .payment.PaymentService import PaymentService
from .payment.paymethods.AdyenService import AdyenService
from .payment.paymethods.OnerwayService import OnerwayService
from .payment.paymethods.PaypalService import PaypalService
from .product.CategoryService import CategoryService
from .search.ProductSearchService import ProductSearchService
from .store.StoreService import StoreService
from .thirdpartmarket.ThirdMarketService import ThirdMarketService
from .thirdpartmarket.market.AmazonService import AmazonService
from .thirdpartmarket.market.MagentoService import MagentoService
from .thirdpartmarket.market.OnBuyService import OnBuyService
from .thirdpartmarket.market.TikTokService import TikTokService
from .thirdpartmarket.market.WishService import WishService
from .user.UserService import UserService


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

permissionService : PermissionService
graphpermissionService : CRUDBase[Models.Graphpermission]
roledisplayedmenuService : CRUDBase[Models.Roledisplayedmenu]
userService : UserService
appService : CRUDBase[Models.App]
countryService : CRUDBase[Models.Country]
orderService : CRUDBase[Models.Order]
orderaddressService : CRUDBase[Models.OrderAddress]
orderitemService : CRUDBase[Models.OrderItem]
orderstatushistoryService : CRUDBase[Models.OrderStatusHistory]
revieworderruleService : CRUDBase[Models.ReviewOrderRule]
ordershipmentService : CRUDBase[Models.OrderShipment]
ordershipmentitemService : CRUDBase[Models.OrderShipmentItem]
preattrspecificationService : CRUDBase[Models.PreAttrSpecification]
productattributeService : CRUDBase[Models.ProductAttribute]
productspecificationService : CRUDBase[Models.ProductSpecification]
brandService : CRUDBase[Models.Brand]
categoryService : CategoryService
productcategoryService : CRUDBase[Models.ProductCategory]
productService : CRUDBase[Models.Product]
variantService : CRUDBase[Models.Variant]
tiktokproductService : CRUDBase[Models.TiktokProduct]
tiktokvariantService : CRUDBase[Models.TiktokVariant]
variantimageService : CRUDBase[Models.VariantImage]
variantstoreService : CRUDBase[Models.VariantStore]
wishproductService : CRUDBase[Models.WishProduct]
wishvariantService : CRUDBase[Models.WishVariant]
purchasereceiptService : CRUDBase[Models.PurchaseReceipt]
purchasereceiptitemsService : CRUDBase[Models.PurchaseReceiptItems]
supplierService : CRUDBase[Models.Supplier]
suppliervariantService : CRUDBase[Models.SupplierVariant]
variantwarehouseService : CRUDBase[Models.VariantWarehouse]
variantwarehouseredeployService : CRUDBase[Models.VariantWarehouseRedeploy]
variantwarehouseredeployitemService : CRUDBase[Models.VariantWarehouseRedeployItem]
packageService : CRUDBase[Models.Package]
warehouseService : CRUDBase[Models.Warehouse]
warehouseshelveService : CRUDBase[Models.WarehouseShelve]
marketService : CRUDBase[Models.Market]
merchantService : CRUDBase[Models.Merchant]
storeService : StoreService
uploadService : UploadService
revieworderService : ReviewOrderService
paymentService : PaymentService
adyenService : AdyenService
onerwayService : OnerwayService
paypalService : PaypalService
productsearchService : ProductSearchService
thirdmarketService : ThirdMarketService
amazonService : AmazonService
magentoService : MagentoService
onbuyService : OnBuyService
tiktokService : TikTokService
wishService : WishService