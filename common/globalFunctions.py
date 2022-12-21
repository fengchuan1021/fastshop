import settings
from fastapi import Request
from jose import  jwt


from component.snowFlakeId import snowFlack
import asyncio
import datetime
from functools import wraps
from typing import Callable,Any
import elasticsearchclient
from component.cache import cache

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
    if elasticsearchclient.es:
        doc = {
            'text': logstr,
            'request': request,
            'timestamp': datetime.datetime.now(),
        }
        await elasticsearchclient.es.index(index=f"xtlog-{settings.MODE.lower()}", document=doc)

def cmdlineApp(func:Callable[...,Any])->Callable[...,Any]:
    @wraps(func)
    def decorator(*args:Any,**kwargs:Any)->Any:

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            from common.after_start import after_start
            from component.dbsession import getdbsession
            dbclient=getdbsession(token=None)
            dbsession=dbclient.session
            loop.run_until_complete(after_start(dbsession))
            result=loop.run_until_complete(func(dbsession,*args,**kwargs))
            loop.run_until_complete(dbclient.close())

            return result
        except Exception as e:
            loop.run_until_complete(writelog(str(e)))
            if settings.DEBUG:
                raise

    return decorator




