

from __future__ import annotations

import base64
import hashlib
import hmac
from typing import Any

from fastapi import APIRouter, Header, Body

import Service
import settings
from .__init__ import dependencies
from dateutil import parser
router = APIRouter(dependencies=dependencies)
@router.get('/api/wish/appcallback')
async def wishappcallback(code:str)->Any:
    retdata=await Service.wishService.getAccessToken()#type: ignore
    print("tokenfromwish:", retdata)
    access_token = retdata['data']['access_token']#type: ignore
    refresh_token = retdata['data']['refresh_token']#type: ignore
    access_token_expire=parser.parse(retdata['data']['expiry_time']).timestamp()#type: ignore

    # await cache.set('wishrefreshtoken', self.refresh_token)


@router.get('/api/wish/webhook')
async def wishwebhook(body: str = Body(..., media_type='text/plain'),Wish_Hmac_Sha256:str=Header(...,alias='Wish-Hmac-Sha256'))->Any:
    digest = hmac.new(settings.WISH_SECRET, body.encode('utf-8'), hashlib.sha256).digest()#type: ignore
    computed_hmac = base64.b64encode(digest)#type: ignore
    if computed_hmac!=Wish_Hmac_Sha256:#type: ignore
        raise Exception("not valid from wish")#type: ignore


    retdata=await Service.wishService.getAccessToken()#type: ignore
    print("tokenfromwish:", retdata)#type: ignore
    access_token = retdata['data']['access_token']#type: ignore
    refresh_token = retdata['data']['refresh_token']#type: ignore
    access_token_expire=parser.parse(retdata['data']['expiry_time']).timestamp()#type: ignore

    # await cache.set('wishrefreshtoken', self.refresh_token)
    pass