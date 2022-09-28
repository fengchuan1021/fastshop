#type: ignore
from __future__ import annotations
import json
import typing

import orjson
from redis.asyncio import Redis
import redis.asyncio as redis
import Models
import settings
from component.cache.key_builder import default_key_builder

from common.globalFunctions import toJson
import asyncio
from functools import wraps
from typing import Callable, Optional, Type,Dict,Tuple,Any,TypeVar,Callable,overload,cast
from inspect import signature,isclass
from Models import Base
ModelType = TypeVar("ModelType", bound=Base)
F = TypeVar('F', bound=Callable[..., Any])
_StrType = TypeVar("_StrType", bound=str | bytes)

class _Cache:
    #self._loop: asyncio.AbstractEventLoop

    def __init__(self)->None:
        self._prefix:str = settings.CACHE_PREFIX
        self._expire:int = settings.DEFAULT_CACHE_EXPIRE
        self._init:bool = False
        self._enable:bool = settings.ENABLE_CACHE
        if self._enable and settings.REDISURL:
            writepool = redis.ConnectionPool.from_url(url=settings.REDISURL)
            readpool = redis.ConnectionPool.from_url(url=settings.SLAVEREDISURL)
            self.write_redis: Redis = redis.Redis(connection_pool=writepool)
            self.read_redis: Redis = redis.Redis(connection_pool=readpool)
        if not settings.REDISURL:
            self._enable=False
            print("cache not enable")
        self._loop:asyncio.AbstractEventLoop
        try:
            loop=asyncio.get_running_loop()
            self._loop = loop
        except Exception as e:
            loop=asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self._loop=loop
    def init(
        self,
        prefix: str = settings.CACHE_PREFIX,
        expire: int = settings.DEFAULT_CACHE_EXPIRE,
        enable: bool = settings.ENABLE_CACHE,
    )->None:#type: ignore
        if self._init:
            return
        self._init = True
        self._prefix = prefix
        self._expire = expire if expire else settings.DEFAULT_CACHE_EXPIRE
        self._enable = enable
        try:
            loop=asyncio.get_running_loop()
            self._loop = loop
        except Exception as e:
            loop=asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self._loop=loop


    @overload
    def __call__(self,__func: Optional[F]=None) -> F: ...

    @overload
    def __call__(self,*, key='',expire: Optional[int]=settings.DEFAULT_CACHE_EXPIRE,key_builder: Optional[Callable[...,str]]=None) -> Callable[[F], F]: ...

    def __call__(
            self,
            __func:Optional[F] = None,
            *,
            key: Optional[str]='',
            expire: Optional[int] = 0,
            key_builder: Optional[Callable[...,str] | str]= None,
    )-> F | Callable[[F], F]:
        """
        cache all function

        :param expire:
        :param key_builder:
        :return:
        """

        def decorator(func:F)->F:
            if not self._enable:
                return func
            funcsig=signature(func)

            @wraps(func)
            async def inner(*args:Any, **kwargs:Any)->Any:
                nonlocal expire
                nonlocal key_builder
                nonlocal key
                expire = expire or self.get_expire()
                func_args=funcsig.bind(*args,**kwargs)
                func_args.apply_defaults()
                classinstance=func_args.arguments.get('self',False)
                usecache=True
                _key=key
                if classinstance:
                    usecache=getattr(classinstance,'usecache')
                if usecache:
                    if not key:
                        key_builder = key_builder or default_key_builder
                        if isinstance(key_builder,str) and classinstance:
                            key_builder =getattr(classinstance,key_builder)
                        calutedkey = key_builder(
                            func,funcsig,func_args
                        )
                        _key=key or calutedkey
                    ret = await self.get(_key)
                    if ret and (returndic:=json.loads(ret)):
                        if isinstance(tmpClass:=func.__annotations__.get('return',int),typing._GenericAlias):
                            returntype=tmpClass.__args__[0]
                            listtype=True if tmpClass.__origin__==list else False
                            if returntype==ModelType:
                                returnclass=classinstance.model
                            elif issubclass(returntype, Models.Base):
                                returnclass=tmpClass.__args__[0]

                            if not listtype:
                                tmpmodel=returnclass(**returndic)
                                tmpmodel._sa_instance_state.committed_state = {}
                                tmpmodel._sa_instance_state.key = (returnclass, (returndic['id'],), None)
                                return tmpmodel
                            if listtype:
                                arr=[]
                                for item in returndic:
                                    tmpmodel=returnclass(**item)
                                    tmpmodel._sa_instance_state.committed_state = {}
                                    tmpmodel._sa_instance_state.key = (returnclass, (item['id'],), None)
                                    arr.append(tmpmodel)
                                return arr

                        elif tmpClass==ModelType:
                            tmpmodel=classinstance.model(**returndic)
                            tmpmodel._sa_instance_state.committed_state = {}
                            tmpmodel._sa_instance_state.key = (classinstance.model, (returndic['id'],), None)
                            return tmpmodel

                        elif isclass(tmpClass) and issubclass(tmpClass,Models.Base):
                            tmpmodel = tmpClass(**returndic)
                            tmpmodel._sa_instance_state.committed_state = {}
                            tmpmodel._sa_instance_state.key = (tmpClass, (returndic['id'],), None)
                            return tmpmodel
                        return returndic

                if asyncio.iscoroutinefunction(func):
                    ret = await func(*args, **kwargs)
                    # await func(inDataType)
                else:
                    ret = func(*args, **kwargs)
                try:
                    if usecache and ret:
                        await self.set(_key, toJson(ret), expire)
                    return ret
                except Exception as e:
                    print('function returned are not jsonable',e)
                return ret
            return cast(F, inner)

        if __func is not None:
            return decorator(__func)
        else:

            return decorator



    def get_prefix(self)->str:
        return self._prefix

    def get_expire(self)->int:
        return self._expire





    def get_enable(self)->bool:
        return self._enable
    
    async def clear(self, key: str = None) -> int:

        if key:
            return await self.write_redis.delete(key)
        else:
            return 0
    async def flush(self)->None:
        await self.write_redis.flushall()

    async def get_with_ttl(self, key: str) -> Tuple[int, str]:
        async with self.read_redis.pipeline(transaction=True) as pipe:
            return await (pipe.ttl(key).get(key).execute()) #type: ignore


    async def get(self, key:str) -> _StrType | None:
        return await self.read_redis.get(key)
    async def close(self):
        await self.read_redis.close(True)
        await self.write_redis.close(True)

    async def delete(self,key):
        await self.write_redis.delete(key)

    async def set(self, key: str, value: str, expire: int = None)-> bool | None:
        return await self.write_redis.set(key, value, ex=expire)



cache=_Cache()