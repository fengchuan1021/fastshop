from typing import Any,TypeVar
import Models
import sys
thismodule = sys.modules[__name__]
from .base import CRUDBase
ModelType = TypeVar("ModelType", bound=Models.Base)


from .UserService import UserService

def __getattr__(name: str) -> Any:
    if hasattr(Models, name.replace('Service', '')):
        model = getattr(Models, name.replace('Service', ''))
        tmpinstance = CRUDBase(model)
        setattr(thismodule, name, tmpinstance)
        return tmpinstance
    raise Exception(f'not found {name}')

ProductService : CRUDBase[Models.Product]
CategoryService : CRUDBase[Models.Category]