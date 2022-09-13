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
# def get_func_args(sig: Signature, *args: List, **kwargs: Dict) -> "OrderedDict[str, Any]":
#     """Return a dict object containing the name and value of all function arguments."""
#     func_args = sig.bind(*args, **kwargs)
#     func_args.apply_defaults()
#
#     return func_args.arguments
def get_args_str(sig_params: SigParameters, func_args: "OrderedDict[str, Any]") -> str:
    """Return a string with the name and value of all args whose type is not included in `ignore_arg_types`"""
    return ",".join(
        f"{arg}={val}" for arg, val in func_args.items() if arg not in ['self','cls'] and sig_params[arg].annotation not in ignore_arg_types
    )
def default_key_builder(
    func,
    funcsig:Signature=None,
    funcargs: BoundArguments=None,
    namespace: Optional[str] = ""
)->str:
    from component.cache import cache

    prefix = f"{cache.get_prefix()}:{namespace}:"
    sig_params = funcsig.parameters
    func_args = funcargs.arguments
    args_str = get_args_str(sig_params, func_args)

    return f"{prefix}{func.__module__}.{func.__name__}({args_str})"
