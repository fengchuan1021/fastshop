import Service
from Service.base import CRUDBase
import Models
from typing import Union, Optional, List
from datetime import datetime, timedelta
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_
from common.filterbuilder import filterbuilder

from sqlalchemy.orm import undefer_group

from sqlalchemy import select,text
from component.cache import cache



class ProductService(CRUDBase[Models.Product]):

    @cache(expire=3600*24)
    async def findByPk(self,dbSession: AsyncSession,id,lang='')->Models.Product:
        if lang:
            statment=select(Models.Product).options(undefer_group(lang)).where(self.model.id==id)
        else:
            statment = select(Models.Product).where(self.model.id==id)
        print(statment)
        results = await dbSession.execute(statment)
        return results.scalar_one_or_none()

    async def findByAttribute(self,dbsession:AsyncSession,filters={},sep=' and ',lang='en')->List[Models.Product]:
        filter=filterbuilder(filters,sep)
        statment=select(self.model).where(text(filter))
        results=await dbsession.execute(statment)
        tmp=results.scalars().all()
        print('tmp::',tmp)
        return tmp
if __name__ == "__main__":
    import asyncio
    from common.dbsession import getdbsession
    async def inserttestproduct():
        db = await getdbsession()
        newproduct=Models.Product(productName_en='english productname',
                                  productDescription_en='english productdescription',
                                  brand_en='english brand',
                                  productName_cn="产品1颜色红",
                                  productDescription_cn="这个产品很有用",
                                  brand_cn="红的的图片",
                                  )
        db.add(newproduct)
        await db.commit()
        await db.close()

    async def testselect():
        db = await getdbsession()
        ps = ProductService(Models.Product)
        tmp=await ps.findByPk(db, 6, 'en')


        await db.close()

        await cache.close()
    async def testfindbyattributes():
        async with getdbsession() as db:
            ps = ProductService(Models.Product)
            tmp=await ps.findByAttribute(db, {"id__in":[2,3]}, 'en')
            print('tmp::',tmp)


            await cache.close()

    async def testcategory():
        async with getdbsession() as db:

            result=await Service.categoryService.findByPk(db,1)
            print(result)
        await cache.close()
    asyncio.run(testcategory())
    #asyncio.run(testfindbyattributes())
    #asyncio.run(testselect())
    #asyncio.run(inserttestproduct())

