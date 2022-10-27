from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

import Service


class PaymentService():
    async def getSession(self,db:AsyncSession,method:str,order_id:str)->Dict:
        if cls:=getattr(Service,f'{method}Service',None):
            return await cls.getSession(db,order_id)
        else:
            raise Exception(f"{method} payment not implement")

    async def refund(self,db:AsyncSession,order_id:str)->Dict:
        pass



