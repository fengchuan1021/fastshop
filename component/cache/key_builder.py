import hashlib
from typing import Optional
from collections import OrderedDict
from starlette.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response
from settings import UserTokenData
ALWAYS_IGNORE_ARG_TYPES = [Request,AsyncSession,UserTokenData]
from inspect import Signature, BoundArguments
from typing import Callable,Any,List,Dict,Mapping, Type
from fastapi import  Response
from settings import UserTokenData
from sqlalchemy.ext.asyncio import AsyncSession
from inspect import Parameter
from inspect import signature
ArgType = Type[object]
SigParameters = Mapping[str, Parameter]


ignore_arg_types = [Request,UserTokenData,AsyncSession]

def default_key_builder(
    func:Callable,
    funcargs: BoundArguments,
    func_annotations:Any
)->str:
    from XTTOOLS import cache

    prefix = f"{cache.get_prefix()}:"
    func_args = funcargs.arguments
    args_str =",".join(
        f"{arg}={val}" for arg, val in func_args.items() if
        arg not in ['self', 'cls'] and func_annotations[arg] not in ignore_arg_types
    )


    return f"{prefix}:{func.__module__}.{func.__name__}({args_str})"
