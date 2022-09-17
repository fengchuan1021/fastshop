import asyncio
import datetime
from functools import wraps
from typing import Callable,Any

import settings
from elasticsearchclient import es
async def writelog(logstr:str)->None:
    doc = {
        'text': logstr,
        'request': '',
        'timestamp': datetime.datetime.now(),
    }
    await es.index(index=f"xtlog-{settings.MODE}", document=doc)

def sync2async(func:Callable[...,Any])->Callable[...,Any]:
    @wraps(func)
    def decorator(*args:Any,**kwargs:Any)->Any:

        loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result=loop.run_until_complete(loop.create_task(func(*args,**kwargs)))
            return result
        except Exception as e:
            loop.run_until_complete(writelog(str(e)))
            if settings.DEBUG:
                raise

    return decorator
