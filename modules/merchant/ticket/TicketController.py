# generated timestamp: 2022-11-29T09:01:02+00:00

from __future__ import annotations

from typing import Any, Dict, Literal

from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common import CommonResponse, XTJsonResponse, get_token
from component.cache import cache
from component.dbsession import get_webdbsession
from component.fastQL import fastAdd, fastDel, fastQuery

from .__init__ import dependencies
#from .ProductShema import MerchantOnlineproductStoreIdGetResponse

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="listtickets">
@router.get(
    "/merchant/tickets/{store_id}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def listtickets(
    store_id: int,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    onlineproduct
    """
    data=await Service.thirdmarketService.getTickets(
        db, token.merchant_id, store_id
    )

    return {'status':'success','data':data}


# </editor-fold>


# <editor-fold desc="ticketdetail">
@router.get(
    "/merchant/tickets/{store_id}/{ticket_id}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def ticketdetail(
    store_id: int,
    ticket_id:str,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    onlineproduct
    """
    data=await Service.thirdmarketService.getTicketDetail(
        db, token.merchant_id, store_id,ticket_id
    )

    return {'status':'success','data':data}


# </editor-fold>


# <editor-fold desc="closeticket">
class State(BaseModel):
    state:Literal["CLOSED","AWAITING_MERCHANT","AWAITING_WISH"]
@router.put(
    "/merchant/tickets/{store_id}/{ticket_id}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def closeticket(
    store_id: int,
    ticket_id:str,
    body:State,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    onlineproduct
    """
    if body.state=="CLOSED":
        data=await Service.thirdmarketService.closeTicket(
            db, token.merchant_id, store_id,ticket_id
        )
    else:
        return {'status':'failed','message':'not emplemented'}

    return {'status':'success','data':data}


# </editor-fold>


# <editor-fold desc="closeticket">
class Reply(BaseModel):
    content:str
@router.post(
    "/merchant/tickets/{store_id}/{ticket_id}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def replay(
    store_id: int,
    ticket_id:str,
    body:Reply,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    onlineproduct
    """

    data=await Service.thirdmarketService.replyTicket(
        db, token.merchant_id, store_id,ticket_id,body.content
    )

    return {'status':'success','data':data}


# </editor-fold>
