import settings
from fastapi import Request
from jose import  jwt
from component.snowFlakeId import snowFlack
from Models import Base
from Models import ModelType
from typing import Any
import json
from fastapi.encoders import jsonable_encoder

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


def _encodesqlalchemymodel(model:ModelType):#type: ignore
    return jsonable_encoder(model.as_dict())

def toJson(obj:Any)->str:
    return json.dumps(jsonable_encoder(obj,custom_encoder={Base:_encodesqlalchemymodel}))



