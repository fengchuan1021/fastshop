#type: ignore
import Service
import asyncio
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

class ProductDynamicService(CRUDBase[Models.ProductDynamic]):
    def __int__(self):
        super().__init__(Models.ProductDynamic,False)

class ProductStaticService(CRUDBase[Models.ProductStatic]):

    @cache(key_builder='getpkcachename',expire=3600*48)
    async def findByPk(self,dbSession: AsyncSession,id:int,lang:str='')->Models.ProductStatic:
        if lang:
            statment=select(Models.ProductStatic).options(undefer_group(lang)).where(self.model.id==id)
        else:
            statment = select(Models.ProductStatic).where(self.model.id==id)
        print(statment)
        results = await dbSession.execute(statment)
        return results.scalar_one_or_none()

    async def findByAttribute(self,dbsession:AsyncSession,filters:Dict={},sep:str=' and ',lang:str='en')->List[Models.ProductStatic]:
        filter=filterbuilder(filters,sep)
        statment=select(self.model).where(text(filter))
        results=await dbsession.execute(statment)
        tmp=results.scalars().all()
        print('tmp::',tmp)
        return tmp
from pydantic import BaseModel

class ProductDynamicInSchema(BaseModel):
    is_hot:Optional[str]="TRUE"
    is_recommend:Optional[str]="TRUE"


class ProductInSchema(BaseModel):
    productName_en: str
    productDescription_en: str
    brand_en: str
    price: float
    dynamic:Optional[ProductDynamicInSchema]



class ProductService():
    def __int__(self):
        super().__init__(Models.ProductDynamic,False)

    async def findByPk(self,db:AsyncSession,id:int,lang:str='',with_dynamic=True):
        funcarr=[Service.productStaticService.findByPk(db,id,lang)]
        if with_dynamic:
            funcarr.append(Service.productDynamicService.findByPk(db,id))

        results=await asyncio.gather(*funcarr)

        modelstatic=results[0]
        if not modelstatic:
            return None
        if with_dynamic:
            modelstatic.dynamic=results[1]
        return modelstatic
    async def addproduct(self,db:AsyncSession,jsonSchema:ProductInSchema)->Models.ProductStatic:

        model=Models.ProductStatic(**jsonSchema.dict(exclude={'dynamic'}))
        dic=jsonSchema.dict()
        if dic['dynamic']:
            dyncmicmodel=Models.ProductDynamic(**dic['dynamic'])
        else:
            dyncmicmodel = Models.ProductDynamic()

        model.dynamic=dyncmicmodel
        db.add(model)

if __name__ == "__main__":
    import asyncio
    from common.dbsession import getdbsession
    async def addproduct():
        async with getdbsession() as db:
            pd= ProductDynamicInSchema(is_hot="TRUE", is_recommend="TRUE")
            ps= ProductInSchema(productName_en='pen', productDescription_en='p desc en', brand_en='br en', price=99.99,dynamic=pd)
            await Service.productService.addproduct(db,ps)

    async def findbyproductpk():
        async with getdbsession() as db:
            tmp=await Service.productService.findByPk(db,68451662070547522)
            print(tmp)

    asyncio.run(findbyproductpk())
    #asyncio.run(addproduct())

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
            tmp=await ps.findByPk(db, 66731785458811970, 'en')
            db.add(tmp)
            print('111111')
            print(tmp.dynamic.statement)



    async def testfindbyattributes():
        async with getdbsession() as db:
            ps = ProductService(Models.Product)
            tmp=await ps.findByAttribute(db, {"id__in":[2,3]}, 'en')
            #print('tmp::',tmp)


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
    #asyncio.run(updateproduct(66731785458811970))
    #asyncio.run(delproduct(66706553062818882))

