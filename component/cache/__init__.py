from __future__ import annotations
import json
import types
import typing

from redis.asyncio import Redis
import redis.asyncio as redis

import Models
import settings
from component.cache.key_builder import default_key_builder
from fastapi.encoders import jsonable_encoder
from common.globalFunctions import toJson
import asyncio
from functools import wraps
from typing import Callable, Optional, Type,Dict,Tuple,Any,TypeVar,Callable,overload,cast
from inspect import signature
from Service.base import ModelType
F = TypeVar('F', bound=Callable[..., Any])
_StrType = TypeVar("_StrType", bound=str | bytes)

class CacheClass:
    #self._loop: asyncio.AbstractEventLoop

    def __init__(self)->None:
        self._prefix:str = settings.CACHE_PREFIX
        self._expire:int = settings.DEFAULT_CACHE_EXPIRE
        self._init:bool = False
        self._enable:bool = settings.ENABLE_CACHE
        self._loop:asyncio.AbstractEventLoop
        pool = redis.ConnectionPool.from_url(url=settings.REDISURL)
        self.redis: Redis= redis.Redis(connection_pool=pool)
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
    def __call__(self,*, key='',expire: Optional[int]=settings.DEFAULT_CACHE_EXPIRE,key_builder: Optional[Callable[...,str]]=None,namespace:Optional[str]='') -> Callable[[F], F]: ...

    def __call__(
            self,
            __func:Optional[F] = None,
            *,
            key: Optional[str]='',
            expire: Optional[int] = 0,
            key_builder: Optional[Callable[...,str] | str]= None,
            namespace: Optional[str] = "",
    )-> F | Callable[[F], F]:
        """
        cache all function

        :param expire:
        :param key_builder:
        :param namespace:
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
                if classinstance:
                    usecache=getattr(classinstance,'usecache')
                if usecache:
                    if not key:
                        key_builder = key_builder or default_key_builder
                        if isinstance(key_builder,str) and classinstance:
                            key_builder =getattr(classinstance,key_builder)
                        key = key_builder(
                            func,funcsig,func_args, namespace
                        )
                    ret = await self.get(key)
                    if ret and (returndic:=json.loads(ret)):
                        if isinstance(tmpClass:=func.__annotations__.get('return',int),typing._GenericAlias):
                            returntype=tmpClass.__args__[0]
                            listtype=True if tmpClass.__origin__==list else False
                            if returntype==ModelType:
                                returnclass=classinstance.model
                            elif issubclass(returntype, Models.Base):
                                returnclass=tmpClass.__args__[0]
                            return [returnclass(**item) for item in returndic] if listtype else returnclass(**returndic)
                        elif tmpClass==ModelType:
                            return classinstance.model(**returndic)
                        elif issubclass(tmpClass,Models.Base):
                            return tmpClass(**returndic)
                        return returndic

                if asyncio.iscoroutinefunction(func):
                    ret = await func(*args, **kwargs)
                    # await func(inDataType)
                else:
                    ret = func(*args, **kwargs)
                try:
                    if usecache and ret:
                        await self.set(key, json.dumps(toJson(ret)), expire)
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
    
    async def clear(self, namespace: str = None, key: str = None) -> int:
        if namespace:
            lua = f"for i, name in ipairs(redis.call('KEYS', '{namespace}:*')) do redis.call('DEL', name); end"
            return await self.redis.eval(lua, numkeys=0)
        elif key:
            return await self.redis.delete(key)
        else:
            return 0

    async def get_with_ttl(self, key: str) -> Tuple[int, str]:
        async with self.redis.pipeline(transaction=True) as pipe:
            return await (pipe.ttl(key).get(key).execute()) #type: ignore


    async def get(self, key:str) -> _StrType | None:
        return await self.redis.get(key)
    async def close(self):
        await self.redis.close(True)

    async def delete(self,key):
        await self.redis.delete(key)

    async def set(self, key: str, value: str, expire: int = None)-> bool | None:
        return await self.redis.set(key, value, ex=expire)



cache=CacheClass()