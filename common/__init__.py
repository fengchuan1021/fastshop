from .globalFunctions import writelog,cmdlineApp,get_token,getorgeneratetoken
from .CommonResponse import CommonResponse,CommonQueryShema
from .CommonError import Common500Response,TokenException,PermissionException
from .encrypt import generateKey
from .filterbuilder import filterbuilder
from XTTOOLS import toJson,toBytesJson,XTJsonResponse
import Models
from functools import lru_cache
from typing import Type

# class XTContext:
#     def __init__(self, **kwargs):
#         for key,v in kwargs.items():
#             setattr(self,key,v)

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
