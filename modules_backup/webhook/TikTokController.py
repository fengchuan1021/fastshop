

from __future__ import annotations

import hmac
from typing import Any

import orjson
from fastapi import APIRouter, Header, Body

import settings
from hashlib import sha256
from .__init__ import dependencies
from common import XTJsonResponse

router = APIRouter(dependencies=dependencies)
@router.post('/api/webhook/tiktok')
async def tiktokwebhook(body: str = Body(..., media_type='text/plain'),Authorization:str=Header(...))->Any:
    s=settings.TIKTOK_APPKEY+body
    sign = hmac.new( settings.TIKTOK_SECRET.encode('utf-8'),s.encode('utf-8'), digestmod=sha256).hexdigest()
    if sign!=Authorization:
        return XTJsonResponse({"code":-1,"msg":"verify signature failed"},status_code=500)
    notify=orjson.loads(body)
    shop_id=notify['shop_id']
    data=notify['shop_id']
    if notify['type']==1:#Order Status Update
        order_id,order_status,update_time=data.values()

    elif notify['type']==2:#Reverse Order
        pass
    elif notify['type']==3:#Receiver Address Updated
        pass
    elif notify['type']==4:#Package Updated
        pass
    elif notify['type']==5:#Product Audit Result Update
        pass
    return XTJsonResponse({"code": 0, "msg": "get it"}, status_code=200)