from __future__ import annotations
import json
import os
import typing

from redis.asyncio import Redis
import redis.asyncio as redis
from XTTOOLS import toJson
import asyncio
from functools import wraps
from typing import Callable, Optional, Type,Dict,Tuple,Any,TypeVar,Callable,overload,cast,List,Mapping
from inspect import signature,isclass,Parameter,Signature, BoundArguments
from starlette.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession
ArgType = Type[object]
SigParameters = Mapping[str, Parameter]

from sqlalchemy.orm import DeclarativeMeta
ModelType = TypeVar("ModelType", bound=DeclarativeMeta)
F = TypeVar('F', bound=Callable[..., Any])
_StrType = TypeVar("_StrType", bound=str | bytes)
_BaseType=TypeVar("_BaseType",bound=str | int)
class _Cache:

    def __init__(self)->None:
        self._enable = True
        self._init=False
        self.writeurl=''
        self._loop:asyncio.AbstractEventLoop
        self.ignore_arg_types = [Request,AsyncSession]#,XTContext
        try:
            self.init()
        except Exception as e:
            pass
    def init(
        self,
        prefix: str = '',
        expire: int = 3600,
        enable: bool = True,
        writeurl:str='',
        readurl:str='',
        ignore_arg_types:List=[],
    )->None:#type: ignore

        self._prefix = prefix
        self._expire = expire
        self._enable = enable
        self.ignore_arg_types+=ignore_arg_types
        try:
            loop=asyncio.get_running_loop()
            self._loop = loop
        except Exception as e:
            loop=asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self._loop=loop
        if not writeurl:
            writeurl=os.getenv('REDISURL','')

        if not readurl:
            readurl=os.getenv('SLAVEREDISURL',writeurl)
        if writeurl and writeurl!=self.writeurl:
            self.writeurl=writeurl
            writepool = redis.ConnectionPool.from_url(url=writeurl)
            self.write_redis: Redis = redis.Redis(connection_pool=writepool)

            readpool = redis.ConnectionPool.from_url(url=readurl or writeurl)
            self.read_redis: Redis = redis.Redis(connection_pool=readpool)
        else:
            self._enable=False

    def default_key_builder(self,
            func: Callable,
            funcargs: BoundArguments,
            func_annotations: Any
    ) -> str:


        prefix = f"{self.get_prefix()}:"
        func_args = funcargs.arguments
        args_str = ",".join(
            f"{arg}={val}" for arg, val in func_args.items() if
            arg not in ['self', 'cls'] and func_annotations[arg] not in self.ignore_arg_types
        )

        return f"{prefix}:{func.__module__}.{func.__name__}({args_str})"

    @overload
    def __call__(self,__func: Optional[F]=None) -> F: ...

    @overload
    def __call__(self,*,key:str='',expire: Optional[int]=3600,key_builder: Optional[Callable[...,str]]=None) -> Callable[[F], F]: ...


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
            func_annotations=typing.get_type_hints(func)
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
                db=None
                if classinstance:
                    db=args[1]
                    usecache=getattr(classinstance,'usecache')
                if usecache:
                    if not key:
                        key_builder = key_builder or self.default_key_builder
                        if isinstance(key_builder,str) and classinstance:
                            key_builder =getattr(classinstance,key_builder)
                        calutedkey = key_builder(
                            func,func_args,func_annotations
                        )#type: ignore
                        _key=key or calutedkey

                    ret = await self.get(_key)#type: ignore
                    if ret and (returndic:=json.loads(ret)):
                        if isinstance(tmpClass:=func_annotations.get('return',int),typing._GenericAlias):

                            returntype=tmpClass.__args__[0]
                            listtype=True if tmpClass.__origin__==list else False
                            if returntype.__name__=='ModelType':#to fix returntype==ModelType
                                returnclass=classinstance.model
                            elif issubclass(returntype, DeclarativeMeta):
                                returnclass=tmpClass.__args__[0]

                            if not listtype:
                                tmpmodel=returnclass(**returndic)
                                tmpmodel._sa_instance_state.committed_state = {}
                                tmpmodel._sa_instance_state.key = (returnclass, (tmpmodel.id,), None)
                                if not tmpmodel._sa_instance_state.key in db.identity_map._dict:
                                    db.add(tmpmodel)
                                return tmpmodel
                            if listtype:
                                arr=[]
                                for item in returndic:
                                    tmpmodel=returnclass(**item)
                                    tmpmodel._sa_instance_state.committed_state = {}
                                    tmpmodel._sa_instance_state.key = (returnclass, (tmpmodel.id,), None)
                                    if not tmpmodel._sa_instance_state.key in db.identity_map._dict:
                                        db.add(tmpmodel)
                                    arr.append(tmpmodel)
                                return arr

                        elif tmpClass==ModelType:
                            tmpmodel=classinstance.model(**returndic)
                            tmpmodel._sa_instance_state.committed_state = {}
                            tmpmodel._sa_instance_state.key = (classinstance.model, (tmpmodel.id,), None)
                            if not tmpmodel._sa_instance_state.key in db.identity_map._dict:
                                db.add(tmpmodel)
                            return tmpmodel

                        elif isclass(tmpClass) and issubclass(tmpClass,DeclarativeMeta):
                            tmpmodel = tmpClass(**returndic)
                            tmpmodel._sa_instance_state.committed_state = {}
                            tmpmodel._sa_instance_state.key = (tmpClass, (tmpmodel.id,), None)
                            if not tmpmodel._sa_instance_state.key in db.identity_map._dict:
                                db.add(tmpmodel)
                            return tmpmodel
                        return returndic

                if asyncio.iscoroutinefunction(func):
                    ret = await func(*args, **kwargs)
                    # await func(inDataType)
                else:
                    ret = func(*args, **kwargs)
                try:
                    if usecache and ret:
                        await self.set(_key, toJson(ret), expire)#type: ignore
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


    async def get(self, key:str,decodestr:bool=False) -> _StrType | None:
        tmp=await self.read_redis.get(key)
        if decodestr:
            return tmp.decode() if tmp else ''#type: ignore
        return tmp

    async def keys(self,name:str,decodestr:bool=False)->List:
        if not decodestr:
            return await self.read_redis.keys(name)
        else:
            tmp=await self.read_redis.keys(name)
            return [t.decode() for t in tmp]

    async def close(self)->None:
        await self.read_redis.close(True)
        await self.write_redis.close(True)
    async def hget(self,name:str,key:str) -> _StrType | None:
        return await self.read_redis.hget(name,key)
    async def hset(self,name:str,key:str,value:_BaseType,ttl:int=None) -> int:
        if not ttl:
            return await self.write_redis.hset(name,key,value)
        else:
            async with self.write_redis.pipeline(transaction=True) as pipe:
                return await (pipe.hset(name,key,value).expire(key,ttl).execute())  # type: ignore
    async def setTtl(self,key:str,expire:int)-> bool:
        return await self.write_redis.expire(key,expire)

    async def delete(self,key:str)->None:
        await self.write_redis.delete(key)

    async def set(self, key: str, value: str, expire: int = None)-> bool | None:
        return await self.write_redis.set(key, value, ex=expire)



cache=_Cache()