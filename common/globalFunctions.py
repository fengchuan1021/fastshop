import orjson

import settings
from fastapi import Request
from jose import  jwt
from component.snowFlakeId import snowFlack
from Models import Base
from Models import ModelType
from typing import Any



async def getorgeneratetoken(request:Request)-> settings.UserTokenData:
    try:
        tokenstr = request.headers.get('token',None)
        if not tokenstr:
            tokenstr=request.cookies.get('token',None)

        if tokenstr:
            payload = jwt.decode(tokenstr, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            data = settings.UserTokenData.parse_obj(payload)
            print("gettoken:",data)
            return data
        else:
            raise Exception("has not token in header or cookie")
    except Exception as e:
        guest_token=settings.UserTokenData(id=snowFlack.getId(),is_guest=True)
        return guest_token

async def get_token(request:Request)->settings.UserTokenData:
    return request.state.token

from pydantic import BaseModel
def obj2json(obj:Any)->str:#type: ignore
    if isinstance(obj,(BaseModel,Base)):
        return obj.json()
    raise Exception("object are not jsonable")

def toJson(obj:Any)->str:
    return orjson.dumps(obj,default=obj2json).decode()



