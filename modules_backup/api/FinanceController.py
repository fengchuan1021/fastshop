# generated timestamp: 2022-10-29T02:15:06+00:00

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import settings
from component.dbsession import get_webdbsession
from common.globalFunctions import get_token
from common import XTJsonResponse

from .__init__ import dependencies
from .FinanceShema import (
    ApiFinanceOrderSettlementsGetRequest,
    ApiFinanceOrderSettlementsGetResponse,
    ApiFinanceSettlementsSearchPostRequest,
    ApiFinanceSettlementsSearchPostResponse,
    ApiFinanceTransactionsSearchPostRequest,
    ApiFinanceTransactionsSearchPostResponse,
)

router = APIRouter(dependencies=dependencies)


# <editor-fold desc="GetTransactions post: /api/finance/transactions/search">
@router.post(
    '/api/finance/transactions/search',
    response_class=XTJsonResponse,
    response_model=ApiFinanceTransactionsSearchPostResponse,
    
)
async def GetTransactions(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFinanceTransactionsSearchPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetTransactions
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFinanceTransactionsSearchPostResponse()


# </editor-fold>


# <editor-fold desc="GetOrderSettlements get: /api/finance/order/settlements">
@router.get(
    '/api/finance/order/settlements',
    response_class=XTJsonResponse,
    response_model=ApiFinanceOrderSettlementsGetResponse,
    
)
async def GetOrderSettlements(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFinanceOrderSettlementsGetRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetOrderSettlements
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFinanceOrderSettlementsGetResponse()


# </editor-fold>


# <editor-fold desc="GetSettlements post: /api/finance/settlements/search">
@router.post(
    '/api/finance/settlements/search',
    response_class=XTJsonResponse,
    response_model=ApiFinanceSettlementsSearchPostResponse,
    
)
async def GetSettlements(
    app_key: str,
    timestamp: str = ...,
    sign: str = ...,
    access_token: str = ...,
    shop_id: str = ...,
    body: ApiFinanceSettlementsSearchPostRequest = ...,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    GetSettlements
    """

    # install pydantic plugin,press alt+enter auto complete the args.
    return ApiFinanceSettlementsSearchPostResponse()


# </editor-fold>
