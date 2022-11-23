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

{imports}

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
                tmpinstance = classtype(model:=findModelByName(lowername),model.__name__ not in settings.not_cache_models)#type: ignore
            else:
                tmpinstance = classtype()
            setattr(thismodule, name, tmpinstance)
            return tmpinstance

    raise Exception(f'not found {name}')

{annotations}