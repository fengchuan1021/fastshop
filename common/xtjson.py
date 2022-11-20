from pydantic import BaseModel
from decimal import Decimal
from typing import Any
import orjson
from sqlalchemy.engine import RowMapping
def obj2dict(obj:Any,striplang='')->Any:#type: ignore
    if hasattr(obj,'__tablename__'):
        return obj.dict(striplang=striplang)
    elif isinstance(obj,BaseModel):
        return obj.dict()
    elif isinstance(obj,Decimal):
        return str(obj)
    elif isinstance(obj,RowMapping):
        return dict(obj)
    raise Exception("object are not jsonable")

def toBytesJson(obj:Any,striplang:str='')->bytes:
    return orjson.dumps(obj,default=lambda obj :obj2dict(obj,striplang=striplang))

def toJson(obj:Any,striplang:str='')->str:
    return orjson.dumps(obj,default=lambda obj :obj2dict(obj,striplang=striplang)).decode()