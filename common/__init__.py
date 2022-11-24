from .globalFunctions import writelog,async2sync,get_token,getorgeneratetoken
from .CommonResponse import CommonResponse,CommonQueryShema
from .CommonError import Common500Response,TokenException,PermissionException
from .encrypt import generateKey
from .filterbuilder import filterbuilder
from XTTOOLS import toJson,toBytesJson,XTJsonResponse
import Models
from functools import lru_cache
from typing import Type
@lru_cache(maxsize=None)
def findModelByName(name:str)->Type[Models.ModelType]:

    if tmp:=getattr(Models,name.upper()+name[1:],None):

        return tmp
    for tmpname,value in Models.__dict__.items():
        if not 65<=ord(tmpname[0])<=90:
            continue
        if tmpname.lower()==name.lower():
            return value
    raise Exception(f'not found {name}')
