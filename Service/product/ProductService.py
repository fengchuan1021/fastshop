#type: ignore
import Service
from Service.base import CRUDBase
import Models
from typing import Union, Optional, List, Dict
from datetime import datetime, timedelta
import settings
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import and_, or_
from common.filterbuilder import filterbuilder

from sqlalchemy.orm import undefer_group

from sqlalchemy import select,text
from component.cache import cache



class ProductService(CRUDBase[Models.Product]):

    @cache(key_builder='getpkcachename',expire=3600*48)
    async def findByPk(self,dbSession: AsyncSession,id:int,lang:str='')->Models.Product:
        if lang:
            statment=select(Models.Product).options(undefer_group(lang)).where(self.model.id==id)
        else:
            statment = select(Models.Product).where(self.model.id==id)
        print(statment)
        results = await dbSession.execute(statment)
        return results.scalar_one_or_none()

    async def findByAttribute(self,dbsession:AsyncSession,filters:Dict={},sep:str=' and ',lang:str='en')->List[Models.Product]:
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
        async with getdbsession() as db:
            newproduct=Models.Product(productName_en='english productname',
                                      productDescription_en='english productdescription',
                                      brand_en='english brand',
                                      productName_cn="产品1颜色红",
                                      productDescription_cn="这个产品很有用",
                                      brand_cn="红的的图片",
                                      )
            db.add(newproduct)


    async def testselect():
        async with getdbsession() as db:
            ps = ProductService(Models.Product)
            tmp=await ps.findByPk(db, 66706553062818882, 'en')


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

    async def updateproduct(id):
        async with getdbsession() as db:
            product=await Service.productService.findByPk(db,id)

            product.brand_en="dior122"
            product.brand_cn='444'
            db.add(product)


    async def delproduct(id):
        async with getdbsession() as db:
            model=await Service.productService.findByPk(db,id)
            if model:
                await db.delete(model)

    #asyncio.run(delproduct())
    #asyncio.run(testcategory())
    #asyncio.run(testfindbyattributes())
    #asyncio.run(testselect())
    #asyncio.run(inserttestproduct())
    asyncio.run(updateproduct(66731785458811970))
    #asyncio.run(delproduct(66706553062818882))

