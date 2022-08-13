import asyncio
from functools import wraps
from typing import Callable,Any
def sync2async(func:Callable[...,Any])->Callable[...,Any]:
    @wraps(func)
    def decorator(*args:Any,**kwargs:Any)->Any:

        loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)


        result=loop.run_until_complete(loop.create_task(func(*args,**kwargs)))

        return result
    return decorator
