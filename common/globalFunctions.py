import settings
import orjson
from fastapi import Request
from jose import  jwt
from component.snowFlakeId import snowFlack
from Models import Base
import asyncio
import datetime
from functools import wraps
from typing import Callable,Any
from pydantic import BaseModel
from elasticsearchclient import es


async def getorgeneratetoken(request:Request)-> settings.UserTokenData:
    try:
        tokenstr = request.headers.get('token',None)
        if not tokenstr:
            tokenstr=request.cookies.get('token',None)

        if tokenstr:
            payload = jwt.decode(tokenstr, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            data = settings.UserTokenData.parse_obj(payload)
            print("gettoken:",data)
            return data
        else:
            raise Exception("has not token in header or cookie")
    except Exception as e:
        guest_token=settings.UserTokenData(id=snowFlack.getId(),is_guest=True)
        return guest_token

async def get_token(request:Request)->settings.UserTokenData:
    return request.state.token


def obj2json(obj:Any)->str:#type: ignore
    if isinstance(obj,(BaseModel,Base)):
        return obj.json()
    raise Exception("object are not jsonable")

def toBytesJson(obj:Any)->bytes:
    return orjson.dumps(obj,default=obj2json)
def toJson(obj:Any)->str:
    return toBytesJson(obj).decode()



async def writelog(logstr:str)->None:
    doc = {
        'text': logstr,
        'request': '',
        'timestamp': datetime.datetime.now(),
    }
    await es.index(index=f"xtlog-{settings.MODE}", document=doc)

def async2sync(func:Callable[...,Any])->Callable[...,Any]:
    @wraps(func)
    def decorator(*args:Any,**kwargs:Any)->Any:

        loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result=loop.run_until_complete(func(*args,**kwargs))
            return result
        except Exception as e:
            loop.run_until_complete(writelog(str(e)))
            if settings.DEBUG:
                raise

    return decorator


