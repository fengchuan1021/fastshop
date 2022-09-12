from Service.base import CRUDBase
import Models
from typing import Union,Optional
from datetime import datetime, timedelta
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_


from sqlalchemy.orm import undefer_group

from sqlalchemy import select




class ProductService(CRUDBase[Models.Product]):

    async def findByPk(self,dbSession: AsyncSession,id,lang='')->Models.Product:
        if lang:
            statment=select(Models.Product).options(undefer_group(lang)).where(self.model.id==id)
        else:
            statment = select(Models.Product).where(self.model.id==id)
        print(statment)
        results = await dbSession.execute(statment)
        return results.scalar_one_or_none()


if __name__ == "__main__":
    import asyncio
    from common.dbsession import getdbsession
    async def main():
        db = await getdbsession()
        ps = ProductService(Models.Product)
        await ps.findByPk(db, 1,'en')
    loop=asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

