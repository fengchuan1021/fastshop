from typing import Any

from XTTOOLS import XTJsonResponse
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

import Service
import settings
from common import get_token
from component.dbsession import get_webdbsession
from .__init__ import dependencies


router = APIRouter(dependencies=dependencies)
# <editor-fold desc="onlineproductdetail get: /merchant/onlineproductdetail/{store_id}/product_id">



@router.get(
    "/merchant/merchant/selfauthrizeurl/{store_id}",
    response_class=XTJsonResponse,
    #response_model=MerchantOnlineproductStoreIdGetResponse,
)
async def selfauthrizeurl(
    store_id:int,
    db: AsyncSession = Depends(get_webdbsession),
    token: settings.UserTokenData = Depends(get_token),
) -> Any:
    """
    wishonlineproductdetail
    """
    data=await Service.thirdmarketService.getSelfAuthrizeUrl(
        db, token.merchant_id, store_id
    )

    return {'status':'success','data':data}


# </editor-fold>
