from typing import Type,TypeVar,List,Iterable,Literal
import asyncio
import settings
from Models import Base
from pydantic import  BaseModel
INDATATYPE=Type[BaseModel]
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict,Callable,Any,Generic,cast
Model= TypeVar("Model", bound=Base)
F = TypeVar('F', bound=Callable[..., Any])
from collections import defaultdict
broadcastqueue=defaultdict(list)

def AfterModelUpdated(listenModel : Type[Model]| Literal['*'],background:bool=False)->Callable[[F], F]:


    queuename = f'After{"*" if listenModel=="*" else listenModel.__name__}Updated{background}'

    def decorator(func:F)->F:
        broadcastqueue[queuename].append(func)
        def wrapper(*args:Any,**kwargs:Any)->Any:
           return func(*args,**kwargs)

        return cast(F, wrapper)
    return decorator

async def fireAfterUpdated(updatedModels:Iterable[Model],db: AsyncSession,token:settings.UserTokenData=None,background:bool=False)->None:
    for model in updatedModels:
        name=f'After{model.__class__.__name__}Updated{background}'
        for func in broadcastqueue[name]+broadcastqueue[f'After*Updated{background}']:
            if asyncio.iscoroutinefunction(func):
                await func(model,db,token)
            else:
                raise Exception("call back must be a async function")


def BeforeModelCreated(listenModel : Type[Model]| Literal['*'])->Callable[[F], F]:
    queuename=f'Before{"*" if listenModel=="*" else listenModel.__name__}Created'

    def decorator(func:F)->F:
        broadcastqueue[queuename].append(func)
        def wrapper(*args:Any,**kwargs:Any)->Any:
            return func(*args,**kwargs)
        return cast(F, wrapper)
    return decorator
async def fireBeforeCreated(newModels:Iterable[Model],db: AsyncSession,token:settings.UserTokenData=None)->None:
    # no meaning to run listener in background. because created model could be rollback. but background task dont know.
    for model in newModels:
        name=f'Before{model.__class__.__name__}Created'

        for func in broadcastqueue[name]+broadcastqueue[f'Before*Created']:
            if asyncio.iscoroutinefunction(func):
                await func(model,db,token)
            else:
                raise Exception("call back must be a async function")
def AfterModelDeleted(listenModel:Type[Model] | Literal['*'],background:bool=False)->Callable[[F], F]:
    queuename = f'After{"*" if listenModel=="*" else listenModel.__name__}Deleted{background}'

    def decorator(func:F)->F:
        broadcastqueue[queuename].append(func)
        def wrapper(*args:Any,**kwargs:Any)->Any:
           return func(*args,**kwargs)
        return cast(F, wrapper)
    return decorator
async def fireAfterDeleted(deletedModels:Iterable[Model],db:AsyncSession,token:settings.UserTokenData=None,background:bool=False)->None:
    for model in deletedModels:
        name=f'After{model.__class__.__name__}Deleted{background}'

        for func in broadcastqueue[name]+broadcastqueue[f'After*Deleted{background}']:
            if asyncio.iscoroutinefunction(func):
                await func(model,db,token)
            else:
                raise Exception("call back must be a async function")

def AfterModelCreated(listenModel : Type[Model]| Literal['*'],background:bool=False)->Callable[[F], F]:
    queuename = f'After{"*" if listenModel=="*" else listenModel.__name__}Created{background}'

    def decorator(func:F)->F:
        broadcastqueue[queuename].append(func)
        def wrapper(*args:Any,**kwargs:Any)->Any:
           return func(*args,**kwargs)
        return cast(F, wrapper)
    return decorator

async def fireAfterCreated(newModels:Iterable[Model],db: AsyncSession,token:settings.UserTokenData=None,background:bool=False)->None:
    for model in newModels:
        name=f'After{model.__class__.__name__}Created{background}'

        for func in broadcastqueue[name]+broadcastqueue[f'After*Created{background}']:
            if asyncio.iscoroutinefunction(func):
                await func(model,db,token)
            else:
                raise Exception("call back must be a async function")

print('test11')