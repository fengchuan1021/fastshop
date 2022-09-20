from .ModelBase import Base
from typing import TypeVar
ModelType = TypeVar("ModelType", bound=Base)
from .User import User
from .product.Product import ProductStatic,ProductDynamic,Category