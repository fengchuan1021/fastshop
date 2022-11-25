import settings
from fastapi import Request
from jose import  jwt

from component.snowFlakeId import snowFlack
import asyncio
import datetime
from functools import wraps
from typing import Callable,Any
from elasticsearchclient import es


async def getorgeneratetoken(request:Request)-> settings.UserTokenData:
    try:
        tokenstr = request.headers.get('token',None)
        if not tokenstr:
            tokenstr=request.cookies.get('token',None)

        if tokenstr:
            payload = jwt.decode(tokenstr, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            data = settings.UserTokenData.parse_obj(payload)
            return data
        else:
            raise Exception("has not token in header or cookie")
    # except ExpiredSignatureError:
    #     raise
    except Exception as e:
        guest_token=settings.UserTokenData(user_id=snowFlack.getId(),is_guest=True)
        return guest_token

async def get_token(request:Request)->settings.UserTokenData:
    return request.state.token







async def writelog(logstr:str,request:str='')->None:
    if es:
        doc = {
            'text': logstr,
            'request': request,
            'timestamp': datetime.datetime.now(),
        }
        await es.index(index=f"xtlog-{settings.MODE.lower()}", document=doc)

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




