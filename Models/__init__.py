from .ModelBase import Base
from typing import TypeVar
ModelType = TypeVar("ModelType", bound=Base)
from .Permission import Permission,Roledisplayedmenu
from .User import User
from .product.AttrSpecification import PreAttrSpecification,ProductAttribute,ProductSpecification
from .product.Category import Category,ProductCategory
from .product.Product import Product,VariantStatis,Variant
from .product.VariantImage import VariantImage,ProductImgLog
from .site.Site import Site
from .site.Warehouse import Warehouse